import re
import math


class Pypplang:

    def __init__(self):
        self.id = 'pypplang'
        self.digits = "{0:.3f}"

    def expand(self, str):
        match = re.search(r'''^\[\[(.*)\]\]''', str)
        if match is None:
            return str
        match = match.group(1).lower()
        if match.startswith("rect:"):
            x = re.search(r'''(x\s*=\s*(-?\d*\.?\d*))''', str).group(2)
            y = re.search(r'''(y\s*=\s*(-?\d*\.?\d*))''', str).group(2)
            z = re.search(r'''(z\s*=\s*(-?\d*\.?\d*))''', str).group(2)
            l = re.search(r'''(l\s*=\s*(-?\d*\.?\d*))''', str).group(2)
            w = re.search(r'''(w\s*=\s*(-?\d*\.?\d*))''', str).group(2)
            h = re.search(r'''(h\s*=\s*(-?\d*\.?\d*))''', str).group(2)
            p = re.search(r'''(p\s*=\s*(-?\d*\.?\d*))''', str).group(2)
            f = re.search(r'''(f\s*=\s*(-?\d*))''', str).group(2)
            return self.rect(float(l), float(w), float(h),
                             float(f),
                             [float(x), float(y), float(z)],
                             float(p))
        elif match.startswith("sphere:"):
            X = re.search(r'''(x\s*=\s*(-?\d*\.?\d*))''', match).group(2)
            Y = re.search(r'''(y\s*=\s*(-?\d*\.?\d*))''', match).group(2)
            Z = re.search(r'''(z\s*=\s*(-?\d*\.?\d*))''', match).group(2)
            R = re.search(r'''(r_1\s*=\s*(-?\d*\.?\d*))''', match).group(2)
            r = re.search(r'''(r_2\s*=\s*(-?\d*\.?\d*))''', match).group(2)
            phi_1 = re.search(r'''(phi_1\s*=\s*(-?\d*\.?\d*))''',
                              match).group(2)
            phi_2 = re.search(r'''(phi_2\s*=\s*(-?\d*\.?\d*))''',
                              match).group(2)
            theta_1 = re.search(r'''(theta_1\s*=\s*(-?\d*\.?\d*))''',
                                match).group(2)
            theta_2 = re.search(r'''(theta_2\s*=\s*(-?\d*\.?\d*))''',
                                match).group(2)
            clearance = re.search(r'''(clearance\s*=\s*(-?\d*\.?\d*))''',
                                  match).group(2)
            retraction = re.search(r'''(retraction\s*=\s*(-?\d*\.?\d*))''',
                                   match).group(2)
            gap = re.search(r'''(gap\s*=\s*(-?\d*\.?\d*))''', match).group(2)
            f = re.search(r'''(f\s*=\s*(-?\d*))''', match).group(2)
            step = re.search(r'''(step\s*=\s*(-?\d*\.?\d*))''',
                             match).group(2)
            return self.sphere(float(X), float(Y), float(Z),
                               float(R), float(r), float(phi_1),
                               float(phi_2), float(theta_1), float(theta_2),
                               float(clearance), float(retraction),
                               float(gap), float(f), float(step))
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
            x = (X + (R + r) * math.sin(theta_1) * \
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

    def atof(self, num):
        return self.digits.format(num).rstrip('0').rstrip('.')
