import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import minimize

# --- 1. Define the True Bimodal Distribution p(x) ---
# This is a mixture of two Gaussian distributions.
# This is the "complex" reality we are trying to approximate.
p_mix = 0.4
p_loc1, p_scale1 = -3, 0.8
p_loc2, p_scale2 = 3, 1.2

def p_pdf(x):
    """The probability density function (PDF) of our bimodal distribution p(x)."""
    return p_mix * norm.pdf(x, loc=p_loc1, scale=p_scale1) + \
           (1 - p_mix) * norm.pdf(x, loc=p_loc2, scale=p_scale2)

def sample_from_p(n_samples):
    """Draws samples from the true bimodal distribution p(x)."""
    n1 = int(n_samples * p_mix)
    n2 = n_samples - n1
    samples1 = norm.rvs(loc=p_loc1, scale=p_scale1, size=n1)
    samples2 = norm.rvs(loc=p_loc2, scale=p_scale2, size=n2)
    return np.concatenate([samples1, samples2])

# --- 2. Define Objective Functions for KL Divergence Minimization ---

# Objective for minimizing D_KL(q || p) -- "Reverse KL"
# This is used in variational inference. We need to sample from q.
def reverse_kl_objective(params):
    """
    Approximates the KL divergence D_KL(q || p) using Monte Carlo sampling.
    We minimize E_q[log q(x) - log p(x)].
    """
    mu_q, log_sigma_q = params
    sigma_q = np.exp(log_sigma_q)  # Ensure sigma is positive

    # 1. Sample from the approximating distribution q(z)
    samples_from_q = norm.rvs(loc=mu_q, scale=sigma_q, size=2000)

    # 2. Calculate the terms of the expectation
    log_q = norm.logpdf(samples_from_q, loc=mu_q, scale=sigma_q)
    log_p = np.log(p_pdf(samples_from_q) + 1e-10) # Add epsilon for stability

    # We want to minimize KL, so we return the mean of (log_q - log_p)
    return np.mean(log_q - log_p)

# Objective for minimizing D_KL(p || q) -- "Forward KL"
# This is equivalent to Maximum Likelihood Estimation. We just need samples from p.
def forward_kl_objective(params, samples_from_p):
    """
    Calculates the negative log-likelihood, which is equivalent to
    minimizing D_KL(p || q) up to a constant.
    We minimize E_p[-log q(x)].
    """
    mu_q, log_sigma_q = params
    sigma_q = np.exp(log_sigma_q) # Ensure sigma is positive

    # Calculate the log-likelihood of samples from p under q
    log_likelihood = norm.logpdf(samples_from_p, loc=mu_q, scale=sigma_q)

    # We want to maximize likelihood, so we minimize the negative log-likelihood
    return -np.sum(log_likelihood)


# --- 3. Run the Optimization ---

# Generate a large number of samples from p for the forward KL calculation
p_samples = sample_from_p(5000)

# Initial guess for the parameters of q (mu, log(sigma))
initial_guess = [0.0, np.log(2.0)]

# Find optimal q for Reverse KL: D_KL(q || p)
# This finds a q that avoids placing mass where p is zero.
print("Optimizing for Reverse KL: D_KL(q || p)... (Mode-Seeking)")
res_reverse = minimize(
    reverse_kl_objective,
    initial_guess,
    method='L-BFGS-B'
)
mu_reverse, sigma_reverse = res_reverse.x[0], np.exp(res_reverse.x[1])
print(f"Result -> mu = {mu_reverse:.2f}, sigma = {sigma_reverse:.2f}\n")


# Find optimal q for Forward KL: D_KL(p || q)
# This finds a q that covers all the areas where p has mass.
print("Optimizing for Forward KL: D_KL(p || q)... (Mass-Covering)")
res_forward = minimize(
    lambda params: forward_kl_objective(params, p_samples),
    initial_guess,
    method='L-BFGS-B'
)
mu_forward, sigma_forward = res_forward.x[0], np.exp(res_forward.x[1])
print(f"Result -> mu = {mu_forward:.2f}, sigma = {sigma_forward:.2f}")


# --- 4. Plot the Results ---
x_domain = np.linspace(-8, 8, 500)
q_reverse_pdf = norm.pdf(x_domain, loc=mu_reverse, scale=sigma_reverse)
q_forward_pdf = norm.pdf(x_domain, loc=mu_forward, scale=sigma_forward)

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the true distribution p(x)
ax.plot(x_domain, p_pdf(x_domain), color='black', linestyle='--', linewidth=3, label='True Bimodal p(x)')

# Plot the Reverse KL result
ax.plot(x_domain, q_reverse_pdf, color='red', linewidth=2, label='Fit via min D_KL(q || p) [Mode-Seeking]')

# Plot the Forward KL result
ax.plot(x_domain, q_forward_pdf, color='blue', linewidth=2, label='Fit via min D_KL(p || q) [Mass-Covering]')

# Fill areas to show the nature of the fit
ax.fill_between(x_domain, q_reverse_pdf, color='red', alpha=0.2)
ax.fill_between(x_domain, q_forward_pdf, color='blue', alpha=0.2)

# Formatting
ax.set_title('KL Divergence Asymmetry: Approximating a Bimodal Distribution', fontsize=16)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('Probability Density', fontsize=12)
ax.legend(fontsize=11)
ax.set_ylim(0, 0.3)
ax.set_yticks([]) # Hide y-axis ticks for clarity
plt.tight_layout()
plt.show()
