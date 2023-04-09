from manim import *


FONT_SIZE = 24
FIGURE_COLOR = YELLOW_C
FILL_COLOR = YELLOW_C
CHAR_COLOR = YELLOW_E


class Areas(Scene):
    def construct(self):
        text = Text(
            'Wszystko zaczęło się od punktu.',
            font_size=FONT_SIZE,
        )
        self.play(FadeIn(text))
        self.wait()
        self.play(FadeOut(text))

        point = Dot(color=FIGURE_COLOR)
        char = Tex('A', color=CHAR_COLOR).next_to(point, UP)
        area_formula = MathTex('P =', '?').shift(DOWN)
        area_formula.set_color_by_tex('?', CHAR_COLOR)

        self.play(FadeIn(point, char, area_formula))
        self.wait(2)
        self.play(FadeOut(area_formula))

        line = Line(LEFT, RIGHT, color=FIGURE_COLOR)
        new_char = MathTex('a', color=CHAR_COLOR).next_to(line, UP)
        area_formula = MathTex('P =', 'a').shift(DOWN)
        area_formula.set_color_by_tex('a', CHAR_COLOR)

        lpoint, rpoint = point, point.copy()
        self.play(
            char.animate.set_color(GREY),
            lpoint.animate.move_to(LEFT),
            rpoint.animate.move_to(RIGHT),
        )
        self.play(
            Create(line),
            char.animate.become(new_char),
            FadeIn(area_formula)
        )
        self.wait(2.5)
        self.play(FadeOut(area_formula))

        char.add_updater(lambda m, _=None: m.next_to(line, UP), call_updater=True)
        lpoint.add_updater(lambda m, _=None: m.move_to(line.get_start()), call_updater=True)
        rpoint.add_updater(lambda m, _=None: m.move_to(line.get_end()), call_updater=True)

        lside = Line(LEFT+UP*2, LEFT, color=FIGURE_COLOR)
        rside = Line(RIGHT+UP*2, RIGHT, color=FIGURE_COLOR)

        bottom_lpoint = Dot(color=FIGURE_COLOR)
        bottom_lpoint.add_updater(lambda m, _=None: m.move_to(lside.get_end()), call_updater=True)
        bottom_rpoint = Dot(color=FIGURE_COLOR)
        bottom_rpoint.add_updater(lambda m, _=None: m.move_to(rside.get_end()), call_updater=True)
        bottom_line = Line(bottom_lpoint, bottom_rpoint, color=FIGURE_COLOR)
        bottom_line.add_updater(
            lambda m, _=None: m.set_y(lside.get_end()[1]), call_updater=True
        )

        side_char = Tex('?', color=GREY).next_to(rpoint, RIGHT)
        side_char.add_updater(lambda m, _=None: m.next_to(rside.get_center(), RIGHT))
        fill = VMobject()
        fill.add_updater(lambda m, _=None: m.become(Polygon(
            lpoint.get_center(), rpoint.get_center(), rside.get_end(), lside.get_end(),
            stroke_width=0, fill_color=FILL_COLOR, fill_opacity=0.5
        )))

        self.play(line.animate.shift(UP*2))

        area_formula = MathTex('P =', 'a', r'\cdot', '?').shift(DOWN)
        area_formula.set_color_by_tex('a', CHAR_COLOR)
        area_formula.set_color_by_tex('?', GREY)
        self.play(FadeIn(area_formula))
        self.add(bottom_lpoint, bottom_rpoint, bottom_line, side_char, fill)

        side_creation_runtime = 4
        self.play(
            Create(lside, run_time=side_creation_runtime),
            Create(rside, run_time=side_creation_runtime),
        )

        comparison_line = Line(line.get_end(), line.get_start(), color=FIGURE_COLOR)
        comparison_line_end = lpoint.copy()
        comparison_line_end.add_updater(lambda m, _=None: m.move_to(comparison_line.get_end()))
        self.add(comparison_line_end)
        self.play(
            Rotate(
                comparison_line, PI/2,
                about_point=line.get_end(),
                rate_func=linear,
                run_time=1.2
            )
        )
        self.play(
            Circumscribe(line, color=GREY),
            Circumscribe(comparison_line, color=GREY),
            side_char.animate.become(
                MathTex('a', color=CHAR_COLOR).next_to(rside.get_center(), RIGHT),
            ),
            area_formula.animate.become(
                MathTex('P =', 'a', r'\cdot', 'a').shift(DOWN).set_color_by_tex('a', CHAR_COLOR)
            )
        )
        self.remove(comparison_line, comparison_line_end)

        self.wait()

        square = Square(color=FIGURE_COLOR, fill_color=FILL_COLOR, fill_opacity=0.5).shift(UP)

        self.add(square)
        self.remove(lside, rside, bottom_line, fill, line)
        self.play(
            FadeOut(
                lpoint, rpoint,
                bottom_lpoint, bottom_rpoint,
                side_char,
                run_time=0.4
            ),
        )
        side_char.clear_updaters()
        side_char.add_updater(
            lambda m, _=None: m.next_to(square.get_left(), LEFT), call_updater=True
        )
        char.clear_updaters()
        char.add_updater(
            lambda m, _=None: m.next_to(square.get_top(), UP), call_updater=True
        )
        self.play(
            FadeIn(side_char, lag_ratio=0.01, run_time=0.4),
        )
        self.play(
            square.animate.scale(0.5).shift(UP+LEFT*2),
        )
