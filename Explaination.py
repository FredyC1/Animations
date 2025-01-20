from manim import *

class formula(Scene):
    def construct(self):
        axes = Axes(x_range=[-7,7,1], y_range=[-4,4,1], x_length=14, y_length=8, tips=False)
        sigmaAxes = Axes(x_range=[-7,7,1], y_range=[-4,4,1], x_length=7, y_length=4, tips=False)
        sigmaText = MathTex(r"\sum_{i=1}^n f(i)", color=BLUE,).shift(LEFT*5+UP*3)
        sigmaText[0][2].set_color(YELLOW)  
        sigmaText[0][7].set_color(YELLOW)
        # self.add(axes) 
        self.play(Write(sigmaText))
        functionTextEquals = MathTex("=", "x", color=BLUE).set_height(0.3)
        functionTextEquals[1].set_color(YELLOW)
        functionTextEquals.next_to(sigmaText, RIGHT)
        self.play(Write(functionTextEquals), run_time=1)
        self.play(Write(sigmaAxes), run_time=2)
        


