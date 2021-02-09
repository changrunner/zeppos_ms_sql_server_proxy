import requests


class LoadFromCsv:
    def __init__(self, server_name, database_name, schema_name, table_name, csv_root_directory, sep="|"):
        self._server_name = server_name
        self._database_name = database_name
        self._schema_name = schema_name
        self._table_name = table_name
        self._csv_root_directory = csv_root_directory
        self._sep = sep
        self._response = None

    @property
    def status_code(self):
        if self._response:
            return self._response.status_code
        else:
            return -1

    def _execute(self):
        self._response = requests.post(
            url='http://127.0.0.1:5800/load_from_csv/',
            data={
                "server_name": self._server_name ,
                "database_name": self._database_name,
                "schema_name": self._schema_name,
                "table_name": self._table_name,
                "csv_root_directory": self._csv_root_directory,
                "sep": self._sep
            }
        )
        print(self._response.status_code)

    @staticmethod
    def execute(server_name, database_name, schema_name, table_name, csv_root_directory, sep="|"):
        load_from_csv = LoadFromCsv(
            server_name=server_name,
            database_name=database_name,
            schema_name=schema_name,
            table_name=table_name,
            csv_root_directory=csv_root_directory,
            sep=sep
        )
        load_from_csv._execute()
        return load_from_csv
