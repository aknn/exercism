from manim import *

class SupplyAndDemand(Scene):
    def construct(self):
        # Title
        title = Text("Microeconomics: Supply and Demand").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

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

        # Create supply and demand curves
        demand_curve = axes.plot(lambda x: 8 - 0.5 * x, color=BLUE)
        demand_label = axes.get_graph_label(demand_curve, "Demand", x_val=8, direction=UP)

        supply_curve = axes.plot(lambda x: 0.5 * x + 2, color=YELLOW)
        supply_label = axes.get_graph_label(supply_curve, "Supply", x_val=8, direction=UP)

        self.play(Create(demand_curve), Write(demand_label))
        self.wait(1)
        self.play(Create(supply_curve), Write(supply_label))
        self.wait(1)

        # Find and mark the equilibrium point
        # This is a simplified approach for this specific case
        # For y = 8 - 0.5x and y = 0.5x + 2
        # 8 - 0.5x = 0.5x + 2  =>  6 = x
        x_intersection = 6
        y_intersection = 0.5 * x_intersection + 2
        intersection_point = axes.c2p(x_intersection, y_intersection)

        dot = Dot(intersection_point, color=RED)
        
        h_line = axes.get_horizontal_line(intersection_point, color=RED, stroke_width=2)
        v_line = axes.get_vertical_line(intersection_point, color=RED, stroke_width=2)

        equilibrium_label = Text("Equilibrium", font_size=24).next_to(dot, RIGHT)

        self.play(Create(h_line), Create(v_line), Create(dot))
        self.play(Write(equilibrium_label))
        self.wait(2)

        # Explanation
        explanation = (
            Text("The point where supply and demand meet is the equilibrium.", font_size=24)
            .next_to(axes, DOWN, buff=0.5)
        )
        self.play(Write(explanation))
        self.wait(3)
