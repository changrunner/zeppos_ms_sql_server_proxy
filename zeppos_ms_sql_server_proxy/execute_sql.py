import requests
import pandas as pd
from io import BytesIO
import json


class ExecuteSql:
    def __init__(self, connection_string, execute_statement):
        self._connection_string = connection_string
        self._execute_statement = execute_statement
        self._response = None

    @property
    def status_code(self):
        if self._response:
            return self._response.status_code
        else:
            return -1

    def _execute(self):
        self._response = requests.post(
            url='http://127.0.0.1:5800/execute/',
            data={
                "connection_string": self._connection_string,
                "execute_statement": self._execute_statement}
        )

    @staticmethod
    def execute(connection_string, execute_statement):
        execute_sql = ExecuteSql(
            connection_string=connection_string,
            execute_statement=execute_statement
        )
        execute_sql._execute()
        return execute_sql
