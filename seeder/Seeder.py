from decouple import AutoConfig
config = AutoConfig()
path_to_root = config("PATH_TO_ROOT_PROJECT", default=None)
import sys
sys.path.append(path_to_root)

import csv
import sqlite3
from domain.Person import Person
from repository.Sqlite_Repository import SQLite_Repository


def seeder(filename: str, dbname: str = "mydb.db"):
    with open(filename, "r", newline="") as csvfile:
        lines = csv.reader(csvfile, delimiter=";")
        header = next(lines)
        print(header)

        # connection = sqlite3.connect(dbname)

        # repository = SQLite_Repository(connection)
        # table = "Person"
        # table_schema = {
        #     "uuid": "TEXT PRIMARY KEY",
        #     "firstname": "TEXT",
        #     "lastname": "TEXT",
        #     "nickname": "TEXT",
        #     "email": "TEXT"
        # }
        # repository.create_table(table, table_schema)

        # for line in lines:
        #     person = Person(*line)
        #     repository.insert(table, person.to_dict())
        
        # print("Dados inseridos no banco de dados com sucesso!")
        # repository.close_connection()



if __name__ == "__main__":
    path_to_file = config("PATH_TO_FILE", default=None)
    print(path_to_file)
    seeder(path_to_file)

# Foi necessário adicionar a biblioteca do python-decouple para ler variáveis de ambiente do arquivo .env
# Por alguma razão, as pastas que organizam este programa não estavam sendo encontradas pelo sys.path.
# o que fez com que eu tivesse que configurar isso manualmente.
# Para resolver este problema, salvei num arquivo .env os caminhos absolutos do diretório do projeto e do diretorio
# onde se encontrada o arquivo com os dados fake. E usei o decouple para chamá-los sempre que necessário.