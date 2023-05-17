from abc import ABC


class DataSource(ABC):
    def _connect(self):
        pass


class Connection(DataSource):

    def __init__(self, type=None, host=None, port=9999, database=None, user=None, password=None):
        _ = type(host, port, database, user, password)
        self.connection = _.connection

    def __enter__(self):
        if self.connection is None or self.connection.closed:
            print('Connection is closed')
            self.connection = self._connect()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        if exc_tb is not None and self.connection:
            self.connection.rollback()
        else:
            self.connection.commit()


class Cursor:
    def __init__(self, connection=None, stmt=None, params=None):
        if not connection:
            raise AttributeError('No connection to create cursor')
        self.stmt = stmt
        self.type = type
        self.params = params
        self.connection = connection

    def __enter__(self):
        self.cursor = self.connection.cursor()
        print(self.params, type(self.params))
        self.cursor.execute(self.stmt, self.params)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()


class TypedCursor(Cursor):
    def __init__(self, connection=None, stmt=None, type=None, params=None):
        if not connection:
            raise AttributeError('No connection to create cursor')
        super().__init__(connection, stmt, params)
        self.type = type
        

class ReadOneCursor(Cursor):
    def __init__(self, connection=None, stmt=None, params=None):
        super().__init__(connection, stmt, params)

    def __enter__(self):
        return super().__enter__()[0]


class ReadManyTypedCursor(TypedCursor):
    def __init__(self, connection=None, stmt=None, type=None, params=None):
        super().__init__(connection, stmt, type, params)

    def __enter__(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.stmt, self.params or [])
        columns = [col.name for col in self.cursor.description]
        rows = self.cursor.fetchall()
        r = list()
        for row in rows:
            _ = {c: r for c, r in (zip(columns, row))}
            record = self.type.from_keys(**_)
            r.append(record.serialize())
        return r


class ReadOneTypedCursor(ReadManyTypedCursor):
    def __init__(self, connection=None, stmt=None, type=None, params=None):
        super().__init__(connection, stmt, type, params)

    def __enter__(self):
        return super().__enter__()[0]


class WriteOneTypedCursor(TypedCursor):
    def __init__(self, connection=None, stmt=None, type=None, params=None):
        super().__init__(connection, stmt, type, params)

    def __enter__(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.stmt, self.params)
        columns = [col.name for col in self.cursor.description]
        row = self.cursor.fetchone()
        _ = {c: r for c, r in (zip(columns, row))}
        record = self.type.from_keys(**_)
        return record


class WriteManyCursor:
    pass
