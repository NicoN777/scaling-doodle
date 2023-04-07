import base64
import datetime
import uuid
from konnector.app import KONNECTOR_SESSION_NAME
from konnector.sideb import (redis_client, DEFAULT_REDIS_TTL_SECONDS)
from konnector.model import Owner


def is_session_alive(knktr_session) -> Owner:
    session = redis_client.hgetall(knktr_session)
    if session:
        return session
    return None


def __session_generator(owner: Owner):
    return base64.b64encode(
        bytes(str(uuid.uuid5(uuid.NAMESPACE_DNS, 'knktr'))
              + str(owner.id) + owner.email + f'{datetime.datetime.now():%H%M%S}', 'ascii'))


def store_session_with_expiration(owner: Owner):
    knktr_session = __session_generator(owner)
    _ = {KONNECTOR_SESSION_NAME: knktr_session}
    cached = redis_client.hset(knktr_session, mapping=owner.deserialize())
    expiration = redis_client.expire(knktr_session, DEFAULT_REDIS_TTL_SECONDS)
    if cached and expiration:
        return _