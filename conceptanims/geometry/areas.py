from manim import *


FONT_SIZE = 24
FIGURE_COLOR = YELLOW_C
FILL_COLOR = YELLOW_C
CHAR_COLOR = YELLOW_D
CHAR_COLOR_SPECIAL = YELLOW_E


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
        self.wait()
        self.play(Indicate(area_formula))

        line = Line(LEFT, RIGHT, color=FIGURE_COLOR)
        new_char = MathTex('a', color=CHAR_COLOR).next_to(line, UP)
        line_area_formula = MathTex('P =', 'a').shift(DOWN)
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
            area_formula.animate.become(line_area_formula)
        )
        self.wait()
        self.play(Indicate(area_formula))

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
            stroke_width=0, fill_color=FILL_COLOR, fill_opacity=0.7
        )))

        self.play(line.animate.shift(UP*2))

        square_area_formula = MathTex('P =', 'a', r'\cdot', '?').shift(DOWN)
        square_area_formula.set_color_by_tex('a', CHAR_COLOR)
        square_area_formula.set_color_by_tex('?', GREY)
        self.add(bottom_lpoint, bottom_rpoint, bottom_line, fill)

        side_creation_runtime = 4
        self.play(
            FadeIn(side_char, lag_ratio=0.01),
            area_formula.animate.become(square_area_formula),
            Create(lside, run_time=side_creation_runtime),
            Create(rside, run_time=side_creation_runtime),
        )

        comparison_line = line.copy().set_color(WHITE)
        self.play(Create(comparison_line))
        self.play(
            comparison_line.animate.become(rside.copy().set_color(WHITE)),
        )
        self.play(Uncreate(comparison_line))
        self.play(
            side_char.animate.become(
                MathTex('a', color=CHAR_COLOR).next_to(rside.get_center(), RIGHT),
            ),
            area_formula.animate.become(
                MathTex('P =', 'a', r'\cdot', 'a').shift(DOWN).set_color_by_tex('a', CHAR_COLOR)
            )
        )

        self.wait()
        self.play(Indicate(area_formula))

        square = Square(color=FIGURE_COLOR, fill_color=FILL_COLOR, fill_opacity=0.7).shift(UP)

        self.add(square)
        self.remove(comparison_line, lside, rside, bottom_line, fill, line)
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
        self.play(square.animate.scale(0.5).shift(LEFT*0.5))
        duplicate_square = square.copy()
        duplicate_char = char.copy()
        duplicate_char.clear_updaters()
        duplicate_char.add_updater(
            lambda m, _=None: m.next_to(duplicate_square.get_top(), UP), call_updater=True
        )

        self.add(duplicate_char)
        self.play(
            char.animate.set_color(CHAR_COLOR_SPECIAL),
            duplicate_char.animate.set_color(CHAR_COLOR_SPECIAL),
            duplicate_square.animate.shift(RIGHT),
            area_formula.animate.become(
                MathTex(
                    'P =', 'a', r'\cdot', '(a+a)'
                ).shift(DOWN).set_color_by_tex('(a+a)', CHAR_COLOR_SPECIAL)
            )
        )

        square.side_length = square.width
        rectangle = Rectangle(
            height=square.side_length,
            width=square.side_length*2,
            color=FIGURE_COLOR,
            fill_color=FILL_COLOR,
            fill_opacity=0.7
        ).shift(UP)
        old_char, char = char, MathTex('b', color=CHAR_COLOR_SPECIAL).next_to(rectangle.get_top(), UP)

        self.play(
            old_char.animate.move_to(char),
            duplicate_char.animate.move_to(char),
            FadeOut(square, duplicate_square, old_char, duplicate_char),
            FadeIn(rectangle, char),
            LaggedStart(
                area_formula.animate.become(
                    MathTex(
                        'P =', 'a', r'\cdot', 'b',
                    ).shift(DOWN)
                    .set_color_by_tex('a', CHAR_COLOR)
                    .set_color_by_tex('b', CHAR_COLOR_SPECIAL)
                ),
                lag_ratio=0.1,
            )
        )
        self.remove(old_char, duplicate_char)
        self.add(char)
        self.wait()
        self.play(Indicate(area_formula))
