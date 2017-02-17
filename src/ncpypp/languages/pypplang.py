import re


class Pypplang:

    def __init__(self):
        self.id = 'pypplang'

    def expand(self, str):
        match = re.search(r'''^\[\[(.*)\]\]''', str)
        if match is None:
            return str

        match = match.group(1).lower()
        if match.startswith("rect:"):
            x = re.search(r'''(x\s*=\s*(\d*))''', str).group(1)
            y = re.search(r'''(y\s*=\s*(\d*))''', str).group(1)
            l = re.search(r'''(l\s*=\s*(\d*))''', str).group(1)
            h = re.search(r'''(h\s*=\s*(\d*))''', str).group(1)
            return self.rect(x, y, l, h)

        return str

    def rect(self, x, y, l, h,):
        return "[[a rectangle]]"
