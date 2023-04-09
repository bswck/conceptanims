from manim import *


class TrigonoClock(Scene):
    def construct(self):
        side_length = 7
        r = side_length / 2

        sine_line = VMobject(color=WHITE)
        cosine_line = VMobject(color=WHITE)
        sine_line_caption = VMobject()
        cosine_line_caption = VMobject()
        angle = VMobject()
        sine_value = DecimalNumber(0, num_decimal_places=3).to_corner(RIGHT + UP)
        cosine_value = DecimalNumber(1, num_decimal_places=3).to_corner(RIGHT + DOWN)

        def update_frame():
            x, y, z = radius_line.get_end()

            angle.become(Angle(horizontal_axis, radius_line, radius=0.6, color=PURPLE_E))

            cur_sine = y / r
            sine_colour = RED_E if cur_sine < 0 else WHITE

            cur_sine_line = Line((x, y, z), (x, 0, 0), color=sine_colour)
            sine_line.become(cur_sine_line)

            sine_value.set_value(cur_sine)
            sine_value.set_color(sine_colour)

            sine_sign = '=' if cur_sine == 0 else ('<' if cur_sine < 0 else '>')
            sine_line_caption.become(
                MathTex(
                    fr'\sin{{\alpha}} {sine_sign} 0',
                    font_size=25,
                    color=sine_colour,
                ).next_to(cur_sine_line, RIGHT, buff=0.15)
            )

            cur_cosine = (x - right_edge[0]) / r + 1
            cosine_colour = RED_E if cur_cosine < 0 else WHITE

            cur_cosine_line = Line(center, (x, 0, 0), color=cosine_colour)
            cosine_line.become(cur_cosine_line)

            cosine_value.set_value(cur_cosine)
            cosine_value.set_color(cosine_colour)

            cosine_sign = '=' if cur_cosine == 0 else ('<' if cur_cosine < 0 else '>')
            cosine_line_caption.become(
                MathTex(
                    fr'\cos{{\alpha}} {cosine_sign} 0',
                    font_size=25,
                    color=cosine_colour,
                ).next_to(cur_cosine_line, DOWN, buff=0.15)
            )

        sine_line.add_updater(lambda _: update_frame())
        base_square = Square(side_length, color=DARKER_GRAY, z_index=-2).to_corner(LEFT)
        circle = Circle(r, color=DARK_GRAY, z_index=-1).to_corner(LEFT)
        horizontal_axis = Line(
            circle.get_edge_center(LEFT),
            right_edge := circle.get_edge_center(RIGHT),
            z_index=-1,
            color=DARK_GRAY
        )
        horizontal_axis_name = MathTex('x', color=GRAY, font_size=24)
        horizontal_axis_name.next_to(horizontal_axis.get_end(), RIGHT, buff=0.1)
        vertical_axis = Line(
            circle.get_edge_center(DOWN),
            circle.get_edge_center(UP),
            z_index=-1,
            color=DARK_GRAY
        )
        vertical_axis_name = MathTex('y', color=GRAY, font_size=24)
        vertical_axis_name.next_to(vertical_axis.get_end(), UP, buff=0.1)
        radius_line = Line(
            center := vertical_axis.get_midpoint(),
            right_edge,
            z_index=-1,
            color=DARK_GRAY
        )
        sine_caption = MathTex(r'\sin{\alpha} = ')
        sine_caption.next_to(sine_value, LEFT, buff=0.35)
        cosine_caption = MathTex(r'\cos{\alpha} = ')
        cosine_caption.next_to(cosine_value, LEFT, buff=0.35)

        self.add(
            base_square,
            circle,
            horizontal_axis,
            horizontal_axis_name,
            vertical_axis,
            vertical_axis_name,
            radius_line,
            angle,
            sine_line,
            sine_line_caption,
            cosine_line,
            cosine_line_caption,
            sine_caption,
            sine_value,
            cosine_caption,
            cosine_value,
        )

        self.play(
            Rotate(
                radius_line,
                angle=2 * PI,
                about_point=radius_line.start,
                rate_func=linear,
                run_time=30
            )
        )
