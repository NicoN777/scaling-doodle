from konnector.model.base import Base


class Response(Base):
    JSON_IGNORE = ['http_code']
    REQUIRED = ['message', 'data']
    OPTIONAL = []

    def __init__(self, http_code: int, message=None, data=None):
        self.http_code = http_code
        self.message = message
        self.data = data
