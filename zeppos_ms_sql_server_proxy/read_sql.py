import requests
import pandas as pd
from io import BytesIO
import json


class ReadSql:
    def __init__(self, connection_string, sql_statement):
        self._connection_string = connection_string
        self._sql_statement = sql_statement
        self._response = None

    @property
    def data(self):
        if self._response:
            if self._response.status_code == 200:
                return json.loads(self._response.content).encode('utf-8')
        return ""

    @property
    def dataframe(self):
        if self.data:
           return pd.read_json(BytesIO(json.loads(self._response.content).encode('utf-8')), orient='table')
        return None

    @property
    def status_code(self):
        if self._response:
            return self._response.status_code
        else:
            return -1

    def _execute(self):
        self._response = requests.post(
            url='http://127.0.0.1:5800/read/',
            data={
                "connection_string": self._connection_string,
                "sql_statement": self._sql_statement}
        )

    @staticmethod
    def execute(connection_string, sql_statement):
        read_sql = ReadSql(
            connection_string=connection_string,
            sql_statement=sql_statement
        )
        read_sql._execute()
        return read_sql
