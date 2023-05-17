import redis

from konnector.data.base import DataSource


class RedisClient(DataSource):
    def __init__(self, host=None, port=9999, password=None, decode_responses=True):
        self.client = redis.Redis(host=host, port=port, password=password, decode_responses=decode_responses)

    def hset(self, key, mapping={}):
        print(f'Adding: key: {key} mapping: {mapping}')
        to_insert = mapping.copy()
        nones = [key for key, val in to_insert.items() if not val or isinstance(val, type(...))]
        for none in nones:
            to_insert.pop(none)
        response = self.client.hset(key, mapping=to_insert)
        return response

    def set(self, key, value):
        print(key, value)
        return self.client.set(key, str(value))

    def get(self, key):
        print(key)
        return self.client.get(key)

    def expire(self, key, expiration_seconds):
        print(f'Adding {expiration_seconds} seconds expiration to key: {key}')
        expire_response = self.client.expire(key, expiration_seconds)
        ttl_response = self.client.ttl(key)
        print(f'Expire Response: {expire_response}, TTL Response: {ttl_response}')
        return ttl_response

    def hgetall(self, key):
        response = self.client.hgetall(key)
        if response:
            print(f'Cache hit for key: {key}')
        else:
            print('Cache miss')
        return response


    def rpush(self, list_name: str=None, data: str=None):
        response = self.client.rpush(list_name, data)
        print(response)
        return response

    def propsies(self):
        response = self.client.config_get('*')
        print(response)

