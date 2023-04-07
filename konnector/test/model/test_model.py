import unittest
from .test_owner import TestOwner
from .test_application import TestApplication
from .test_response import TestResponse


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestOwner())
    suite.addTest(TestApplication())
    suite.addTest(TestResponse())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())