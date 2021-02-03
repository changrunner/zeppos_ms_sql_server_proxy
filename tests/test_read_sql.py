import unittest
from zeppos_ms_sql_server_proxy.read_sql import ReadSql


class TestTheProjectMethods(unittest.TestCase):
    def test_get_execute_methods(self):
        read_sql = ReadSql.execute(
            connection_string="DRIVER={ODBC Driver 17 for SQL Server}; SERVER=localhost\sqlexpress; DATABASE=master; Trusted_Connection=yes;App=Test;",
            sql_statement="select SUSER_NAME() as User_Name, APP_NAME() as app_name"
        )
        self.assertEqual(200, read_sql.status_code)
        self.assertGreater(len(read_sql.data), 0)
        df_actual = read_sql.dataframe.copy()
        self.assertEqual(df_actual.iloc[0]["app_name"], 'Test')


if __name__ == '__main__':
    unittest.main()