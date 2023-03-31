
import unittest

from konnector.model.owner import Owner


class TestOwner(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.valid_owner_dict = dict(id=1, first_name='Bye', last_name='Hi', email='byehi@byehi.com', phone_no='5129985123')
        cls.invalid_owner_dict = dict(first_name='Bye', last_name='Hi', email='byehi@byehi.com', phone_no='5129985123')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.valid_owner_dict = None
        cls.invalid_valid_owner_dict = None

    def test_from_keys_returns_owner_when_attributes_match_class_attributes(self):
        owner = Owner.from_keys(**self.valid_owner_dict)
        self.assertIsNotNone(owner, msg='Assert is not none')
        self.assertIsInstance(owner, cls=Owner, msg='Assert is instance none')

    def test_from_keys_raises_exception_when_attribute_names_do_not_match_class_attributes(self):
        self.assertRaises(AttributeError, Owner.from_keys, **self.invalid_owner_dict, msg='Should raise AttributeError')

