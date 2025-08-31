from manim import *
import numpy as np

class GaussianDistribution(Scene):
    def construct(self):
        # Title, in the persona of Gauss
        title = Text("A Study of the Error Curve", font_size=48)
        author = Text("by C.F. Gauss", font_size=24).next_to(title, DOWN, buff=0.2)
        self.play(Write(title), Write(author))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(author))

        # Gauss introduces the concept
        intro_text = Text(
            "In my astronomical observations, I noticed that errors in measurement\n"
            "are not chaotic, but follow a predictable pattern.",
            font_size=28
        ).to_edge(UP)
        self.play(Write(intro_text))
        self.wait(3)
        self.play(FadeOut(intro_text))

        # The Gaussian Function
        formula = MathTex(
            r"f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}",
            font_size=48
        )
        self.play(Write(formula))
        self.wait(3)

        # Explain the components
        explanation = Text("This is the formula for my distribution.", font_size=24).next_to(formula, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(explanation))

        # Graph the distribution
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            x_length=10,
            y_length=6,
            axis_config={"include_tip": False},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Define the Gaussian function for the graph
        def gaussian(x, mu=0, sigma=1):
            return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

        curve = axes.plot(lambda x: gaussian(x), color=BLUE)
        self.play(FadeOut(formula), Create(axes), Create(labels))
        self.play(Create(curve))
        self.wait(2)

        # Explain Mean and Standard Deviation
        mean_line = axes.get_vertical_line(axes.c2p(0, gaussian(0)), color=YELLOW)
        mean_label = MathTex(r"\mu").next_to(mean_line, DOWN)

        std_dev_line = Brace(Line(axes.c2p(0, 0), axes.c2p(1, 0)), direction=DOWN)
        std_dev_label = std_dev_line.get_tex(r"\sigma")

        self.play(Create(mean_line), Write(mean_label))
        self.wait(1)
        self.play(Create(std_dev_line), Write(std_dev_label))
        self.wait(2)

        # Concluding remarks
        conclusion = Text(
            "This 'bell curve' shows that small errors are more likely than large ones.",
            font_size=28
        ).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects])