# a text animated using manim
from manim import *


class KineticEnergy(Scene):
    def construct(self):

        text = MarkupText(
            '<span>A particle with rest mass m moves with speed 0.6c. Calculate its </span> <span  foreground="yellow">kinetic energy.</span>', color=WHITE, font_size=29, line_spacing=0.5, should_center=True)

        self.play(Write(text), run_time=5)
        self.wait(1)
        self.play(ApplyMethod(text.shift, UP*3))

        # create list of options
        options = [
            'a. 0.18 mc^2',
            'b. 0.22 mc^2',
            'c. 0.25 mc^2',
            'd. mc^2',
        ]

        option_2 = MathTex(options[1], color=WHITE)
        option_3 = MathTex(options[2], color=WHITE)
        option_4 = MathTex(options[3], color=WHITE)
        option_1 = MathTex(options[0], color=WHITE)

        optionGroup = VGroup(option_1, option_2, option_3,
                             option_4).arrange(RIGHT, buff=0.5)

        optionGroup.next_to(text, DOWN*2)

        # write each option one by one
        self.play(Write(option_1), run_time=1)
        self.wait(1)

        self.play(Write(option_2), run_time=1)
        self.wait(1)

        self.play(Write(option_3), run_time=1)
        self.wait(1)

        self.play(Write(option_4), run_time=1)
        self.wait(1)

        solutionText = MarkupText(
            '<span> SOLUTION </span>', color=YELLOW, font_size=29, line_spacing=0.5, should_center=True)
        solutionText.next_to(optionGroup, DOWN*2)
        self.play(Write(solutionText), run_time=1)

        # shrink the question and options and move them to the left side  top of the screen
        question_group = VGroup(text, optionGroup)
        question_group.generate_target()
        question_group.target.scale(0.6).to_corner(UL)
        self.play(MoveToTarget(question_group), run_time=2)

        # move solutionText up
        solutionText.generate_target()
        # solutionText.target.next_to(question_group, DOWN*3)
        # self.play(MoveToTarget(solutionText), run_time=1)

        solutionText.target.shift(UP*1)
        self.play(MoveToTarget(solutionText), run_time=1)

        line1 = MathTex(
            '\\textnormal{given values: } u = 0 m/s, m= 0, v = 0.6c', color=WHITE)
        line1.next_to(solutionText, DOWN*1)

        line2 = MathTex(
            '\\textnormal{kinetic energy, } K.E = \\frac{1}{2} m(v-u)^2', color=WHITE, tex_to_color_map={"K.E": YELLOW})
        line2.next_to(line1, DOWN*1)

        line3 = MathTex(
            'K.E = \\frac{1}{2} m(0.6c-0)^2', color=WHITE)
        line3.next_to(line2, DOWN*1)

        line4 = MathTex(
            '\\textnormal{inserting values, we get: }K.E = 0.5 \\times m \\times (0.6c)^2', color=WHITE)
        line4.next_to(line3, DOWN*1)

        line5 = MathTex(
            '\\textnormal{Kinetic energy} = 0.18 mc^2', color=WHITE)
        line5.next_to(line4, DOWN*1)

        # create a rectangle around the correct answer
        rect = SurroundingRectangle(option_1, color=YELLOW)

        # animate the rectangle
        self.play(Create(rect), run_time=1)

        # animate solution VGroup items one by one
        self.play(Write(line1), run_time=1)
        self.wait(1)

        self.play(Write(line2), run_time=1)
        self.wait(1)

        self.play(Write(line3), run_time=1)
        self.wait(1)

        self.play(Write(line4), run_time=1)
        self.wait(1)

        self.play(Write(line5), run_time=1)
        self.wait(1)

   # logo text is "studentFirst" in the bottom right corner
        logo = MarkupText(
            "Muyiwa Johnson", gradient=(RED, YELLOW), font_size=29).to_corner(DR)
        self.play(FadeIn(logo), run_time=1)

        self.wait(2)
