from konnector.model.owner import Owner
from konnector.model.base import Base


class ApplicationBase(Base):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class Application(ApplicationBase):
    REQUIRED = ['id', 'name', 'password', 'owner']

    def __init__(self, id: int, name: str, password: str, owner: Owner):
        super().__init__(id, name)
        self.password = password
        self.owner = owner

    def __repr__(self):
        return Base.__repr__(self)

