from manim import *

class UtilityTheory(Scene):
    def construct(self):
        # Title
        title = Text("Microeconomics: Utility Theory").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction to Utility
        intro_text = Text("Utility is the satisfaction or happiness from consumption.", font_size=24).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # Create axes for Total Utility
        tu_axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 20, 5],
            x_length=9,
            y_length=5,
            axis_config={"include_tip": False},
        ).add_coordinates()
        tu_axes_labels = tu_axes.get_axis_labels(x_label="Units Consumed", y_label="Total Utility")

        self.play(Create(tu_axes), Write(tu_axes_labels))
        self.wait(1)

        # Total Utility Curve
        total_utility_curve = tu_axes.plot(lambda x: -0.5 * x**2 + 5 * x, color=GREEN)
        total_utility_label = tu_axes.get_graph_label(total_utility_curve, "Total Utility", x_val=4, direction=UP)

        self.play(Create(total_utility_curve), Write(total_utility_label))
        self.wait(2)

        # Transition to Marginal Utility
        self.play(FadeOut(total_utility_curve), FadeOut(total_utility_label), FadeOut(tu_axes), FadeOut(tu_axes_labels))

        # Create axes for Marginal Utility
        mu_axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 6, 1],
            x_length=9,
            y_length=5,
            axis_config={"include_tip": False},
        ).add_coordinates()
        mu_axes_labels = mu_axes.get_axis_labels(x_label="Units Consumed", y_label="Marginal Utility")

        self.play(Create(mu_axes), Write(mu_axes_labels))
        self.wait(1)

        # Marginal Utility Curve
        marginal_utility_curve = mu_axes.plot(lambda x: -x + 5, color=ORANGE)
        marginal_utility_label = mu_axes.get_graph_label(marginal_utility_curve, "Marginal Utility", x_val=3, direction=UP)

        self.play(Create(marginal_utility_curve), Write(marginal_utility_label))
        self.wait(1)

        # Diminishing Marginal Utility Explanation
        explanation = (
            Text("Marginal utility diminishes with each additional unit consumed.", font_size=24)
            .next_to(mu_axes, DOWN, buff=0.5)
        )
        self.play(Write(explanation))
        self.wait(3)

        self.play(FadeOut(explanation), FadeOut(marginal_utility_curve), FadeOut(marginal_utility_label), FadeOut(mu_axes), FadeOut(mu_axes_labels), FadeOut(title))
        self.wait(1)
