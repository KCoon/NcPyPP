import re


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
            f = re.search(r'''(f\s*=\s*(-?\d*\.?\d*))''', str).group(2)
            return self.rect(float(l), float(w), float(h),
                             float(f),
                             [float(x), float(y), float(z)],
                             float(p))
        else:
            return str

    def rect(self, length, width, height, feedrate, origin, pitch):
        result = ""
        pitch_x = length * (pitch / (2 * length + 2 * width))
        pitch_y = width * (pitch / (2 * length + 2 * width))
        z = origin[2]
        result += "feed(" + self.atof(feedrate) + ")\n"
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
        return result

    def atof(self, num):
        return self.digits.format(num).rstrip('0').rstrip('.')
