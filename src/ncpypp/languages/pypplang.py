import re
import math
import numpy as np

def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    div_ = ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    Sx = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)) / \
         div_
    Sy = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)) / \
         div_
    return Sx, Sy

class Pypplang:

    def __init__(self):
        self.id = 'pypplang'
        self.digits = "{0:.5f}"
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

    def expand(self, str):
        match = re.search(r'''^\[\[(.*)\]\]''', str)
        if match is None:
            return str
        match = match.group(1).lower()
        match = match.replace(" ", "")
        if match.startswith("rect:"):
            x = re.search(r'''(x=(-?\d*\.?\d*))''', str).group(2)
            y = re.search(r'''(y=(-?\d*\.?\d*))''', str).group(2)
            z = re.search(r'''(z=(-?\d*\.?\d*))''', str).group(2)
            l = re.search(r'''(l=(-?\d*\.?\d*))''', str).group(2)
            w = re.search(r'''(w=(-?\d*\.?\d*))''', str).group(2)
            h = re.search(r'''(h=(-?\d*\.?\d*))''', str).group(2)
            p = re.search(r'''(p=(-?\d*\.?\d*))''', str).group(2)
            f = re.search(r'''(f=(-?\d*))''', str).group(2)
            return self.rect(float(l), float(w), float(h),
                             float(f),
                             [float(x), float(y), float(z)],
                             float(p))
        elif match.startswith("sphere:"):
            X = re.search(r'''(x=(-?\d*\.?\d*))''', match).group(2)
            Y = re.search(r'''(y=(-?\d*\.?\d*))''', match).group(2)
            Z = re.search(r'''(z=(-?\d*\.?\d*))''', match).group(2)
            R = re.search(r'''(r_1=(-?\d*\.?\d*))''', match).group(2)
            r = re.search(r'''(r_2=(-?\d*\.?\d*))''', match).group(2)
            phi_1 = re.search(r'''(phi_1=(-?\d*\.?\d*))''',
                              match).group(2)
            phi_2 = re.search(r'''(phi_2=(-?\d*\.?\d*))''',
                              match).group(2)
            theta_1 = re.search(r'''(theta_1=(-?\d*\.?\d*))''',
                                match).group(2)
            theta_2 = re.search(r'''(theta_2=(-?\d*\.?\d*))''',
                                match).group(2)
            clearance = re.search(r'''(clearance=(-?\d*\.?\d*))''',
                                  match).group(2)
            retraction = re.search(r'''(retraction=(-?\d*\.?\d*))''',
                                   match).group(2)
            gap = re.search(r'''(gap=(-?\d*\.?\d*))''', match).group(2)
            f = re.search(r'''(f=(-?\d*))''', match).group(2)
            step = re.search(r'''(step=(-?\d*\.?\d*))''',
                             match).group(2)
            return self.sphere(float(X), float(Y), float(Z),
                               float(R), float(r), float(phi_1),
                               float(phi_2), float(theta_1), float(theta_2),
                               float(clearance), float(retraction),
                               float(gap), float(f), float(step))

        elif match.startswith("cylinder:"):
            X = re.search(r'''(x=(-?\d*\.?\d*))''', match).group(2)
            Y = re.search(r'''(y=(-?\d*\.?\d*))''', match).group(2)
            Z = re.search(r'''(z=(-?\d*\.?\d*))''', match).group(2)
            H = re.search(r'''(h=(-?\d*\.?\d*))''', match).group(2)
            R = re.search(r'''(r_1=(-?\d*\.?\d*))''', match).group(2)
            r = re.search(r'''(r_2=(-?\d*\.?\d*))''', match).group(2)
            phi_1 = re.search(r'''(phi_1=(-?\d*\.?\d*))''',
                              match).group(2)
            clearance = re.search(r'''(clearance=(-?\d*\.?\d*))''',
                                  match).group(2)
            retraction = re.search(r'''(retraction=(-?\d*\.?\d*))''',
                                   match).group(2)
            gap = re.search(r'''(gap=(-?\d*\.?\d*))''', match).group(2)
            f = re.search(r'''(f=(-?\d*))''', match).group(2)
            return self.cylinder(float(X), float(Y), float(Z), float(H),
                                 float(R), float(r), float(phi_1), float(1),
                                 float(clearance), float(retraction),
                                 float(gap), float(f))

        elif match.startswith("bore:"):
            X = re.search(r'''(x=(-?\d*\.?\d*))''', match).group(2)
            Y = re.search(r'''(y=(-?\d*\.?\d*))''', match).group(2)
            Z = re.search(r'''(z=(-?\d*\.?\d*))''', match).group(2)
            H = re.search(r'''(h=(-?\d*\.?\d*))''', match).group(2)
            R = re.search(r'''(r_1=(-?\d*\.?\d*))''', match).group(2)
            r = re.search(r'''(r_2=(-?\d*\.?\d*))''', match).group(2)
            phi_1 = re.search(r'''(phi_1=(-?\d*\.?\d*))''',
                              match).group(2)
            clearance = re.search(r'''(clearance=(-?\d*\.?\d*))''',
                                  match).group(2)
            retraction = re.search(r'''(retraction=(-?\d*\.?\d*))''',
                                   match).group(2)
            f = re.search(r'''(f=(-?\d*))''', match).group(2)
            return self.bore(float(X), float(Y), float(Z), float(H),
                                 float(R), float(r), float(phi_1), float(1),
                                 float(clearance), float(retraction),
                                 float(f))

        elif match.startswith("polybore:"):
            X = re.search(r'''(x=(-?\d*\.?\d*))''', match).group(2)
            Y = re.search(r'''(y=(-?\d*\.?\d*))''', match).group(2)
            Z = re.search(r'''(z=(-?\d*\.?\d*))''', match).group(2)
            H = re.search(r'''(h=(-?\d*\.?\d*))''', match).group(2)
            R = re.search(r'''(r_1=(-?\d*\.?\d*))''', match).group(2)
            r = re.search(r'''(r_2=(-?\d*\.?\d*))''', match).group(2)
            phi_1 = re.search(r'''(phi_1=(-?\d*\.?\d*))''',
                              match).group(2)
            clearance = re.search(r'''(clearance=(-?\d*\.?\d*))''',
                                  match).group(2)
            retraction = re.search(r'''(retraction=(-?\d*\.?\d*))''',
                                   match).group(2)
            f = re.search(r'''(f=(-?\d*))''', match).group(2)
            failure = re.search(r'''(failure=(-?\d*\.?\d*))''',
                                match).group(2)
            return self.polybore(float(X), float(Y), float(Z), float(H),
                                 float(R), float(r), float(phi_1), float(1),
                                 float(clearance), float(retraction),
                                 float(f), float(failure))

        elif match.startswith("contour:"):
            Z = re.search(r'''(z=(-?\d*\.?\d*))''', match).group(2)
            H = re.search(r'''(h=(-?\d*\.?\d*))''', match).group(2)
            r = re.search(r'''(r=(-?\d*\.?\d*))''', match).group(2)
            ap = re.search(r'''(ap=(-?\d*\.?\d*))''', match).group(2)
            clearance = re.search(r'''(clearance=(-?\d*\.?\d*))''',
                                  match).group(2)
            retraction = re.search(r'''(retraction=(-?\d*\.?\d*))''',
                                   match).group(2)
            gap = re.search(r'''(gap=(-?\d*\.?\d*))''', match).group(2)
            side = re.search(r'''(side=(left|right))''', match).group(2)
            f = re.search(r'''(f=(-?\d*))''', match).group(2)
            contour_match = re.finditer(r'''(line\(-?\d*\.?\d*,'''
                                        r'''-?\d*\.?\d*,'''
                                        r'''-?\d*\.?\d*\)|'''
                                        r'''circle\(-?\d*\.?\d*,'''
                                        r'''-?\d*\.?\d*,'''
                                        r'''-?\d*\.?\d*,'''
                                        r'''-?\d*\.?\d*,'''
                                        r'''-?\d*\.?\d*,'''
                                        r'''(cw|ccw)\))''',
                                        match, re.IGNORECASE)
            return self.contour(float(Z), float(H), float(r),
                                float(ap), float(clearance),
                                float(retraction), float(gap),
                                side, float(f), contour_match)

        else:
            return str

    def rect(self, length, width, height, feedrate, origin, pitch):
        result = "[[comment:rect]]\n"
        pitch_x = length * (pitch / (2 * length + 2 * width))
        pitch_y = width * (pitch / (2 * length + 2 * width))
        z = origin[2]
        result += "[[feed(" + self.atof(feedrate) + ")]]\n"
        x0 = origin[0]
        x1 = origin[0] - length * 0.5
        x2 = origin[0] + length * 0.5
        y0 = origin[1] - width * 0.5
        y1 = origin[1] + width * 0.5

        while z > origin[2] - height:
            result += "[[Line("
            result += self.atof(x0) + ","
            result += self.atof(y0) + ","
            result += self.atof(z) + ")]]\n"

            z -= pitch_x * 0.5
            if z < origin[2] - height:
                z = origin[2] - height

            result += "[[Line("
            result += self.atof(x1) + ","
            result += self.atof(y0) + ","
            result += self.atof(z) + ")]]\n"

            z -= pitch_y
            if z < origin[2] - height:
                z = origin[2] - height

            result += "[[Line("
            result += self.atof(x1) + ","
            result += self.atof(y1) + ","
            result += self.atof(z) + ")]]\n"

            z -= pitch_y
            if z < origin[2] - height:
                z = origin[2] - height

            result += "[[Line("
            result += self.atof(x2) + ","
            result += self.atof(y1) + ","
            result += self.atof(z) + ")]]\n"

            z -= pitch_y
            if z < origin[2] - height:
                z = origin[2] - height

            result += "[[Line("
            result += self.atof(x2) + ","
            result += self.atof(y0) + ","
            result += self.atof(z) + ")]]\n"

            z -= pitch_y
            if z < origin[2] - height:
                z = origin[2] - height

            result += "[[Line("
            result += self.atof(x0) + ","
            result += self.atof(y0) + ","
            result += self.atof(z) + ")]]\n"

        result += "[[Line("
        result += self.atof(x0) + ","
        result += self.atof(y0) + ","
        result += self.atof(z) + ")]]\n"
        result += "[[Line("
        result += self.atof(x1) + ","
        result += self.atof(y0) + ","
        result += self.atof(z) + ")]]\n"
        result += "[[Line("
        result += self.atof(x1) + ","
        result += self.atof(y1) + ","
        result += self.atof(z) + ")]]\n"
        result += "[[Line("
        result += self.atof(x2) + ","
        result += self.atof(y1) + ","
        result += self.atof(z) + ")]]\n"
        result += "[[Line("
        result += self.atof(x2) + ","
        result += self.atof(y0) + ","
        result += self.atof(z) + ")]]\n"
        result += "[[Line("
        result += self.atof(x0) + ","
        result += self.atof(y0) + ","
        result += self.atof(z) + ")]]\n"

        result += "[[comment:/rect]]\n"

        return result

    def bore(self, X, Y, Z, H, R, r, phi_1, pitch,
             clearance, retraction, feedrate):

        phi_1 = math.radians(phi_1)

        result = "[[comment:bore]]\n"

        x = X + (R - r) * \
            math.cos(phi_1)
        y = Y + (R - r) * \
            math.sin(phi_1)

        # feedrate
        result += "[[feed(" + self.atof(feedrate) + ")]]\n"

        # retraction plane
        result += "[[Rapid(" + self.atof(x) + ", "
        result += self.atof(y) + ", "
        result += self.atof(retraction) + ")]]\n"

        x = X + (R - r) * \
            math.cos(phi_1)
        y = Y + (R - r) * \
            math.sin(phi_1)
        result += "[[Rapid(" + self.atof(x) + ", "
        result += self.atof(y) + ", )]]\n"

        # gap
        z = Z + clearance

        result += "[[Rapid(,," + self.atof(z) + ")]]\n"

        # z start plane
        result += "[[Line(,," + self.atof(Z) + ")]]\n"

        # number of revolusions
        n = math.ceil(H / pitch)
        pitch = H / n

        for j in range(1, n + 1):
            result += "[[Circle(" + self.atof(x) + ", "
            result += self.atof(y) + ", "
            result += self.atof(Z-j*pitch) + ", "
            result += self.atof(X) + ", "
            result += self.atof(Y) + ", ccw)]]\n"

        result += "[[Circle(" + self.atof(x) + ", "
        result += self.atof(y) + ", "
        result += self.atof(Z-j*pitch) + ", "
        result += self.atof(X) + ", "
        result += self.atof(Y) + ", ccw)]]\n"

        # semicircle departure
        x2 = X + (R - r - 0.4 * (R - r)) * \
            math.cos(phi_1 + math.pi)
        y2 = Y + (R - r - 0.4 * (R - r)) * \
            math.sin(phi_1 + math.pi)
        result += "[[Circle(" + self.atof(x2) + ", "
        result += self.atof(y2) + ", "
        result += self.atof(Z-j*pitch) + ", "
        result += self.atof(x + 0.5 * (x2 - x)) + ", "
        result += self.atof(y + 0.5 * (y2 - y)) + ", ccw)]]\n"

        # retraction plane
        result += "[[Rapid(" + ", , "
        result += self.atof(retraction) + ")]]\n"

        result += "[[comment:/bore]]\n"
        return result

    def polybore(self, X, Y, Z, H, R, r, phi_1, pitch,
                 clearance, retraction, feedrate, failure):

        phi_1 = math.radians(phi_1)

        result = "[[comment:polybore]]\n"

        x = X + (R - r) * \
            math.cos(phi_1)
        y = Y + (R - r) * \
            math.sin(phi_1)

        # feedrate
        result += "[[feed(" + self.atof(feedrate) + ")]]\n"

        # retraction plane
        result += "[[Rapid(" + self.atof(x) + ", "
        result += self.atof(y) + ", "
        result += self.atof(retraction) + ")]]\n"

        x = X + (R - r) * \
            math.cos(phi_1)
        y = Y + (R - r) * \
            math.sin(phi_1)
        result += "[[Rapid(" + self.atof(x) + ", "
        result += self.atof(y) + ", )]]\n"

        # gap
        z = Z + clearance

        result += "[[Rapid(,," + self.atof(z) + ")]]\n"

        # z start plane
        z = Z
        result += "[[Line(,," + self.atof(z) + ")]]\n"

        n = math.ceil(H / pitch)
        pitch = H / n

        phi_max = 2 * math.acos(-failure/(R-r)+1)
        # number of steps per revolusion
        m = math.ceil(2 * math.pi / phi_max)
        phi = 2 * math.pi / m
        # pitch per increment
        dpitch = pitch / m

        for j in range(1, n + 1):
            for i in range(1, m+1):
                x = X + (R-r) * math.cos(phi_1 + phi*i)
                y = Y + (R-r) * math.sin(phi_1 + phi*i)
                z = z - dpitch
                result += "[[Line(" + self.atof(x) + ", "
                result += self.atof(y) + ", "
                result += self.atof(z) + ")]]\n"

        for i in range(1, m+1):
            x = X + (R-r) * math.cos(phi*i)
            y = Y + (R-r) * math.sin(phi*i)
            result += "[[Line(" + self.atof(x) + ", "
            result += self.atof(y) + ", )]]\n"

        # semicircle departure
        x = X + (R - r) * \
            math.cos(phi_1)
        y = Y + (R - r) * \
            math.sin(phi_1)
        x2 = X + (R - r - 0.4 * (R - r)) * \
             math.cos(phi_1 + math.pi)
        y2 = Y + (R - r - 0.4 * (R - r)) * \
             math.sin(phi_1 + math.pi)
        X2 = x + 0.5 * (x2 - x)
        Y2 = y + 0.5 * (y2 - y)
        for i in range(1, math.ceil(0.5 * (m+1))):
            x = X2 + (R-r - 0.2*(R-r)) * math.cos(phi*i)
            y = Y2 + (R-r - 0.2*(R-r)) * math.sin(phi*i)
            result += "[[Line(" + self.atof(x) + ", "
            result += self.atof(y) + ", )]]\n"

        # retraction plane
        result += "[[Rapid(" + ", , "
        result += self.atof(retraction) + ")]]\n"

        result += "[[comment:/polybore]]\n"
        return result

    def cylinder(self, X, Y, Z, H, R, r, phi_1, pitch,
                 clearance, retraction, gap, feedrate):

        phi_1 = math.radians(phi_1)

        result = "[[comment:cylinder]]\n"

        # feedrate
        result += "[[feed(" + self.atof(feedrate) + ")]]\n"

        x = X + (R + r) * \
            math.cos(phi_1) + \
            gap * math.cos(phi_1 - math.pi * 0.5)
        y = Y + (R + r) * \
            math.sin(phi_1) + \
            gap * math.sin(phi_1 - math.pi * 0.5)

        # retraction plane
        result += "[[Rapid(" + self.atof(x) + ", "
        result += self.atof(y) + ", "
        result += self.atof(retraction) + ")]]\n"

        # gap
        z = Z + clearance

        result += "[[Rapid(,," + self.atof(z) + ")]]\n"

        # z start plane
        result += "[[Line(,," + self.atof(Z) + ")]]\n"

        x = X + (R + r) * \
            math.cos(phi_1)
        y = Y + (R + r) * \
            math.sin(phi_1)
        result += "[[Line(" + self.atof(x) + ", "
        result += self.atof(y) + ", )]]\n"

        n = math.ceil(H / pitch)
        pitch = H / n

        for j in range(1, n + 1):
            result += "[[Circle(" + self.atof(x) + ", "
            result += self.atof(y) + ", "
            result += self.atof(Z-j*pitch) + ", "
            result += self.atof(X) + ", "
            result += self.atof(Y) + ", ccw)]]\n"

        result += "[[Circle(" + self.atof(x) + ", "
        result += self.atof(y) + ", "
        result += self.atof(Z-j*pitch) + ", "
        result += self.atof(X) + ", "
        result += self.atof(Y) + ", ccw)]]\n"

        x = X + (R + r) * \
            math.cos(phi_1) + \
            gap * math.cos(phi_1 + math.pi * 0.5)
        y = Y + (R + r) * \
            math.sin(phi_1) + \
            gap * math.sin(phi_1 + math.pi * 0.5)

        result += "[[Line(" + self.atof(x) + ", "
        result += self.atof(y) + ", )]]\n"

        result += "[[comment:/cylinder]]\n"
        return result

    def sphere(self, X, Y, Z, R, r, phi_1, phi_2, theta_1, theta_2,
               clearance, retraction, gap, feedrate, step):

        phi_1 = math.radians(phi_1)
        phi_2 = math.radians(phi_2)
        theta_1 = math.radians(theta_1)
        theta_2 = math.radians(theta_2)

        result = "[[comment:sphere]]\n"
        x = X + (R + r + gap) * math.sin(theta_1) * math.cos(phi_1)
        y = Y + (R + r + gap) * math.sin(theta_1) * math.sin(phi_1)
        z = Z + (R + r) * math.cos(theta_1) - r

        # feedrate
        result += "[[feed(" + self.atof(feedrate) + ")]]\n"

        # retraction plane
        result += "[[Rapid(" + self.atof(x) + ", "
        result += self.atof(y) + ", "
        result += self.atof(retraction) + ")]]\n"

        # calculate number of steps in theta direction
        n = math.ceil(abs(theta_1-theta_2)/step)
        step_theta = abs(theta_1-theta_2)/n

        # calculate number of steps in phi direction
        m = math.ceil(abs(phi_1-phi_2)/step)
        step_phi = abs(phi_1-phi_2)/m

        for j in range(0, m+1):
            # gap
            x = (X + (R + r) * math.sin(theta_1) *
                 math.cos(phi_1 + j * step_phi)) + \
                 gap * math.cos(phi_1 + j * step_phi)
            y = Y + (R + r) * math.sin(theta_1) * \
                math.sin(phi_1 + j * step_phi) + \
                gap * math.sin(phi_1 + j * step_phi)
            z = Z + (R + r) * math.cos(theta_2) - r

            result += "[[Rapid(" + self.atof(x) + ", "
            result += self.atof(y) + ", )]]\n"

            # z clearance plane
            z = Z + (R + r) * math.cos(theta_1) - r + clearance
            result += "[[Rapid(,," + self.atof(z) + ")]]\n"
            # z start plane
            z = Z + (R + r) * math.cos(theta_1) - r
            result += "[[Line(,," + self.atof(z) + ")]]\n"

            for i in range(0, n+1):
                x = X + (R + r) * math.sin(theta_1-i*step_theta) * \
                    math.cos(phi_1+j*step_phi)
                y = Y + (R + r) * math.sin(theta_1-i*step_theta) * \
                    math.sin(phi_1+j*step_phi)
                z = Z + (R + r) * math.cos(theta_1-i*step_theta) - r
                result += "[[Line(" + self.atof(x) + ", "
                result += self.atof(y) + ", "
                result += self.atof(z) + ")]]\n"

            # gap
            x = X + (R + r) * math.sin(theta_1-i*step_theta) * \
                math.cos(phi_1 + j * step_phi) - \
                gap * math.cos(phi_1 + j * step_phi)
            y = Y + (R + r) * math.sin(theta_1-i*step_theta) * \
                math.sin(phi_1 + j * step_phi) - \
                gap * math.sin(phi_1 + j * step_phi)
            result += "[[Line(" + self.atof(x) + ", "
            result += self.atof(y) + ", )]]\n"

            # z clearance plane
            # z = (R + r) * math.cos(theta_2) - r + clearance
            result += "[[Rapid(,," + self.atof(retraction) + ")]]\n"

        result += "[[comment:/sphere]]\n"

        return result

    def contour(self, Z, H, r, ap, clearance, retraction,
                gap, side, feedrate, contour):

        # list with points of contour
        points = []

        result = "[[comment:contour]]\n"

        # feedrate
        result += "[[feed(" + self.atof(feedrate) + ")]]\n"

        nextcmd = contour.__next__().group(1)
        line_start = re.search(r'''line\((-?\d*\.?\d*),'''
                               r'''(-?\d*\.?\d*),(-?\d*\.?\d*)\)''',
                               nextcmd, re.IGNORECASE)
        nextcmd = contour.__next__().group(1)
        line_end = re.search(r'''line\((-?\d*\.?\d*),'''
                             r'''(-?\d*\.?\d*),(-?\d*\.?\d*)\)''',
                             nextcmd, re.IGNORECASE)

        x0 = float(line_start.group(1))
        y0 = float(line_start.group(2))
        x1 = float(line_end.group(1))
        y1 = float(line_end.group(2))

        # first vertex
        # direction vector
        if side == 'right':
            x10 = x1 - x0
            y10 = y1 - y0
        elif side == 'left':
            x10 = x0 - x1
            y10 = y0 - y1
        # rotate 90deg
        x10n = y10
        y10n = -x10
        # normalize
        x0T = x0 + (x10n * r) / (math.sqrt(x10n**2 + y10n**2))
        y0T = y0 + (y10n * r) / (math.sqrt(x10n**2 + y10n**2))
        x1T = x1 + (x10n * r) / (math.sqrt(x10n**2 + y10n**2))
        y1T = y1 + (y10n * r) / (math.sqrt(x10n**2 + y10n**2))

        # start point
        # direction vector
        x10T = x0T - x1T
        y10T = y0T - y1T
        # normalize
        x10Tn = x10T / math.sqrt(x10T**2 + y10T**2)
        y10Tn = y10T / math.sqrt(x10T**2 + y10T**2)
        # scale distance
        x_start = x0T + (x10Tn * (r+gap))
        y_start = y0T + (y10Tn * (r+gap))

        points.append([0, x_start, y_start])

        last_type = 0

        for m in contour:
            # read next segment
            segment = re.search(r'''line\((-?\d*\.?\d*),'''
                                r'''(-?\d*\.?\d*),(-?\d*\.?\d*)\)''',
                                m.group(1), re.IGNORECASE)
            type_ = 0   # line
            # if elements isn't line, read cyrcle
            if segment is None:
                segment = re.search(r'''circle\((-?\d*\.?\d*),'''
                                    r'''(-?\d*\.?\d*),'''
                                    r'''(-?\d*\.?\d*),'''
                                    r'''(-?\d*\.?\d*),'''
                                    r'''(-?\d*\.?\d*),(cw|ccw)\)''',
                                    m.group(1), re.IGNORECASE)
                # circle centre
                cx = float(segment.group(4))
                cy = float(segment.group(5))
                dir_ = segment.group(6)
                type_ = 1   # circle
                if math.sqrt((cx-x1)**2+(cy-y1)**2) < r:
                    x0 = x1
                    y0 = y1
                    x1 = float(segment.group(1))
                    y1 = float(segment.group(2))
                    last_type = 0
                    continue

            x2 = float(segment.group(1))
            y2 = float(segment.group(2))

            # get 1T_2 and 2T
            # if segment is line
            if type_ == 0:
                # direction vector
                if side == "right":
                    x12 = x2 - x1
                    y12 = y2 - y1
                elif side == "left":
                    x12 = x1 - x2
                    y12 = y1 - y2
                # rotate 90deg
                x12n = y12
                y12n = -x12
                # normalize
                x1T_2 = x1 + ((x12n * r) / math.sqrt(x12n**2 + y12n**2))
                y1T_2 = y1 + ((y12n * r) / math.sqrt(x12n**2 + y12n**2))
                x2T = x2 + ((x12n * r) / math.sqrt(x12n**2 + y12n**2))
                y2T = y2 + ((y12n * r) / math.sqrt(x12n**2 + y12n**2))

            # if segment is circle
            if type_ == 1:
                if (side == 'right' and dir_ == 'cw') or \
                   (side == 'left' and dir_ == 'ccw'):
                    # direction 1 to centre
                    x1c = cx - x1
                    y1c = cy - y1
                    # direction 2 to centre
                    x2c = cx - x2
                    y2c = cy - y2
                else:
                    # direction 1 to centre
                    x1c = x1 - cx
                    y1c = y1 - cy
                    # direction 2 to centre
                    x2c = x2 - cx
                    y2c = y2 - cy
                # normalize
                x1T_2 = x1 + ((x1c * r) / math.sqrt(x1c**2 + y1c**2))
                y1T_2 = y1 + ((y1c * r) / math.sqrt(x1c**2 + y1c**2))
                x2T = x2 + ((x2c * r) / math.sqrt(x2c**2 + y2c**2))
                y2T = y2 + ((y2c * r) / math.sqrt(x2c**2 + y2c**2))
                # get x1T_2T by rotating 2c
                x1T_2T = x1T_2 + y1c
                y1T_2T = y1T_2 - x1c
                # get x2TT by rotating 2c
                x2TT = x2T + y2c
                y2TT = y2T - x2c

            # / get 1T_2 and 2T

            # find intersection
            # if actual and last segment are line
            if type_ == 0 and last_type == 0:
                Sx, Sy = intersect(x0T, y0T, x1T, y1T,
                                   x2T, y2T, x1T_2, y1T_2)

            # if actual segment ist line and last was circle
            if type_ == 0 and last_type == 1:
                if abs(x1T-x1T_2)<0.002 and abs(y1T-y1T_2)<0.002:
                    Sx = x1T
                    Sy = y1T
                else:
                    Sx, Sy = intersect(x1T, y1T, x1TT, y1TT,
                                       x1T_2, y1T_2, x2T, y2T)

            # if actual segment ist circle
            if type_ == 1:
                if abs(x1T-x1T_2)<0.002 and abs(y1T-y1T_2)<0.002:
                    Sx = x1T
                    Sy = y1T
                else:
                    Sx, Sy = intersect(x0T, y0T, x1T, y1T,
                                       x1T_2, y1T_2, x1T_2T, y1T_2T)

            # write segment
            # if last_type == 0:
            if type_ == 0:
                points.append([0, Sx, Sy])
            if type_ == 1:
                if last_type == 0:
                    points.append([0, Sx, Sy])
                if abs(Sx-x1T_2)>0.002 and abs(Sy-y1T_2)>0.002:
                    points.append([0, x1T_2, y1T_2])
                points.append([1, x2T, y2T, cx, cy, dir_])

            # copy points for next itteration
            if type_ == 0:
                x0T = Sx
                y0T = Sy
            if type_ == 1:
                x0T = x1T_2
                y0T = y1T_2
                x1TT = x2TT
                y1TT = y2TT
            x0 = x1
            y0 = y1
            x1 = x2
            y1 = y2
            x1T = x2T
            y1T = y2T

            last_type = type_
        # / for m in contour

        # end point
        # direction vector
        x01T = x1T - x0T
        y01T = y1T - y0T
        # normalize
        x01Tn = x01T / math.sqrt(x01T**2 + y01T**2)
        y01Tn = y01T / math.sqrt(x01T**2 + y01T**2)
        # scale distance
        x_end = x1T + (x01Tn * gap)
        y_end = y1T + (y01Tn * gap)

        points.append([0, x_end, y_end])

        n = math.ceil(H / ap)
        ap = H / n

        z = Z
        for i in range(0, n):
            z = z - ap
            # start
            # retraction plane
            result += "[[Rapid(" + self.atof(points[0][1]) + ", "
            result += self.atof(points[0][2]) + ", "
            result += self.atof(retraction) + ")]]\n"

            # gap
            result += "[[Rapid(,," + self.atof(z + clearance) + ")]]\n"

            # z
            result += "[[Line(,," + self.atof(z) + ")]]\n"

            # contour
            for p in points[1:]:
                if p[0] == 0:
                    result += "[[Line(" + self.atof(p[1]) + ", "
                    result += self.atof(p[2]) + ", )]]\n"
                elif p[0] == 1:
                    result += "[[Circle(" + self.atof(p[1]) + ", "
                    result += self.atof(p[2]) + ", ,"
                    result += self.atof(p[3]) + ", "
                    result += self.atof(p[4]) + ", "
                    result += p[5] + ")]]\n"

            # end
            # clearance
            result += "[[Line(,," + self.atof(z + clearance) + ")]]\n"
            # retraction plane
            result += "[[Rapid(,," + self.atof(retraction) + ")]]\n"

        result += "[[comment:/contour]]\n"

        return result

    def atof(self, num):
        return self.digits.format(num).rstrip('0').rstrip('.')
