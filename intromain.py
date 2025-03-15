from manim import *

class ChannelIntro(Scene):
    def construct(self):
        # Create the logo: C with a hat
        C = MathTex(r"\mathbb{C}").scale(3)  # Complex number C
        hat = MathTex(r"\hat{\ }").scale(3)  # Hat symbol

        # Position the hat directly above the C
        hat.next_to(C, UP, buff=0.1)  # Align the hat properly

        # Group C and hat together
        logo = VGroup(C, hat)

        # Position the logo off-screen to the left
        logo.move_to(LEFT * 4)  # Move it far enough to be off-screen
        
        self.play(
            Write(logo),
            run_time = 2
        )

        # Animate the logo floating in from the left
        self.play(logo.animate.move_to(LEFT * 2), run_time=2)  # Move it to the left side of the screen

        # Pause for a moment to show the logo
        self.wait(1)

        # Add the text "Constant Variables?"
        text = Tex("Constant Variables", font_size=48).next_to(logo, RIGHT, buff=0.5)
        self.play(Write(text), run_time=2)

        # Pause for a moment
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(logo), FadeOut(text), run_time=1)

# Render the scene
if __name__ == "__main__":
    scene = ChannelIntro()
    scene.render()