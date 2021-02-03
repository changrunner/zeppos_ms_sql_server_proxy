import unittest
from zeppos_ms_sql_server_proxy.extract_to_csv import ExtractToCsv


class TestTheProjectMethods(unittest.TestCase):
    def test_get_execute_methods(self):
        extract_to_csv = ExtractToCsv.execute(
            connection_string="DRIVER={ODBC Driver 17 for SQL Server}; SERVER=localhost\sqlexpress; DATABASE=master; Trusted_Connection=yes;App=Test;",
            sql_statement="select * from information_schema.columns",
            csv_root_directory=r"c:\temp\ms_sql_server_proxy",
            csv_file_name="test_file.csv"
        )
        self.assertEqual(201, extract_to_csv.status_code)


if __name__ == '__main__':
    unittest.main()
