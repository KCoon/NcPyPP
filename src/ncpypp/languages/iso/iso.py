''' @todo   adding doctstring '''
import re


class Language(object):

    def __init__(self):
        self.digits = "{0:.3f}"
        self.id_ = 'iso'
        self.write_feed = False
        self.feed = 0
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

    def remove_numbers(self, str):
        match = re.search(r'''^(\d*\s*)(.*)''', str)
        return match.group(2) + '\n'

    def to_pypplang(self, str):
        match = re.search(r'''G1(\s*[XYZ]-?\d*\.?\d*\s*){1,3}''',
                          str, re.IGNORECASE)
        if match is not None:
            x = re.search(r'''X(-?\d*\.?\d*)''', str, re.IGNORECASE)
            if x is not None:
                x = x.group(1)
            else:
                x = ""

            y = re.search(r'''Y(-?\d*\.?\d*)''', str, re.IGNORECASE)
            if y is not None:
                y = y.group(1)
            else:
                y = ""

            z = re.search(r'''Z(-?\d*\.?\d*)''', str, re.IGNORECASE)
            if z is not None:
                z = z.group(1)
            else:
                z = ""

            result = "[[Line(" + x + ", " + y + ", " + z + ")]]\n"
            return result

        return str

    def expand(self, str):
        match = re.search(r'''^\[\[(.*)\]\]''', str)
        if match is None:
            return str + "\n"

        # dummy lorem ipsum
        match_lorem = re.search(r'''^\[\[lorem\]\]''', str, re.IGNORECASE)
        if match_lorem is not None:
            return self.lorem()

        # comment
        match_comment = re.search(r'''^\[\[comment:(.*)\]\]''',
                                  str, re.IGNORECASE)
        if match_comment is not None:
            return "(" + match_comment.group(1) + ")\n"

        # feedrate
        match_feed = re.search(r'''^\[\[(feed\((\d*)\))\]\]''',
                               str, re.IGNORECASE)
        if match_feed is not None:
            self.feed = float(match_feed.group(2))
            self.write_feed = True
            return ""

        # rapid movement G0
        match_rapid = re.search(r'''rapid\((-?\d*\.?\d*)\s*,\s*'''
                                r'''(-?\d*\.?\d*)\s*,\s*(-?\d*\.?\d*)\)''',
                                str, re.IGNORECASE)
        if match_rapid is not None:
            x = match_rapid.group(1)
            y = match_rapid.group(2)
            z = match_rapid.group(3)
            if x is not "":
                self.x = float(x)
                x = float(x)
            else:
                x = None
            if y is not "":
                self.y = float(y)
                y = float(y)
            else:
                y = None
            if z is not "":
                self.z = float(z)
                z = float(z)
            else:
                z = None
            return self.rapid(x, y, z)
        # linear movement G1
        match_line = re.search(r'''line\((-?\d*\.?\d*)\s*,\s*'''
                               r'''(-?\d*\.?\d*)\s*,\s*(-?\d*\.?\d*)\)''',
                               str, re.IGNORECASE)
        if match_line is not None:
            x = match_line.group(1)
            y = match_line.group(2)
            z = match_line.group(3)
            if x is not "":
                self.x = float(x)
                x = float(x)
            else:
                x = None
            if y is not "":
                self.y = float(y)
                y = float(y)
            else:
                y = None
            if z is not "":
                self.z = float(z)
                z = float(z)
            else:
                z = None
            return self.line(x, y, z)

        # polar movement G2/G3
        match_circle = re.search(r'''circle\((-?\d*\.?\d*)\s*,\s*'''
                                 r'''(-?\d*\.?\d*)\s*,\s*(-?\d*\.?\d*)\s*,\s*'''
                                 r'''(-?\d*\.?\d*)\s*,\s*(-?\d*\.?\d*)\s*,\s*'''
                                 r'''((ccw)|(cw))\)''',
                                 str, re.IGNORECASE)
        if match_circle is not None:
            x = match_circle.group(1)
            y = match_circle.group(2)
            z = match_circle.group(3)
            X = match_circle.group(4)
            Y = match_circle.group(5)
            if x is not "":
                x = float(x)
            else:
                x = None
            if y is not "":
                y = float(y)
            else:
                y = None
            if z is not "":
                z = float(z)
            else:
                z = None

            return self.circle(x, y, z,
                               float(X),
                               float(Y),
                               match_circle.group(6))
            if x is not None:
                self.x = x
            if y is not None:
                self.y = y
            if z is not None:
                self.z = z

        return str

    def lorem(self):
        return """Lorem ipsum dolor sit amet, consectetur
adipisicing elit, sed do eiusmod tempor incididunt ut
labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex
ea commodo consequat. Duis aute irure dolor in reprehenderit
in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
officia deserunt mollit anim id est laborum.""" + '\n'

    def line(self, x, y, z):
        feed = ""
        if self.write_feed:
            feed = " F" + self.atof(self.feed)
            self.write_feed = False

        result = "G1"
        if x is not None:
            result += " X" + self.atof(x)
        if y is not None:
            result += " Y" + self.atof(y)
        if z is not None:
            result += " Z" + self.atof(z)
        result += feed + "\n"
        return result

    def rapid(self, x, y, z):
        result = "G0"
        if x is not None:
            result += " X" + self.atof(x)
        if y is not None:
            result += " Y" + self.atof(y)
        if z is not None:
            result += " Z" + self.atof(z)
        result += "\n"
        return result

    def circle(self, x, y, z, i, j, direction):
        result = ""
        if direction == "cw":
            result = "G2"
        elif direction == "ccw":
            result = "G3"
        if x is not None:
            result += " X" + self.atof(x)
        if y is not None:
            result += " Y" + self.atof(y)
        if z is not None:
            result += " Z" + self.atof(z)
        result += " I" + self.atof(i-self.x)
        result += " J" + self.atof(j-self.y) + "\n"
        return result

    def atof(self, num):
        return self.digits.format(num).rstrip('0').rstrip('.')


class Instance(Language):
    pass
