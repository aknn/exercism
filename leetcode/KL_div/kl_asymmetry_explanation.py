import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

"""
Understanding KL Divergence Asymmetry through log(p/q) Analysis

This file demonstrates how the behavior of log(p/q) drives the fundamental
asymmetry between forward KL D_KL(p || q) and reverse KL D_KL(q || p).

Key insight: The role of p and q switches between the two formulations,
leading to dramatically different penalty structures.
"""

# Setup the same bimodal distribution from the main example
p_mix = 0.4
p_loc1, p_scale1 = -3, 0.8
p_loc2, p_scale2 = 3, 1.2

def p_pdf(x):
    """True bimodal distribution"""
    return p_mix * norm.pdf(x, loc=p_loc1, scale=p_scale1) + \
           (1 - p_mix) * norm.pdf(x, loc=p_loc2, scale=p_scale2)

def analyze_log_ratio_behavior():
    """
    Analyze how log(p/q) behaves in different scenarios and how this
    drives the asymmetry between forward and reverse KL.
    """

    print("=" * 70)
    print("UNDERSTANDING KL DIVERGENCE ASYMMETRY THROUGH log(p/q)")
    print("=" * 70)

    # Create domain for analysis
    x = np.linspace(-8, 8, 1000)
    p_vals = p_pdf(x)

    # Define two different q distributions to compare
    # q1: Narrow Gaussian at left mode (what reverse KL might find)
    q1_mu, q1_sigma = -3, 0.8
    q1_vals = norm.pdf(x, loc=q1_mu, scale=q1_sigma)

    # q2: Wide Gaussian covering both modes (what forward KL might find)
    q2_mu, q2_sigma = 0, 3
    q2_vals = norm.pdf(x, loc=q2_mu, scale=q2_sigma)

    print("\nSCENARIO ANALYSIS:")
    print("-" * 50)

    # Analyze different regions
    regions = [
        ("Left Mode (x ≈ -3)", -3, -2.5),
        ("Between Modes (x ≈ 0)", -0.5, 0.5),
        ("Right Mode (x ≈ 3)", 2.5, 3.5),
        ("Far Tail (x ≈ 6)", 5.5, 6.5)
    ]

    for region_name, x_start, x_end in regions:
        print(f"\n{region_name}:")

        # Get representative point
        x_rep = (x_start + x_end) / 2
        p_val = p_pdf(x_rep)
        q1_val = norm.pdf(x_rep, loc=q1_mu, scale=q1_sigma)
        q2_val = norm.pdf(x_rep, loc=q2_mu, scale=q2_sigma)

        print(f"  p(x) = {p_val:.6f}")
        print(f"  q1(x) = {q1_val:.6f} (narrow)")
        print(f"  q2(x) = {q2_val:.6f} (wide)")

        # Calculate log ratios (with small epsilon to avoid log(0))
        eps = 1e-10

        if p_val > eps and q1_val > eps:
            log_p_q1 = np.log(p_val / q1_val)
            print(f"  log(p/q1) = {log_p_q1:.3f}")
        else:
            print(f"  log(p/q1) = undefined (zero densities)")

        if p_val > eps and q2_val > eps:
            log_p_q2 = np.log(p_val / q2_val)
            print(f"  log(p/q2) = {log_p_q2:.3f}")
        else:
            print(f"  log(p/q2) = undefined (zero densities)")

    return x, p_vals, q1_vals, q2_vals, q1_mu, q1_sigma, q2_mu, q2_sigma

def explain_kl_formulations():
    """
    Explain the mathematical formulations and how log ratios drive behavior
    """

    print("\n" + "=" * 70)
    print("KL DIVERGENCE FORMULATIONS AND LOG RATIO ANALYSIS")
    print("=" * 70)

    print("""
FORWARD KL: D_KL(p || q) = ∫ p(x) log(p(x)/q(x)) dx = E_p[log(p/q)]

Key points about Forward KL:
1. We sample from p (the true distribution)
2. We evaluate log(p(x)/q(x)) at those samples
3. When p(x) is high but q(x) is low → log(p/q) is large and POSITIVE
4. This creates a LARGE PENALTY when q fails to assign probability where p does
5. Result: q must "cover" all regions where p has mass (mass-covering)

REVERSE KL: D_KL(q || p) = ∫ q(x) log(q(x)/p(x)) dx = E_q[log(q/p)]

Key points about Reverse KL:
1. We sample from q (our approximation)
2. We evaluate log(q(x)/p(x)) at those samples
3. When q(x) is high but p(x) is low → log(q/p) is large and POSITIVE
4. This creates a LARGE PENALTY when q assigns probability where p doesn't
5. Result: q avoids regions where p ≈ 0 (mode-seeking)
""")

