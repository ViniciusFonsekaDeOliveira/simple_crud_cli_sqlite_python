import unittest
from unittest import TestCase
from unittest.mock import Mock, patch
from Sqlite_Repository import SQLite_Repository

class Test_Sqlite_Repository(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection_mock = Mock()
        cls.repo_mock = SQLite_Repository(cls.connection_mock)
    
    @classmethod
    def tearDownClass(cls):
        if hasattr(cls.repo_mock, "close_connection"):
            cls.repo_mock.close_connection()
            print("Conexão mockada encerrada com sucesso!")


    def test_connection(self):
        connection_mock = self.connection_mock
        repo_mock = self.repo_mock
    
        self.assertEqual(connection_mock, repo_mock.connection)


    def test_cursor(self):
        repo_mock = self.repo_mock
        
        cursor_mock = Mock()
        self.connection_mock.cursor.return_value = cursor_mock

        self.assertEqual(repo_mock.cursor, cursor_mock)

    
    def test_create_table(self):
        table_name_test = "test"
        table_schema_test = {
            "id": "INTEGER PRIMARY KEY",
            "firstname": "TEXT"
        }
        cursor_mock = Mock()
        self.connection_mock.cursor.return_value = cursor_mock
    
        with patch("builtins.print") as print_message:
            self.repo_mock.create_table(table_name_test, table_schema_test)

            self.repo_mock.cursor.execute.assert_called_once_with("CREATE TABLE IF NOT EXISTS test ( id INTEGER PRIMARY KEY,firstname TEXT )")
            self.repo_mock.connection.commit.assert_called_once()
            print_message.assert_called_once_with("A tabela test foi criada com sucesso!")      
            self.repo_mock.cursor.close.assert_called_once()


    def test_findAll(self):
        cursor_mock  = Mock()
        self.connection_mock.cursor.return_value = cursor_mock
        self.connection_mock.cursor.return_value.fetchall.return_value = [("test1", ),("test2", )]

        table_name = "test"

        results = self.repo_mock.findAll(table_name)

        self.repo_mock.cursor.execute.assert_called_once_with("SELECT * FROM test")
        self.assertEqual(results, [("test1", ),("test2", )])
        self.repo_mock.cursor.close.assert_called_once()


    def test_findOne(self):
        cursor_mock = Mock()
        self.connection_mock.cursor.return_value = cursor_mock
        self.connection_mock.cursor.return_value.fetchone.return_value = [("test1",)]

        table_name = "test"
        identifier = {
            "id": "test",
            }

        result = self.repo_mock.findOne(table_name, identifier)

        self.repo_mock.cursor.execute.assert_called_once_with("SELECT * FROM test WHERE id=?", ("test",))
        self.assertEqual(result, [("test1",)])
        self.repo_mock.cursor.fetchone.assert_called_once()
        self.repo_mock.cursor.close.assert_called_once()


    def test_insert(self):
        cursor_mock = Mock()
        self.connection_mock.cursor.return_value = cursor_mock
        self.connection_mock.cursor.return_value.lastrowid = 1

        table_name = "test"
        data_to_insert = {
            "id": "test",
            "data": "test_data"
        }

        result = self.repo_mock.insert(table_name, data_to_insert)

        self.repo_mock.cursor.execute.assert_called_once_with("INSERT INTO test (id,data) VALUES (?,?)", ("test", "test_data"))
        self.repo_mock.connection.commit.assert_called()
        self.repo_mock.cursor.close.assert_called_once()
        self.assertEqual(result, 1)


    def test_update(self):
        cursor_mock = Mock()
        self.connection_mock.cursor.return_value = cursor_mock
        self.connection_mock.cursor.return_value.rowcount = 1

        table_name = "test"
        data_identifier = {
            "id": "test"
        }
        updated_data = {
            "id": "test_id",
            "data": "new_data"
        }

        result = self.repo_mock.update(table_name, data_identifier, updated_data)
        self.repo_mock.cursor.execute.assert_called_once_with("UPDATE test SET id=?,data=? WHERE id=?", ("test_id", "new_data", "test"))
        self.repo_mock.cursor.close.assert_called_once()
        self.assertEqual(result, 1)


    def test_delete(self):
        cursor_mock = Mock()
        self.connection_mock.cursor.return_value = cursor_mock
        self.connection_mock.cursor.return_value.rowcount = 1

        table_name = "test"
        data_identifier = {
            "id": "test_id"
        }

        result = self.repo_mock.delete(table_name, data_identifier)
        self.repo_mock.cursor.execute.assert_called_once_with("DELETE FROM test WHERE id=?", ("test_id",))
        self.repo_mock.cursor.close.assert_called_once()
        self.assertEqual(result, 1)


    def test_close_connection(self):
        with patch("builtins.print") as print_message:
            self.repo_mock.close_connection()
            print_message.assert_called_once_with("Conexão com o SQLite encerrada com sucesso!")
            self.connection_mock.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()
