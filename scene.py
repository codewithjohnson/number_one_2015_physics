# a text animated using manim
from manim import *


# write text at center of the screen, then animate drag up

class WriteText(Scene):
    def construct(self):
        # logo text is "studentFirst" in the bottom right corner
        logo = MarkupText(
            "studentFirst", gradient=(RED, YELLOW), font_size=18).to_corner(DR)
        self.play(FadeIn(logo), run_time=1)

        text = MarkupText(
            '<span>A particle with rest mass m moves with speed 0.6c. Calculate its </span> <span  foreground="yellow">kinetic energy.</span>', color=WHITE, font_size=24, line_spacing=0.5, should_center=True)

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
        option_objects = []
        left = 3
        # display options one by one using latex and animate them up to the left side by side

        for i in range(len(options)):
            option = MathTex(options[i], color=WHITE,
                             font_size=24)
            option.next_to(text, DOWN*2).shift(LEFT*left*1.5)
            left -= 1
            self.play(Write(option), run_time=1)
            option_objects.append(option)

        solutionText = MarkupText(
            '<span> SOLUTION </span>', color=YELLOW, font_size=24, line_spacing=0.5, should_center=True)
        solutionText.next_to(option, DOWN*2)
        self.play(Write(solutionText), run_time=1)

        # shrink the question and options and move them to the left side  top of the screen
        question_group = VGroup(text, *option_objects)
        question_group.generate_target()
        question_group.target.scale(0.9).to_corner(UL)
        self.play(MoveToTarget(question_group), run_time=2)

        # move solutionText up
        solutionText.generate_target()
        solutionText.target.shift(UP)
        self.play(MoveToTarget(solutionText), run_time=1)

        line1 = Text(
            'given values: u = 0 m/s, m= 0, v = 0.6c', color=WHITE, font_size=20)
        line1.next_to(solutionText, DOWN*1)

        line2 = MathTex(
            '\\textnormal{kinetic energy, } K.E = \\frac{1}{2} m(v-u)^2', color=WHITE, font_size=20)
        line2.next_to(line1, DOWN*1)

        line3 = MathTex(
            'K.E = \\frac{1}{2} m(0.6c-0)^2', color=WHITE, font_size=20)
        line3.next_to(line2, DOWN*1)

        line4 = MathTex(
            '\\textnormal{inserting values, we get: }K.E = 0.5 \\times m \\times (0.6c)^2', color=WHITE, font_size=20)
        line4.next_to(line3, DOWN*1)

        line5 = MathTex(
            'Kinetic energy = 0.18 mc^2', color=WHITE, font_size=20)
        line5.next_to(line4, DOWN*1)

        # create a rectangle around the correct answer
        rect = SurroundingRectangle(option_objects[0], color=YELLOW)

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
