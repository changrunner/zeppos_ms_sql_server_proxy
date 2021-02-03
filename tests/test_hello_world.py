import unittest
from zeppos_pypi_template.hello_world import HelloWorld


class TestTheProjectMethods(unittest.TestCase):
    def test_get_hello_world_methods(self):
        self.assertEqual(HelloWorld.get_hello_world(), "Hello World")


if __name__ == '__main__':
    unittest.main()
