import requests


class ExtractToCsv:
    def __init__(self, connection_string, sql_statement, csv_root_directory, csv_file_name):
        self._connection_string = connection_string
        self._sql_statement = sql_statement
        self._csv_root_directory = csv_root_directory
        self._csv_file_name = csv_file_name
        self._response = None

    @property
    def status_code(self):
        if self._response:
            return self._response.status_code
        else:
            return -1

    def _execute(self):
        self._response = requests.post(
            url='http://127.0.0.1:5800/extract_to_csv/',
            data={
                "connection_string": self._connection_string,
                "sql_statement": self._sql_statement,
                "csv_root_directory": self._csv_root_directory,
                "csv_file_name": self._csv_file_name
            }
        )
        print(self._response.status_code)

    @staticmethod
    def execute(connection_string, sql_statement, csv_root_directory, csv_file_name):
        extract_to_csv = ExtractToCsv(
            connection_string=connection_string,
            sql_statement=sql_statement,
            csv_root_directory=csv_root_directory,
            csv_file_name=csv_file_name
        )
        extract_to_csv._execute()
        return extract_to_csv
