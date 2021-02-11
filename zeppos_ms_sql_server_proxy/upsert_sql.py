import requests


class UpsertSql:
    def __init__(self, connection_string, dataframe, table_schema, table_name, batch_size):
        self._connection_string = connection_string
        self._dataframe = dataframe
        self._table_schema = table_schema
        self._table_name = table_name
        self._batch_size = batch_size
        self._response = None

    @property
    def status_code(self):
        if self._response:
            return self._response.status_code
        else:
            return -1

    def _execute(self):
        self._response = requests.post(
            url='http://127.0.0.1:5800/upsert/by_record/',
            data={
                "connection_string": self._connection_string,
                "dataframe": self._dataframe,
                "table_schema": self._table_schema,
                "table_name": self._table_name,
                "batch_size": self._batch_size,
            }
        )
        print(self._response)

    @staticmethod
    def execute(connection_string, dataframe, table_schema, table_name, batch_size):
        upsert_sql = UpsertSql(
            connection_string=connection_string,
            dataframe=dataframe,
            table_schema=table_schema,
            table_name=table_name,
            batch_size=batch_size
        )
        upsert_sql._execute()
        return upsert_sql
