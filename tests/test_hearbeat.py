import unittest
from zeppos_ms_sql_server_proxy.heartbeat import Heartbeat


class TestTheProjectMethods(unittest.TestCase):
    def test_get_pong_methods(self):
        self.assertEqual("pong", Heartbeat.ping())


if __name__ == '__main__':
    unittest.main()