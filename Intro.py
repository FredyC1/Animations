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
        self.play(FadeIn(functionimg))
        #revrese
        self.play(FadeOut(functionimg), run_time=2)
        self.play(Unwrite(functionTextEquals))
        self.play(FadeIn(arrow, arrow2, input, output, box, box2), run_time=1)
        self.play(functionText.animate.shift(RIGHT*5+DOWN*3), run_time=2)
        self.play(Unwrite(functionText))
        #Sigma/sigmoid functions
        sigmaText = MathTex(r"\sum_{i=1}^n f(i)", color=BLUE)
        sigmaText[0][2].set_color(YELLOW)  
        sigmaText[0][7].set_color(YELLOW)

        self.play(Write(sigmaText))
        self.play(Unwrite(sigmaText))
        sigmoidText = MathTex(r"\sigma","(","x",")",color=BLUE).set_height(0.6)
        sigmoidText[2].set_color(YELLOW)
        self.play(Write(sigmoidText))
        self.play(Unwrite(sigmoidText))

        # Functions
        softmax_tex = MathTex(r"\text{softmax}(x_i)", color=BLUE).set_height(0.3)
        softmax_tex[0][8].set_color(YELLOW)
        reLu_tex = MathTex(r"\text{ReLU}(x)", color=BLUE).set_height(0.4)
        reLu_tex[0][5].set_color(YELLOW)
        Diracdelta_tex = MathTex(r"\delta(x)", color=BLUE).set_height(0.5)
        Diracdelta_tex[0][2].set_color(YELLOW)
        gamma_tex = MathTex(r"\Gamma(x)", color=BLUE).set_height(0.5)
        gamma_tex[0][2].set_color(YELLOW)
        erf_tex = MathTex(r"\text{erf}(x)", color=BLUE).set_height(0.5)
        erf_tex[0][4].set_color(YELLOW)
        bessel_tex = MathTex(r"J_n(x)", color=BLUE).set_height(0.5)
        bessel_tex[0][3].set_color(YELLOW)
        zeta_tex = MathTex(r"\zeta(s)", color=BLUE).set_height(0.5)
        zeta_tex[0][2].set_color(YELLOW)
        softplus_tex = MathTex(r"\text{softplus}(x)", color=BLUE).set_height(0.3)
        softplus_tex[0][9].set_color(YELLOW)
        self.play(Write(softmax_tex), run_time=0.5)
        self.play(Unwrite(softmax_tex), run_time=0.5)
        self.play(Write(softplus_tex), run_time=0.5)
        self.play(Unwrite(softplus_tex), run_time=0.5)
        self.play(Write(reLu_tex), run_time=0.5)
        self.play(Unwrite(reLu_tex), run_time=0.5)
        self.play(Write(Diracdelta_tex), run_time=0.4)
        self.play(Unwrite(Diracdelta_tex), run_time=0.4)
        self.play(Write(gamma_tex), run_time=0.4)
        self.play(Unwrite(gamma_tex), run_time=0.4)
        self.play(Write(erf_tex), run_time=0.4)
        self.play(Unwrite(erf_tex), run_time=0.4)
        self.play(Write(bessel_tex), run_time=0.4)
        self.play(Unwrite(bessel_tex), run_time=0.4)
        self.play(Write(zeta_tex), run_time=0.4)
        self.play(Unwrite(zeta_tex), run_time=0.4)
        self.wait(0.7)
        sigmaText = MathTex(r"\sum_{i=1}^n f(i)", color=BLUE)
        sigmaText[0][2].set_color(YELLOW)
        sigmaText[0][7].set_color(YELLOW)
        self.play(FadeOut(arrow, arrow2, input, output, box, box2), FadeIn(sigmaText), run_time=1.5)
        self.play(sigmaText.animate.shift(LEFT*5+UP*3), run_time=2)


