
class Path:
    def __init__(self, path=None, macro='%FOLDERS_STORAGE%'):
        self.linux = path if path else ''
        self.win = path if path else ''
        self.osx = path if path else ''

        self.macro = macro

    def get_object(self):
        attrs = {
            'linux': self.linux,
            'win': self.win,
            'osx': self.osx
        }

        if self.macro is not None:
            attrs['macro'] = self.macro

        return attrs
