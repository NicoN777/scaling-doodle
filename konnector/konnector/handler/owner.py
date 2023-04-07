from konnector.model import Owner, User, Response
from konnector.sideb import (postgres_conn,
                             ReadManyTypedCursor,
                             WriteOneTypedCursor,
                             redis_client)


def get_owners():
    with postgres_conn as conn:
        type = Owner
        stmt = f"SELECT {','.join(type.REQUIRED + type.OPTIONAL)} FROM owner"
        with ReadManyTypedCursor(conn, stmt, Owner) as execute:
            result_set = execute
            return Response(200, message='OK', data=result_set)


def register(user: User) -> Response:
    registered = _is_registered(key_prefix='Owner:', user=user)
    if registered:
        return Response(400, message='User already exists', data=registered)

    try:
        result = _persist_owner(user=user)
        if not result:
            return Response(400, message='Something went wrong, :(')
    except Exception:
        return Response(400, message='Something went wrong, :(')

    return Response(200, message='OK', data=result)


def _persist_owner(user: User = None) -> Owner:
    persisted = _persist_owner_db(user)
    if persisted:
        persisted_serde = persisted.serialize()
        cached = _cache_result(key_prefix = 'Owner:', key=user.email, mapping=persisted_serde)
        if cached:
            return persisted_serde
    return None


def _persist_owner_db(user: User) -> Owner:
    _ = user.deserialize().copy()
    with postgres_conn as conn:
        type = Owner
        place_holders = ','.join(['%s' for i in range(len(_.values()))])
        stmt = f"""INSERT INTO owner({','.join(_.keys())}) VALUES ({place_holders}) RETURNING {','.join(type.REQUIRED + type.JSON_IGNORE + type.OPTIONAL)}"""
        with WriteOneTypedCursor(conn, stmt, type, [*_.values()]) as execute:
            result = execute
            return result


def _cache_result(key_prefix: str = '', key: str = '', mapping: dict = None):
    cached = redis_client.hset(key_prefix + key, mapping=mapping)
    return cached


def _is_registered(key_prefix: str = '', user: User = None):
    response = redis_client.hgetall(key_prefix + user.email)
    return response
