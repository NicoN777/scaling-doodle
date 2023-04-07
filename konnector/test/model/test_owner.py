
import unittest

from konnector.model.owner import Owner


class TestOwner(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.valid_owner_dict = dict(id=1, first_name='Bye', last_name='Hi', email='byehi@byehi.com', phone_no='5129980345')
        cls.invalid_owner_dict = dict(first_name='Bye', last_name='Hi', email='byehi@byehi.com', phone_no='5129980345')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.valid_owner_dict = None
        cls.invalid_valid_owner_dict = None

    def test_from_keys_returns_owner_when_attributes_match_class_attributes_names_and_length(self):
        owner = Owner.from_keys(**self.valid_owner_dict)
        self.assertIsNotNone(owner, msg='Assert is not none')
        self.assertIsInstance(owner, cls=Owner, msg='Assert is instance none')

    def test_from_keys_returns_owner_when_attributes_match_class_attributes_names_and_have_required_attributes(self):
        owner = Owner.from_keys(**self.valid_owner_dict)
        self.assertIsNotNone(owner, msg='Assert is not none')
        self.assertIsInstance(owner, cls=Owner, msg='Assert is instance none')

