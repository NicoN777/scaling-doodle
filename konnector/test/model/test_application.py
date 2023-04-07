import unittest

from konnector.model import Owner
from konnector.model import Application


class TestApplication(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.owner = Owner(1, 'Toasty', 'Nunez', 'toasty_nunez@toaster.com', '5129980327')
        cls.valid_application_dict = dict(id=1, name='2', password='fsdfasd', owner=cls.owner)
        cls.invalid_application_dict = dict(id=1, name='2', password='fsdfasd')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.valid_application_dict = None
        cls.invalid_application_dict = None

    def test_from_keys_returns_application_when_attributes_match_class_attributes(self):
        application = Application.from_keys(**self.valid_application_dict)
        self.assertIsNotNone(application, msg='Assert is not none')
        self.assertIsInstance(application, cls=Application, msg='Assert is instance none')

    def test_from_keys_raises_attribute_error_exception_when_attribute_names_do_not_match_class_attributes(self):
        self.assertRaises(AttributeError, Application.from_keys, **self.invalid_application_dict)
