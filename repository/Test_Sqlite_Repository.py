import unittest
from unittest import TestCase
from unittest.mock import Mock, patch
from Sqlite_Repository import SQLite_Repository

class Test_Sqlite_Repository(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection_mock = Mock()
        cls.cursor_mock = cls.connection_mock.cursor.return_value
       
    
    @classmethod
    def tearDownClass(cls):
        cls.connection_mock.close_connection()
    
    def test_create_table(self):
        table_name_test = "test"
        table_schema_test = {
            "id": "INTEGER PRIMARY KEY",
            "firstname": "TEXT"
        }
        connection_mock = self.connection_mock
        cursor_mock = self.cursor_mock
        
        repo_mock = SQLite_Repository(connection_mock)

        with patch("builtins.print") as print_message:
            repo_mock.create_table(connection_mock, cursor_mock, table_name_test, table_schema_test)

            cursor_mock.execute.assert_called_once_with("CREATE TABLE IF NOT EXISTS test ( id INTEGER PRIMARY KEY,firstname TEXT )")
            connection_mock.commit.assert_called_once()
            print_message.assert_called_once_with("A tabela test foi criada com sucesso!")      
            cursor_mock.close.assert_called_once()


    def test_findAll(self):
        pass

    def test_findOne(self):
        pass

    def test_insert(self):
        pass

    def test_update(self):
        pass

    def test_delete(self):
        pass

    def test_close_connection(self):
        pass

if __name__ == "__main__":
    unittest.main()
