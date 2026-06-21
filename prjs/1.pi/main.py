from manim import *

class Pi(Scene):

    def add_ticks(self, line, tick_length = 0.15):
        direction = line.get_unit_vector()
        perp = rotate_vector(direction, PI/2) # perpendicular direction

        half_a_tick = perp * tick_length

        tick_start = Line(
            line.get_start() - half_a_tick,
            line.get_start() + half_a_tick
        )

        tick_end = Line(
            line.get_end() - half_a_tick,
            line.get_end() + half_a_tick
        )

        return VGroup(tick_start, tick_end)
    
    def get_rolling_mob(self, c, phi, n_points = 300):
        # c = circle
        # phi = rotation angle
        # n_points = number of points used to represent the cut circumference

        r = c.radius
        contact_point = c.get_bottom()
        origin = contact_point + UP * r
        current_origin = origin + RIGHT * r * phi   # distance = radius * rotation_angle

        points = []
        for i in range(n_points):
            s = 2 * PI * i / n_points               # angle between [0, 2PI]

            if s <= phi:    # the point is on the x axis
                point = contact_point + RIGHT * r * s
            else:           # the point is somewhere on the current position of the circle
                theta = - PI / 2 + (s - phi)    # the point is at this angle on the circle
                point = current_origin + r * np.array([np.cos(theta), np.sin(theta), 0])

            points.append(point)
        
        # Create a VMobject by iterpolating points
        mob = VMobject(color = c.get_color())
        mob.set_points_smoothly(points)
        return mob
    
    def add_tick_at(self, point, tick_length = 0.15):
        return Line(
            point + DOWN * tick_length,
            point + UP * tick_length
        )

    def construct(self):
        t = MathTex(r"\pi = \ ?")
        # r = raw text so \p is not considered an special character
        # \ = explicit space (Latex sometimes chooses to ignore spaces)
        t.scale(2)
        self.play(Write(t))
        self.wait()
        
        t1 = MathTex(
            r"\pi = \frac{\text{\scriptsize circumference}}{\text{\scriptsize diameter}}"
        )
        # \scriptsize = text size (\tiny → \scriptsize → \footnotesize → \small → \normalsize → \large → \Large → \LARGE → \huge → \Huge)
        t1.scale(1.5)
        self.play(TransformMatchingShapes(t, t1))
        t = t1
        self.wait()
        
        hidden_t = t.copy().to_edge(UP, buff = 0.5)
        t1 = MathTex(r"\text{\small Let's consider a circle of diameter 1 unit}").next_to(hidden_t, DOWN, buff = 0.7)
        c = Circle(radius = 1.3)
        c.to_edge(DOWN, buff = 1.7)
        self.play(
            t.animate.to_edge(UP, buff = 0.5),
            Succession(Wait(0.5), Create(t1), Create(c))
        )
        self.wait()

        d = Line(c.get_left(), c.get_right())
        d_label = MathTex(r"1 \ \text{u}")
        d_label.scale(1.5)
        d_label.next_to(d, UP, buff = 0.3)
        ticks = self.add_ticks(d)
        
        self.play(
            Create(d),
            Create(ticks),
            Write(d_label)
        )
        self.wait()

        grp = VGroup(c, d, d_label, ticks)
        self.play(grp.animate.to_edge(LEFT, buff = 2), Uncreate(t1))
        self.wait()

        x_axis = NumberLine(
            x_range = [0, 5, 1],   # [start, stop, step]
            unit_size = d.get_length(),
            include_numbers = True,
            numbers_to_include = [0, 1, 2, 3, 4]
        )
        zero_point = x_axis.number_to_point(0)
        target_point = c.get_corner(DL)
        x_axis.shift(target_point - zero_point)
        self.play(Create(x_axis))
        self.wait()

        self.play(grp.animate.shift(LEFT * (d.get_length() / 2)))
        self.play(FadeOut(d, d_label, ticks))
        self.wait()

        tracker = ValueTracker(0)
        c_rolling = always_redraw(lambda: self.get_rolling_mob(c, tracker.get_value()))
        self.remove(c)
        self.add(c_rolling)
        self.play(tracker.animate.set_value(2 * PI), run_time = 3, rate_func = smooth)
        self.wait()

        pi_position = c.get_bottom() + RIGHT * d.get_length() * PI
        pi_tick = self.add_tick_at(pi_position)
        pi_label = MathTex(r"\pi")
        pi_label.scale(1.5)
        pi_label.next_to(pi_tick, UP, buff = 0.3)
        pi_tick_grp = VGroup(pi_tick, pi_label)
        self.play(Create(pi_tick_grp))
        self.wait()

        self.remove(c_rolling)
        fixed_c_rolling = c_rolling.copy()
        self.add(fixed_c_rolling)
        x_axis_grp = VGroup(x_axis, fixed_c_rolling, pi_tick_grp)
        self.play(
            x_axis_grp.animate
                .scale(3, about_point = pi_tick.get_center()) # or pi_position
                .shift(ORIGIN - pi_tick.get_center() + DOWN * 1)
        )
        self.wait()

        pi_label_full = MathTex(r"\pi = \text{\scriptsize 3.14159...}")
        pi_label_full.scale(1.5 * 3)
        pi_label_full.move_to(pi_label)
        self.play(TransformMatchingShapes(pi_label, pi_label_full))
        self.wait()

        pi_tick_grp.remove(pi_label)
        pi_label = pi_label_full
        self.play(
            FadeOut(x_axis_grp),
            pi_label.animate
                .set(font_size = t.font_size)
                .next_to(t, DOWN, buff = 1)
                .align_to(t, LEFT)
        )
        self.wait()

        t1 = MathTex(
            r"\pi = \ &\text{\scriptsize how many times}\\[-0.7em]",
            r"&\text{\scriptsize the diameter fits}\\[-0.7em]",
            r"&\text{\scriptsize around the circle}"
        )
        # & = the alignment point
        # \\ = new line
        # [-0.7em] = reduces vertical space
        #       em = font's size
        t1.set(font_size = t.font_size)\
          .next_to(pi_label, DOWN, buff = 1)\
          .align_to(t, LEFT)
        self.play(Write(t1))
        self.wait()
