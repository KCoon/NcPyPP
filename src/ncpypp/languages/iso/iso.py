''' @todo   adding doctstring '''
import re


class Language(object):

    def __init__(self):
        self.id_ = 'iso'
        self.write_feed = False
        self.feed = 0

    def remove_numbers(self, str):
        match = re.search(r'''^(\d*\s*)(.*)''', str)
        return match.group(2) + '\n'

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
        match_rapid = re.search(r'rapid\((-?\d*\.?\d*)\s*,\s*'
                                r'(-?\d*\.?\d*)\s*,\s*(-?\d*\.?\d*)\)''',
                                str, re.IGNORECASE)
        if match_rapid is not None:
            return self.rapid(match_rapid.group(1), match_rapid.group(2),
                             match_rapid.group(3))
        # linear movement G1
        match_line = re.search(r'line\((-?\d*\.?\d*)\s*,\s*'
                               r'(-?\d*\.?\d*)\s*,\s*(-?\d*\.?\d*)\)''',
                               str, re.IGNORECASE)
        if match_line is not None:
            return self.line(match_line.group(1), match_line.group(2),
                             match_line.group(3))

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

class Instance(Language):
    pass
