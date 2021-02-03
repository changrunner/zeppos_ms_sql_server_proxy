import unittest
from zeppos_ms_sql_server_proxy.execute_sql import ExecuteSql


class TestTheProjectMethods(unittest.TestCase):
    def test_get_execute_methods(self):
        execute_sql = ExecuteSql.execute(
            connection_string="DRIVER={ODBC Driver 17 for SQL Server}; SERVER=localhost\sqlexpress; DATABASE=master; Trusted_Connection=yes;App=Test;",
            execute_statement="execute [sys].[sp_columns] 'spt_monitor'"
        )
        self.assertEqual(201, execute_sql.status_code)


if __name__ == '__main__':
    unittest.main()