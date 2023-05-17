from konnector.data import Connection, Cursor, ReadOneCursor, ReadManyTypedCursor, ReadOneTypedCursor, WriteOneTypedCursor
from konnector.data import Postgres
from konnector.data import RedisClient
import os

DEFAULT_REDIS_TTL_SECONDS=600

pg_password = os.environ.get('PG_PASSWORD', "secret")
redis_password = os.environ.get('REDIS_PASSWORD', 'p422w0rd')
postgres_conn = Connection(type=Postgres, host='127.0.0.1', database='postgres', user='postgres', password=pg_password)
redis_client = RedisClient(host='localhost', port=9736, password=redis_password, decode_responses=True)


from functools import wraps

def pre(f):
    msg = f.__qualname__
    @wraps(f)
    def _(*args, **kwargs):
        result = f(*args, **kwargs)
        print(f'Result: {result}')
        return result
    return _

@pre
def sum(a,b):
    print(f'{a} + {b} = ?')
    return a+b

if __name__ == '__main__':
    a = sum(5,6)



