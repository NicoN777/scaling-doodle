import unittest
from konnector.model import Response


class TestResponse(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.valid_response_dict = dict(http_code=200, message="OK", data={})
        cls.invalid_response_dict = dict(message="Server Error", data=None)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.valid_response_dict = None
        cls.invalid_response_dict = None

    def test_from_keys_returns_response_when_attributes_match_class_attributes_names_and_length(self):
        response = Response.from_keys(**self.valid_response_dict)
        self.assertIsNotNone(response)
        self.assertEqual(response.http_code, 200)
        self.assertEqual(response.message, "OK")

    def test_from_keys_raises_attribute_error_exception_when_missing_attributes_names(self):
        self.assertRaises(AttributeError, Response.from_keys, **self.invalid_response_dict)
