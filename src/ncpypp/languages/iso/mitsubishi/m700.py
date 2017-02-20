from ncpypp.languages.iso.mitsubishi.mitsubishi import Dialect


class Instance(Dialect):

    def __init__(self):
        super().__init__()
        self.id_ = 'fumg'

    def lorem(self):
        return "lorem ipsum\n"
