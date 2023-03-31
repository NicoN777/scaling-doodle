class Base:
    def __repr__(self):
        attrs = '='.join([f'{_},{self.__getattribute__(_)}' for _ in self.__slots__])
        return f'{self.__class__.__name__}({attrs})'

    def serde(self):
        return {_: self.__getattribute__(_) for _ in self.__slots__}