def demonstrate_penalty_structure():
    """
    Show concrete examples of how penalties work
    """

    print("\n" + "=" * 70)
    print("PENALTY STRUCTURE ANALYSIS")
    print("=" * 70)

    # Example scenarios
    scenarios = [
        ("High p, Low q", 0.1, 0.01),
        ("Low p, High q", 0.01, 0.1),
        ("Both High", 0.1, 0.1),
        ("Both Low", 0.01, 0.01)
    ]

    print("\nHow log ratios create different penalties:")
    print("-" * 50)

    for scenario, p_val, q_val in scenarios:
        forward_penalty = p_val * np.log(p_val / q_val) if p_val > 0 and q_val > 0 else float('inf')
        reverse_penalty = q_val * np.log(q_val / p_val) if p_val > 0 and q_val > 0 else float('inf')

        print(f"\n{scenario}: p={p_val}, q={q_val}")
        print(f"  log(p/q) = {np.log(p_val/q_val):.2f}")
        print(f"  log(q/p) = {np.log(q_val/p_val):.2f}")
        print(f"  Forward KL contribution: p×log(p/q) = {forward_penalty:.4f}")
        print(f"  Reverse KL contribution: q×log(q/p) = {reverse_penalty:.4f}")

def create_visualization(x, p_vals, q1_vals, q2_vals, q1_mu, q1_sigma, q2_mu, q2_sigma):
    """
    Create comprehensive visualization of log ratio behavior
    """

    # Calculate log ratios with epsilon for numerical stability
    eps = 1e-10
    log_p_q1 = np.log((p_vals + eps) / (q1_vals + eps))
    log_p_q2 = np.log((p_vals + eps) / (q2_vals + eps))
    log_q1_p = np.log((q1_vals + eps) / (p_vals + eps))
    log_q2_p = np.log((q2_vals + eps) / (p_vals + eps))

    # Create subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('KL Divergence Asymmetry: Understanding through log(p/q)', fontsize=16)

    # Plot 1: Probability distributions
    ax1 = axes[0, 0]
    ax1.plot(x, p_vals, 'k-', linewidth=3, label='True p(x)')
    ax1.plot(x, q1_vals, 'r-', linewidth=2, label=f'q₁(x): N({q1_mu}, {q1_sigma}²)')
    ax1.plot(x, q2_vals, 'b-', linewidth=2, label=f'q₂(x): N({q2_mu}, {q2_sigma}²)')
    ax1.set_title('Probability Distributions')
    ax1.set_xlabel('x')
    ax1.set_ylabel('Density')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot 2: log(p/q) ratios
    ax2 = axes[0, 1]
    ax2.plot(x, log_p_q1, 'r-', linewidth=2, label='log(p/q₁)')
    ax2.plot(x, log_p_q2, 'b-', linewidth=2, label='log(p/q₂)')
    ax2.axhline(y=0, color='k', linestyle='--', alpha=0.5)
    ax2.set_title('Forward KL: log(p/q) ratios')
    ax2.set_xlabel('x')
    ax2.set_ylabel('log(p/q)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(-10, 10)

    # Plot 3: log(q/p) ratios
    ax3 = axes[1, 0]
    ax3.plot(x, log_q1_p, 'r-', linewidth=2, label='log(q₁/p)')
    ax3.plot(x, log_q2_p, 'b-', linewidth=2, label='log(q₂/p)')
    ax3.axhline(y=0, color='k', linestyle='--', alpha=0.5)
    ax3.set_title('Reverse KL: log(q/p) ratios')
    ax3.set_xlabel('x')
    ax3.set_ylabel('log(q/p)')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_ylim(-10, 10)

    # Plot 4: KL contributions (integrand)
    ax4 = axes[1, 1]
    forward_contrib_1 = p_vals * log_p_q1
    forward_contrib_2 = p_vals * log_p_q2
    reverse_contrib_1 = q1_vals * log_q1_p
    reverse_contrib_2 = q2_vals * log_q2_p

    ax4.plot(x, forward_contrib_1, 'r--', linewidth=2, label='p×log(p/q₁) [Forward]')
    ax4.plot(x, forward_contrib_2, 'b--', linewidth=2, label='p×log(p/q₂) [Forward]')
    ax4.plot(x, reverse_contrib_1, 'r:', linewidth=2, label='q₁×log(q₁/p) [Reverse]')
    ax4.plot(x, reverse_contrib_2, 'b:', linewidth=2, label='q₂×log(q₂/p) [Reverse]')
    ax4.axhline(y=0, color='k', linestyle='-', alpha=0.5)
    ax4.set_title('KL Divergence Integrands')
    ax4.set_xlabel('x')
    ax4.set_ylabel('Contribution to KL')
    ax4.legend(fontsize=9)
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    return log_p_q1, log_p_q2, log_q1_p, log_q2_p

def numerical_kl_calculation(x, p_vals, q1_vals, q2_vals):
    """
    Calculate actual KL divergences numerically
    """
    print("\n" + "=" * 70)
    print("NUMERICAL KL DIVERGENCE CALCULATIONS")
    print("=" * 70)

    eps = 1e-10
    dx = x[1] - x[0]  # Grid spacing for numerical integration

    # Forward KL calculations
    # D_KL(p || q1)
    log_p_q1 = np.log((p_vals + eps) / (q1_vals + eps))
    forward_kl_1 = np.sum(p_vals * log_p_q1 * dx)

    # D_KL(p || q2)
    log_p_q2 = np.log((p_vals + eps) / (q2_vals + eps))
    forward_kl_2 = np.sum(p_vals * log_p_q2 * dx)

    # Reverse KL calculations
    # D_KL(q1 || p)
    log_q1_p = np.log((q1_vals + eps) / (p_vals + eps))
    reverse_kl_1 = np.sum(q1_vals * log_q1_p * dx)

    # D_KL(q2 || p)
    log_q2_p = np.log((q2_vals + eps) / (p_vals + eps))
    reverse_kl_2 = np.sum(q2_vals * log_q2_p * dx)

    print(f"Forward KL D_KL(p || q₁) = {forward_kl_1:.4f}")
    print(f"Forward KL D_KL(p || q₂) = {forward_kl_2:.4f}")
    print(f"Reverse KL D_KL(q₁ || p) = {reverse_kl_1:.4f}")
    print(f"Reverse KL D_KL(q₂ || p) = {reverse_kl_2:.4f}")

    print(f"\nKey Observations:")
    print(f"1. Forward KL prefers q₂ (wide): {forward_kl_2:.4f} < {forward_kl_1:.4f}")
    print(f"2. Reverse KL prefers q₁ (narrow): {reverse_kl_1:.4f} < {reverse_kl_2:.4f}")
    print(f"3. Asymmetry: D_KL(p||q₁)={forward_kl_1:.4f} ≠ D_KL(q₁||p)={reverse_kl_1:.4f}")

def main():
    """
    Run the complete analysis
    """
    print("Note: Probability densities can be > 1! They're not probabilities.")
    print("For a narrow Gaussian, the peak density can be much greater than 1.")
    print("What matters for probabilities is that ∫ p(x)dx = 1\n")

    # Run analysis
    x, p_vals, q1_vals, q2_vals, q1_mu, q1_sigma, q2_mu, q2_sigma = analyze_log_ratio_behavior()
    explain_kl_formulations()
    demonstrate_penalty_structure()

    # Create visualization
    log_ratios = create_visualization(x, p_vals, q1_vals, q2_vals, q1_mu, q1_sigma, q2_mu, q2_sigma)

    # Calculate numerical KL values
    numerical_kl_calculation(x, p_vals, q1_vals, q2_vals)

    print("\n" + "=" * 70)
    print("SUMMARY: WHY THE ASYMMETRY MATTERS")
    print("=" * 70)
    print("""
The asymmetry in KL divergence comes from the fundamental difference in
how we weight the log ratios:

FORWARD KL: E_p[log(p/q)]
- Samples come from p (true distribution)
- Large penalties when p is high but q is low
- Forces q to cover all modes of p
- Used in Maximum Likelihood Estimation

REVERSE KL: E_q[log(q/p)]
- Samples come from q (our approximation)
- Large penalties when q is high but p is low
- Forces q to avoid regions where p ≈ 0
- Used in Variational Inference (VAEs, etc.)

This is why VAEs often suffer from "posterior collapse" - the reverse KL
objective encourages the approximate posterior to be narrow and focused
on a single mode, rather than capturing the full complexity of the true
posterior distribution.
""")

if __name__ == "__main__":
    main()
