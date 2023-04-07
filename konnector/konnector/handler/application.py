from konnector.model import Owner, Application, Response
from konnector.sideb import (postgres_conn,
                             ReadManyTypedCursor,
                             WriteOneTypedCursor,
                             redis_client)


def get_applications():
    with postgres_conn as conn:
        type = Owner
        stmt = f"SELECT {','.join(type.REQUIRED + type.OPTIONAL)} FROM owner"
        with ReadManyTypedCursor(conn, stmt, Owner) as execute:
            result_set = execute
            return Response(200, message='OK', data=result_set)


def register(application: Application) -> Response:
    registered = _is_registered(key_prefix='Owner:', application=application)
    if registered:
        return Response(400, message='User already exists', data=registered)

    result = _persist_owner(application=application)
    if not result:
        return Response(400, message='Something went wrong, :(')

    return Response(200, message='OK', data=result)


def _persist_owner(application: Application = None) -> Owner:
    persisted = _persist_owner_db(application)
    if persisted:
        persisted_serde = persisted.serialize()
        cached = _cache_result(key_prefix = 'Owner:', key=application.email, mapping=persisted_serde)
        if cached:
            return persisted_serde
    return None


def _persist_owner_db(application: Application) -> Owner:
    _ = application.serialize().copy()
    with postgres_conn as conn:
        type = Owner
        place_holders = ','.join(['%s' for i in range(len(_.values()))])
        stmt = f"""INSERT INTO owner({','.join(_.keys())}) VALUES ({place_holders}) RETURNING {','.join(type.REQUIRED + type.OPTIONAL)}"""
        with WriteOneTypedCursor(conn, stmt, type, [*_.values()]) as execute:
            result = execute
            return result


def _cache_result(key_prefix: str = '', key: str = '', mapping: dict = None):
    cached = redis_client.hset(key_prefix + key, mapping=mapping)
    return cached


def _is_registered(key_prefix: str = '', application: Application = None):
    response = redis_client.hgetall(key_prefix + application.email)
    return response
