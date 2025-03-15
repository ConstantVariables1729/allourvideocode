from manim import *

class SpinningWheel(Scene):
    def construct(self):

        wheelintor = self.create_wheel(sectors=4,ora=1)
        #The Intro
        nit = Text("In Mathematics nothing is Impossiable, just extremly unlikly:)",font_size=14).move_to(UP)
        wheelintor.next_to(nit, DOWN)

        self.play(
            Write(nit),
            Create(wheelintor),
            run_time = 2
        )
        self.spin_wheel(wheelintor,spins=10,spin_duration=6)
        self.play(
            FadeOut(nit),
            FadeOut(wheelintor)
        )
        # Create a wheel with 3 or 4 sectors
        wheel = self.create_wheel(sectors=4)  # Change to 3 or 4 as needed
        wheel2 = self.create_wheel(sectors=4, angles =[360/4, 360/8, 360/5, 360-(360/4+360/8+360/5)])
        self.play(Create(wheel))
        self.wait(1)

        # Spin the wheel
        self.spin_wheel(wheel)
        self.wait(2)
        self.play(
            ReplacementTransform(wheel, wheel2)
        )
        self.wait(2)
        self.spin_wheel(wheel2)

    def create_wheel(self, sectors=4, angles = None, ora = None):
        # Define colors for the sectors
        colors = [RED, GREEN, BLUE, YELLOW][:sectors]  # Adjust colors as needed
        if angles == None:
            angles = [360 / sectors for _ in range(sectors)]  # Equal angles for simplicity

        # Create the wheel
        if ora == None:
            ora = 2
        wheel = VGroup()
        start_angle = 0
        for i in range(sectors):
            sector = Sector(
                outer_radius=ora,
                angle=angles[i] * DEGREES,
                start_angle=start_angle * DEGREES,
                fill_color=colors[i],
                fill_opacity=0.8,
                stroke_color=WHITE,
                stroke_width=2
            )
            wheel.add(sector)
            start_angle += angles[i]

        # Add a center circle
        center = Circle(radius=0.2, color=WHITE, fill_opacity=1)
        wheel.add(center)

        return wheel

    def spin_wheel(self, wheel, spins=5, spin_duration=3):
        # Spin the wheel
        for _ in range(spins):
            self.play(Rotate(wheel, angle=TAU, rate_func=linear, run_time=spin_duration / spins))
        self.wait(1)

# Run the scene
if __name__ == "__main__":
    scene = SpinningWheel()
    scene.render()