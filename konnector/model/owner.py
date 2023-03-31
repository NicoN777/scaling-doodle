from konnector.model.base import Base


class PersonBase(Base):

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Person(PersonBase):
    __slots__ = ['first_name', 'last_name', 'email', 'phone_no']

    def __init__(self, first_name: str, last_name: str, email: str, phone_no):
        super().__init__(first_name, last_name)
        self.email = email
        self.phone_no = phone_no

    @classmethod
    def from_keys(cls, **kwargs):
        if len(cls.__slots__) != len(kwargs):
            raise AttributeError(f'No, {len(cls.__slots__)} values are required')

        for key in kwargs.keys():
            if key not in cls.__slots__:
                raise AttributeError(f'No attribute {key} in {cls.__name__}')

        return Person(*kwargs.values())


class Owner(Person):
    __slots__ = ['id', 'first_name', 'last_name', 'email', 'phone_no']

    def __init__(self, id: int, first_name: str, last_name: str, email: str, phone_no):
        super().__init__(first_name, last_name, email, phone_no)
        self.id = id

    @classmethod
    def from_keys(cls, **kwargs):
        if len(cls.__slots__) != len(kwargs):
            raise AttributeError(f'No, {len(cls.__slots__)} values are required')

        for key in kwargs.keys():
            if key not in cls.__slots__:
                raise AttributeError(f'No attribute {key} in {cls.__name__}')

        return Owner(*kwargs.values())
