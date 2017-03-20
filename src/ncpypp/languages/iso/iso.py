''' @todo   adding doctstring '''
import re


class Language(object):

    def __init__(self):
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
        match = re.search(r'''G1(\s*[XYZ]\d*\.?\d*\s*){1,3}''',
                          str, re.IGNORECASE)
        if match is not None:
            x = re.search(r'''X(\d*\.?\d*)''', str, re.IGNORECASE)
            if x is not None:
                x = x.group(1)
            else:
                x = ""

            y = re.search(r'''Y(\d*\.?\d*)''', str, re.IGNORECASE)
            if y is not None:
                y = y.group(1)
            else:
                y = ""

            z = re.search(r'''Z(\d*\.?\d*)''', str, re.IGNORECASE)
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
            self.feed = match_feed.group(2)
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
            if y is not "":
                self.y = float(y)
            if z is not "":
                self.z = float(z)
            return self.rapid(match_rapid.group(1), match_rapid.group(2),
                              match_rapid.group(3))
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
            if y is not "":
                self.y = float(y)
            if z is not "":
                self.z = float(z)
            return self.line(match_line.group(1), match_line.group(2),
                             match_line.group(3))

        # polar movement G2/G3
        match_circle = re.search(r'''circle\((-?\d*\.?\d*)\s*,\s*'''
                                 r'''(-?\d*\.?\d*)\s*,\s*(-?\d*\.?\d*)\s*,\s*'''
                                 r'''(-?\d*\.?\d*)\s*,\s*(-?\d*\.?\d*)\s*,\s*'''
                                 r'''((ccw)|(cw))\)''',
                                 str, re.IGNORECASE)
        if match_circle is not None:
            return self.circle(float(match_circle.group(1)),
                               float(match_circle.group(2)),
                               float(match_circle.group(3)),
                               float(match_circle.group(4)),
                               float(match_circle.group(5)),
                               match_circle.group(6))

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
            feed = " F" + str(self.feed)
            self.write_feed = False

        result = "G1"
        if x:
            result += " X" + str(x)
        if y:
            result += " Y" + str(y)
        if z:
            result += " Z" + str(z)
        result += feed + "\n"
        return result

    def rapid(self, x, y, z):
        result = "G0"
        if x:
            result += " X" + str(x)
        if y:
            result += " Y" + str(y)
        if z:
            result += " Z" + str(z)
        result += "\n"
        return result

    def circle(self, x, y, z, i, j, direction):
        result = ""
        if direction == "cw":
            result = "G2"
        elif direction == "ccw":
            result = "G3"
        result += " X" + str(x)
        result += " Y" + str(y)
        result += " Z" + str(z)
        result += " I" + str(i-self.x)
        result += " J" + str(j-self.y) + "\n"
        return result


class Instance(Language):
    pass
