import unittest
from zeppos_ms_sql_server_proxy.upsert_sql import UpsertSql
import pandas as pd

class TestTheProjectMethods(unittest.TestCase):
    def test_get_execute_methods(self):
        upsert_sql = UpsertSql.execute(
            connection_string="DRIVER={ODBC Driver 13 for SQL Server}; SERVER=localhost\sqlexpress; DATABASE=master; Trusted_Connection=yes;",
            dataframe=pd.DataFrame({'column_1': [3600]}, columns=['column_1']).to_json(orient='table'),
            table_schema="dbo",
            table_name="api_test_table",
            batch_size="500"
        )
        self.assertEqual(201, upsert_sql.status_code)


if __name__ == '__main__':
    unittest.main()