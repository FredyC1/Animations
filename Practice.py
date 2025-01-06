from manim import *

class moveObject(Scene):
    def construct(self):

        box = Rectangle(stroke_color = GREEN_C, stroke_opacity=0.7,
        fill_color = RED_B, fill_opacity = 0.5, height=1, width=1)

        self.add(box)
        self.play(box.animate.shift(DOWN*3), run_time=2)
        self.play(box.animate.shift(RIGHT*6), run_time=2)
        self.play(box.animate.shift(UP*6), run_time=2)
        self.play(box.animate.shift(LEFT*12), run_time=2)
        self.play(box.animate.shift(DOWN*6), run_time=2)
        self.play(box.animate.shift(RIGHT*6), run_time=2)
        self.play(box.animate.shift(UP*3), run_time=2)


class fittingObject(Scene):
    def construct(self):
        axes = Axes (x_range=[-7,7,1], y_range=[-4,4,1],
        x_length = 14, y_length=8, tips=False)
        # axes.to_edge(LEFT, buff=7)  # Changes the cordinates of the axis
        # axes.add_coordinates()  # Numbers the graph

        circle = Circle(stroke_width = 6, stroke_color = YELLOW, 
        fill_color = RED_C, fill_opacity = 0.8)
        circle.set_width(3) # .to_edge(DOWN, buff=1) #Cordinates are at the bottom(Y-3)

        triangle = Triangle(stroke_color = RED, stroke_width = 10,
        fill_color = GREY).set_height(2).shift(UP*2+RIGHT*3)

        # self.play(Write(axes))
        self.add(axes)
        self.play(DrawBorderThenFill(circle))
        self.play(circle.animate.set_width(1))
        self.play(Transform(circle, triangle), run_time=3)

class Updaters(Scene):
    def construct(self):
        axes = Axes (x_range=[-7,7,1], y_range=[-4,4,1],
        x_length = 14, y_length=8, tips=False)

        rectangle = RoundedRectangle(stroke_width = 8, stroke_color = WHITE,
        fill_color = BLUE_B, width = 4.5, height = 2).shift(UP*2.5+LEFT*4)

        mathtext = MathTex(r"\sum_{n=1}^{10} n")
        mathtext.set_color_by_gradient(GREEN, PINK).set_height(1.5) 
        # mathtext.move_to(rectangle.get_center()) #Unnececsary 
        mathtext.add_updater(lambda x : x.move_to(rectangle.get_center()))
        
        self.add(axes)
        self.play(FadeIn(rectangle))
        self.play(Write(mathtext))
        self.play(rectangle.animate.shift(DOWN*5), run_time=4)
        self.wait()
        # mathtext.clear_updaters()
        self.play(rectangle.animate.shift(RIGHT*8), run_time=4)
        self.wait()
        self.play(rectangle.animate.shift(UP*5), run_time=4)
        self.wait()
        self.play(rectangle.animate.shift(LEFT*8), run_time=4)


# manim Practice.py -pqm

class Tute4(Scene):
    def construct(self):
        axes = Axes (x_range=[-7,7,1], y_range=[-4,4,1],
        x_length = 14, y_length=8, tips=False)

        r = ValueTracker(1) #tracks the value of the radius

        circle = always_redraw(lambda :
        Circle(radius = r.get_value(), stroke_color = YELLOW,
        stroke_width = 5))

        line_radius = always_redraw(lambda :
        Line(start = circle.get_center(), end = circle.get_bottom(), stroke_color = RED_B,
        stroke_width = 15))

        line_circumference = always_redraw(lambda :
        Line(stroke_color = YELLOW, stroke_width = 2
        ).set_length(2 * r.get_value() * PI).next_to(circle, DOWN, buff = 0.2))

        triangle = always_redraw(lambda :
        Polygon(circle.get_top(), circle.get_left(), circle.get_right(), fill_color = GREEN_C))

        self.add(axes)
        self.play(
        Create(circle), DrawBorderThenFill(line_radius), DrawBorderThenFill(triangle),
        run_time = 4)
        self.play(ReplacementTransform(circle.copy(), line_circumference), run_time = 2)
        self.play(r.animate.set_value(2), run_time = 5)
       

