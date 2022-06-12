from manim import *

class FirstVideo(Scene):
    def construct(self):
        subject = Text('Distance between 2 points').scale(1.4)
        subtitle = Text('in euclidian metric').scale(1.4)
        subtitle.set_y(-0.5)
        subject.set_y(1.0)

        self.play(Write(subject))
        self.play(Write(subtitle))
        group1 = Group(subject, subtitle)

        ax = Axes(
            x_range=[0, 10],
            y_range=[0, 10],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False},
        )
        labels = ax.get_axis_labels()
        point1 = ax.coords_to_point(1.5, 1)
        point2 = ax.coords_to_point(4, 4)
        dot1 = Dot(point1)
        dot2 = Dot(point2)

        #unsual point
        point_a = ax.coords_to_point(4, 1)
        dot_a = Dot(point_a)


        x1_text = Tex(r"($x_1$, $y_1$)").next_to(dot1, UP*0.3).scale(0.7)
        x2_text = Tex(r"($x_2$, $y_2$)").next_to(dot2, UP*0.3).scale(0.7)
        line_x1 = ax.get_vertical_line(point1, line_config={"dashed_ratio": 0.7}, color=YELLOW)
        line_x2 = ax.get_vertical_line(point2, line_config={"dashed_ratio": 0.7}, color=YELLOW)
        line_y1 = ax.get_horizontal_line(point1, line_config={"dashed_ratio": 0.7}, color=YELLOW)
        line_y2 = ax.get_horizontal_line(point2, line_config={"dashed_ratio": 0.7}, color=YELLOW)
        group2 = Group(ax, labels, dot1, dot2, line_x1, line_x2, line_y1, line_y2)

        self.play(ReplacementTransform(group1, group2))
        self.add(x1_text, x2_text)

        first_line = Line(dot1.get_center(), dot_a.get_center()).set_color(ORANGE)
        b1 = Brace(first_line, sharpness=0.7)
        b1_text = b1.get_tex("x_2-x_1").scale(0.8)

        self.play(Write(first_line))
        self.add(b1)
        self.play(Write(b1_text))

        second_line = Line(dot2.get_center(), dot_a.get_center()).set_color(ORANGE)
        b2 = Brace(second_line, direction=second_line.copy().rotate(PI / 2).get_unit_vector(), sharpness=0.7)
        b2_text = b2.get_tex("y_2-y_1").scale(0.8)
        aux_group = Group(x1_text, x2_text)
        self.play(Write(second_line))
        self.add(b2)
        self.play(Write(b2_text))
        self.wait(1)

        distance = Line(dot1.get_center(), dot2.get_center()).set_color(BLUE)

        self.play(ReplacementTransform(aux_group, distance))
        self.wait()

        curvedArrow = CurvedArrow(start_point=np.array([0,0,0]), end_point=np.array([-1.5, -1.10, 0]))

        self.play(Write(curvedArrow))

        text_distance = Text("Distance").set_x(1.2).set_color(BLUE).scale(0.7)

        self.play(Write(text_distance))

        group3 = Group(group1, group2, curvedArrow, b1, b2, text_distance)
        
        self.play(FadeOut(group3))

        group4 = Group(distance, first_line, second_line, b1_text, b2_text)

        self.play(group4.animate.shift(UP*2))
        self.play(group4.animate.shift(LEFT*3))
        self.play(b1_text.animate.shift(UP*0.5))
        self.play(b2_text.animate.shift(LEFT*0.5))

        d = Text("d", color=BLUE).scale(0.6)
        d.set_x(-4.6)
        d.set_y(0.7)

        self.play(Write(d))

        new_text = Text("Using Pythagoras' theorem", color=WHITE).scale(0.8)
        new_text.set_x(3)
        new_text.set_y(3)

        self.play(FadeIn(new_text))

        result = MathTex(r"d^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2", substrings_to_isolate="d").scale(0.9)
        result.set_color_by_tex("d", BLUE)
        result.set_x(3)
        result.set_y(0.5)
        
        d_2 = Tex("$d$", color=BLUE).scale(0.9)
        final_result = Tex(r"$ = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$").scale(0.9)
        final_result.set_x(3)
        final_result.set_y(-1)
        d_2.set_x(0)
        d_2.set_y(-1)

        self.play(Write(result))
        self.play(Write(d_2))
        self.play(Write(final_result))

        rect = Rectangle(height=1, width=6.2,color=ORANGE)
        rect.set_x(2.8)
        rect.set_y(-1)

        self.play(GrowFromCenter(rect,point_color=RED))
        self.wait(2)

        final_group = Group(rect, d_2, final_result, result, new_text, d, group4)



        circ = Circle(color=WHITE, radius=1.2)
        y = Tex(r"$\mathbb{Y}$", color=RED).scale(5)
        triangle = Triangle(color=BLUE, fill_opacity=1).scale(0.3)
        square = Square(color=GREEN, fill_opacity=1).scale(0.2)
        square.set_x(-0.83)
        square.set_y(0.15)
        triangle.set_x(0.8)
        triangle.set_y(0.15)
        circ.set_y(0.1)
        group_intro = Group(y, triangle, square)
        
        self.wait(0.5)
        
        self.play(ReplacementTransform(final_group, circ))
        self.play(FadeIn(group_intro))
        self.wait()