from ncpypp.languages.iso.iso import Language

class Dialect(Language):

    def __init__(self):
        self.id = 'mitsubishi'

    def lorem(self):
        return "lorem\n"

class Instance (Dialect):
        pass
