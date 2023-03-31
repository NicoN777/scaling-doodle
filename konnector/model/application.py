from konnector.model.owner import Owner
from konnector.model.base import Base


class ApplicationBase(Base):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class Application(ApplicationBase):
    __slots__ = ['id', 'name', 'password', 'owner']

    def __init__(self, id: int, name: str, password: str, owner: Owner):
        super().__init__(id, name)
        self.password = password
        self.owner = owner

    def __repr__(self):
        return Base.__repr__(self)

    @classmethod
    def from_keys(cls, **kwargs):
        if len(cls.__slots__) != len(kwargs):
            raise AttributeError(f'No, {len(cls.__slots__)} values are required')

        for key in kwargs.keys():
            if key not in cls.__slots__:
                raise AttributeError(f'No attribute {key} in {cls.__name__}')

        return Application(*kwargs.values())
