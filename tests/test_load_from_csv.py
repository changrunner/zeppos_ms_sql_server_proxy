import unittest
from zeppos_ms_sql_server_proxy.load_from_csv import LoadFromCsv


class TestTheProjectMethods(unittest.TestCase):
    def test_get_execute_methods(self):
        extract_to_csv = LoadFromCsv.execute(
            server_name="localhost\sqlexpress",
            database_name="master",
            schema_name="dbo",
            table_name="ms_sql_server_proxy_test",
            csv_root_directory=r"c:\temp\ms_sql_server_proxy",
        )
        self.assertEqual(201, extract_to_csv.status_code)


if __name__ == '__main__':
    unittest.main()
