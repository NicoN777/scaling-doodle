from konnector.data.base import DataSource

import psycopg2


class Postgres(DataSource):

    def __init__(self, host=None, port=5432, database=None, user=None, password=None):
        if not host or not database or not user or not password:
            raise AttributeError('Are you serious?')
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self._connect()

    def _connect(self):
        print('Connecting')
        self.connection = psycopg2.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
        return self.connection

    def __str__(self):
        return f'{self.__class__.__name__}(host={self.host}, port={self.port}, database={self.database}, user={self.user})'


