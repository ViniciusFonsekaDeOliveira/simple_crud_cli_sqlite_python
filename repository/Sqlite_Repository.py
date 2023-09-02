from sqlite3 import Connection, Cursor, Row
from repository_utils import get_where_clause_conditions

class SQLite_Repository:
    def __init__(self, connection: Connection) -> None:
        self._db = connection
        self._db.row_factory = Row #allowing search by column name in fetchall and fetchone results.

    @property
    def connection(self):
        return self._db
    
    @property
    def cursor(self) -> Cursor:
        return self._db.cursor()
    
    def create_table(self, connection: Connection, cursor: Cursor, table_name: str, table_schema: dict):
        schema_columns = ','.join([f"{col_name} {col_type}" for col_name, col_type in table_schema.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ( {schema_columns} )"
        cursor.execute(query)
        connection.commit()
        print(f"A tabela {table_name} foi criada com sucesso!")
        cursor.close()

    def findAll(self, connection: Connection, cursor: Cursor, table_name: str, fields="*"):
        query = f"SELECT {fields} FROM {table_name}"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results


    def findOne(self, connection: Connection, cursor: Cursor, table_name: str, identifier: dict, fields="*"):
        clause_conditions, clause_values = get_where_clause_conditions(identifier)
        query = f"SELECT {fields} FROM {table_name} WHERE {clause_conditions}"
        cursor.execute(query, clause_values)
        result = cursor.fetchone()
        cursor.close()
        return result

    def insert(self, connection: Connection, cursor: Cursor, table_name: str, data: dict):
        columns = ",".join(data.keys())
        placeholders = ",".join(["?"] * len(data.keys()))
        values = tuple(data.values())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(query, values)
        connection.commit()
        last_id = cursor.lastrowid
        cursor.close()
        return last_id


    def update(self, connection: Connection, cursor: Cursor, table_name: str, updated_data: dict):
        columns_to_update = ",".join([f"{column}=?" for column in updated_data.keys()])
        clause_conditions, clause_values = get_where_clause_conditions(updated_data)
        values_to_update = tuple(updated_data.values()) + clause_values
        query = f"UPDATE {table_name} SET {columns_to_update} WHERE {clause_conditions}"
        cursor.execute(query, values_to_update)
        connection.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        return rows_affected

    def delete(self, connection: Connection, cursor: Cursor, table_name: str, identifier: dict):
        clause_conditions, clause_values = get_where_clause_conditions(identifier)
        query = f"DELETE FROM {table_name} WHERE {clause_conditions}"
        cursor.execute(query, clause_values)
        connection.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        return rows_affected


    def close_connection(self):
        if self.connection:
            self._db.close()
            print("Conexão com o SQLite encerrada com sucesso!")
