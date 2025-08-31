from manim import *

class Elasticity(Scene):
    def construct(self):
        # Title
        title = Text("Microeconomics: Elasticity").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction to Elasticity
        intro_text = Text("Elasticity measures how much one variable responds to a change in another.", font_size=24).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # Create axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=9,
            y_length=6,
            axis_config={"include_tip": False},
        ).add_coordinates()
        axes_labels = axes.get_axis_labels(x_label="Quantity", y_label="Price")

        self.play(Create(axes), Write(axes_labels))
        self.wait(1)

        # Inelastic Demand
        inelastic_demand_curve = axes.plot(lambda x: 8 - 2 * x, color=ORANGE)
        inelastic_label = axes.get_graph_label(inelastic_demand_curve, "Inelastic Demand", x_val=3, direction=UP)

        self.play(Create(inelastic_demand_curve), Write(inelastic_label))
        self.wait(1)

        inelastic_explanation = Text("Inelastic: Quantity changes less than price.", font_size=24).next_to(axes, DOWN, buff=0.5)
        self.play(Write(inelastic_explanation))
        self.wait(2)
        self.play(FadeOut(inelastic_explanation), FadeOut(inelastic_demand_curve), FadeOut(inelastic_label))


        # Elastic Demand
        elastic_demand_curve = axes.plot(lambda x: 6 - 0.2 * x, color=GREEN)
        elastic_label = axes.get_graph_label(elastic_demand_curve, "Elastic Demand", x_val=8, direction=UP)

        self.play(Create(elastic_demand_curve), Write(elastic_label))
        self.wait(1)

        elastic_explanation = Text("Elastic: Quantity changes more than price.", font_size=24).next_to(axes, DOWN, buff=0.5)
        self.play(Write(elastic_explanation))
        self.wait(3)
        self.play(FadeOut(elastic_explanation), FadeOut(elastic_demand_curve), FadeOut(elastic_label))
        self.play(FadeOut(axes), FadeOut(axes_labels), FadeOut(title))
        self.wait(1)
