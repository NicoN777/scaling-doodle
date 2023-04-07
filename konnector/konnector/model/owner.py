from datetime import datetime
from konnector.model.base import Base


class PersonBase(Base):

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class User(PersonBase):
    JSON_IGNORE = ['password']
    REQUIRED = ['first_name', 'last_name', 'email']
    OPTIONAL = ['phone_no']

    def __init__(self, first_name: str, last_name: str, email: str, password: str, phone_no=None):
        super().__init__(first_name, last_name)
        self.email = email
        self.password = password
        self.phone_no = phone_no


class Owner(User):
    REQUIRED = ['id', 'first_name', 'last_name', 'email']
    OPTIONAL = ['phone_no', 'create_ts', 'update_ts']

    def __init__(self, id: int = ...,
                 first_name: str = ...,
                 last_name: str = ...,
                 email: str = ...,
                 password: str = ...,
                 phone_no: str = '',
                 create_ts: datetime = '',
                 update_ts: datetime = ''):
        super().__init__(first_name, last_name, email, password, phone_no)
        self.id = id
        self.create_ts = create_ts
        self.update_ts = update_ts
