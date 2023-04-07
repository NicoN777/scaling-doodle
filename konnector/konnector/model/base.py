import datetime


class Base:
    JSON_IGNORE = []
    REQUIRED = []
    OPTIONAL = []

    def __repr__(self):
        attrs = ','.join([f'{_}={self.__getattribute__(_)}' for _ in self.REQUIRED + self.OPTIONAL + self.JSON_IGNORE])
        return f'{self.__class__.__name__}({attrs})'

    def deserialize(self):
        data = {}
        for attribute in self.REQUIRED + self.OPTIONAL + self.JSON_IGNORE:
            value = self.__getattribute__(attribute)
            instance = type(self.__getattribute__(attribute))
            data[attribute] = value
            if isinstance(value, datetime.datetime):
                data[attribute] = f'{value:%m/%d/%Y %H:%M:%S}'
        return data

    def serialize(self):
        data = {}
        for attribute in self.REQUIRED + self.OPTIONAL:
            value = self.__getattribute__(attribute)
            instance = type(self.__getattribute__(attribute))
            data[attribute] = value
            if isinstance(value, datetime.datetime):
                data[attribute] = f'{value:%m/%d/%Y %H:%M:%S}'
        return data

    @classmethod
    def from_keys(cls, **kwargs):
        required_arguments = len(cls.REQUIRED) + len(cls.JSON_IGNORE)
        if len(kwargs) < required_arguments:
            raise AttributeError(f'No, at least {required_arguments} values are required.\n{cls.REQUIRED + cls.JSON_IGNORE}')

        extra = (kwargs.keys() - (cls.REQUIRED + cls.OPTIONAL + cls.JSON_IGNORE))
        for _ in extra:
            kwargs.pop(_)
        return cls(**kwargs)
