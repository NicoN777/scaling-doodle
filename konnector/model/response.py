from konnector.model.base import Base

class Response(Base):
    __slots__ = ['http_code', 'message', 'data']
    def __init__(self, http_code: int, message=None, data=dict()):
        self.http_code = http_code
        self.message = message
        self.data = data
