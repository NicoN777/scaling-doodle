from konnector.data import Connection, Cursor, ReadOneCursor, ReadManyTypedCursor, ReadOneTypedCursor, WriteOneTypedCursor
from konnector.data import Postgres
from konnector.data import RedisClient
import os

DEFAULT_REDIS_TTL_SECONDS=600

password = os.environ.get('PG_PASSWORD', "'secret'")
postgres_conn = Connection(type=Postgres, host='127.0.0.1', database='postgres', user='postgres', password=password)
redis_client = RedisClient(host='localhost', port=6379, decode_responses=True)



