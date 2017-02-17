import re


class Language:

    def __init__(self):
        self.id = 'iso'

    def remove_numbers(self, str):
        match = re.search(r'''^(\d*\s*)(.*)''', str)
        return match.group(2) + '\n'

    def expand(self, str):
        match = re.search(r'''^\[\[(.*)\]\]''', str)
        if match is None:
            return str

        match = match.group(1).lower()
        if match == "lorem":
            return self.lorem()

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


class Instance (Language):
        pass

