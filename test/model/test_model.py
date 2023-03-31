import unittest
from .test_owner import TestOwner
from .test_application import TestApplication


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestOwner('test_default_widget_size'))
    suite.addTest(TestApplication('test_widget_resize'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())