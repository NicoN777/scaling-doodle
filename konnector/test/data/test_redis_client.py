import unittest
from unittest import mock
from konnector.data.redis_client import RedisClient

class TestRedisClient(unittest.TestCase):

    def setUp(self) -> None:
        self.redis_client_patcher = mock.patch('konnector.data.redis_client.RedisClient')
        print(self.redis_client_patcher)
        self.redis_client_patcher.start()

    def tearDown(self) -> None:
        self.redis_client_patcher.stop()

    def test_redis_client(self):
        instance = self.redis_client_patcher.new
        print(instance)
        # print(self.redis_client_mock)
        # self.redis_client_mock.
