from ncpypp.languages.iso.iso import Language


class Dialect(Language):

    def __init__(self):
        super().__init__()
        self.id_ = 'mitsubishi'

    def lorem(self):
        return "lorem\n"


class Instance(Dialect):
    pass
