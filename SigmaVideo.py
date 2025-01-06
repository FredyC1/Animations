from manim import *

class Intro(Scene):
    def construct(self):
        axes = Axes(x_range=[-7,7,1], y_range=[-4,4,1],
        x_length=14, y_length=8, tips=False)

        #self.add(axes)
        functionText = MathTex("f(", "x", ")", color=BLUE).set_height(0.7)
        functionText[1].set_color(YELLOW)
        arrow = Arrow(start=LEFT, end=RIGHT, stroke_width=4, color=YELLOW).next_to(functionText, LEFT)
        arrow2 = Arrow(start=LEFT, end=RIGHT, stroke_width=4, color=BLUE).next_to(functionText, RIGHT)
        input = MathTex("x", color=YELLOW).set_height(0.3).next_to(arrow, LEFT).shift(LEFT*0.1)
        output = MathTex("y", color=BLUE).set_height(0.3).next_to(arrow2, RIGHT).shift(RIGHT*0.1)
        box = SurroundingRectangle(input, color=WHITE, stroke_width=4, buff=0.2)
        box2 = SurroundingRectangle(output, color=WHITE, stroke_width=4, buff=0.2)
        # self.add(axes) 
        self.play(Write(functionText), run_time=3)
        self.play(Write(input), run_time=0.5)
        self.play(Write(box))
        self.play(Write(arrow),run_time=1)
        self.wait(1)
        self.play(Write(arrow2),run_time=1)
        self.play(Write(output), run_time=0.5)
        self.play(Write(box2))
        # Fade out
        self.play(FadeOut(arrow, arrow2, input, output, box, box2), run_time=3)
        self.play(functionText.animate.shift(LEFT*5+UP*3), run_time=2)
        #Equals
        functionTextEquals = MathTex("=", "x", color=BLUE).set_height(0.3)
        functionTextEquals[1].set_color(YELLOW)
        functionTextEquals.next_to(functionText, RIGHT)

        
        self.play(Write(functionTextEquals))

        #image 
        functionimg = ImageMobject("images/function.jpeg")
        # functionimg.scale()
        self.play(FadeIn(functionimg))

        self.play(FadeOut(functionimg), run_time=2)
        self.play(Unwrite(functionTextEquals))
        self.play(FadeIn(arrow, arrow2, input, output, box, box2), run_time=1)
        self.play(functionText.animate.shift(RIGHT*5+DOWN*3), run_time=2)
        self.play(Unwrite(functionText))
        
        sigmaText = MathTex(r"\sum_{i=1}^n f(i)", color=BLUE)
        sigmaText[0][2].set_color(YELLOW)  
        sigmaText[0][7].set_color(YELLOW)

        self.play(Write(sigmaText))