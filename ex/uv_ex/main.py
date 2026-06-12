from manim import *

# run: uv run manim -ql main.py CreateCircle

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

def main():
    print("Hello from uv-ex!")


if __name__ == "__main__":
    main()
