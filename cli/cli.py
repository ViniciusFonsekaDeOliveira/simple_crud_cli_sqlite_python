
from decouple import AutoConfig
config = AutoConfig()
path_to_root_project = config("PATH_TO_ROOT_PROJECT", default=None)
import sys
sys.path.append(path_to_root_project)
from domain.Person import Person
from repository.Sqlite_Repository import SQLite_Repository
import uuid
import sqlite3

def cadastrarPessoa():
    firstname = input("\nDigite o primeiro nome: ")
    lastname = input("\nDigite o ultimo nome: ")
    nickname = input("\nDigite o apelido: ")
    email = input("\nDigite o email: ")

    new_uuid = str(uuid.uuid4())
    person = Person(new_uuid, firstname.strip(), lastname.strip(), nickname.strip(), email.strip())

    db_path = config("DB_PATH", default=None)
    connection = sqlite3.connect(db_path)
    repository = SQLite_Repository(connection)

    repository.insert("Person", person.to_dict())
    print("Pessoa inserida com sucesso!")
    repository.close_connection()

    
def listarTodas():

    db_path = config("DB_PATH", default=None)
    connection = sqlite3.connect(db_path)
    repository = SQLite_Repository(connection)
    
    results = repository.findAll("Person")

    name_list = []
    for person in results:
        name_list.append(person["firstname"])
    
    name_list.sort()
    for name in name_list:
        print(name)
    

def procurarAlguma():
    firstname = input("\nDigite o primeiro nome: ")
    lastname = input("\nDigite o ultimo nome: ")
    
    db_path = config("DB_PATH", default=None)
    connection = sqlite3.connect(db_path)
    repository = SQLite_Repository(connection)

    data_to_search = {
        "firstname": firstname,
        "lastname": lastname
    }
    
    result = repository.findOne("Person", data_identifier=data_to_search)

    if result == None:
        print("Resultado não encontrado!")
        return

    for person in result:
        print(person)


def atualizarRegistro():
    firstname = input("\nDigite o primeiro nome do registro para ser alterado: ")
    lastname = input("\nDigite o ultimo nome do registro para ser alterado: ")

    data_identifier = {
        "firstname": firstname,
        "lastname": lastname
    }

    field = input("\nDigite o nome campo a ser alterado: ")
    data = input("\nDigite o dado a ser inserido no campo a ser alterado: ")

    possibilities = ["uuid", "firstname", "lastname", "nickname", "email" ]

    if field not in possibilities:
        raise ValueError("Erro. O campo digitado precisa existir!")


    updated_data = {
        f"{field}": f"{data}"
    }
    
    db_path = config("DB_PATH", default=None)
    connection = sqlite3.connect(db_path)
    repository = SQLite_Repository(connection)

    repository.update("Person", data_identifier, updated_data)
    print(f"O campo {field} de {firstname} foi alterado com sucesso!")
    repository.close_connection()


def deletarAlguma():
    firstname = input("\nDigite o primeiro nome do registro a ser deletado: ")
    lastname = input("\nDigite o ultimo nome do registro a ser deletado: ")

    data_identifier = {
        "firstname": firstname,
        "lastname": lastname
    }

    db_path = config("DB_PATH", default=None)
    connection = sqlite3.connect(db_path)
    repository = SQLite_Repository(connection)

    deleted = repository.delete("Person", data_identifier)
    if deleted:
        print("Registro deletado com sucesso!" + deleted)

    repository.close_connection()


def sair():
    print("Encerrando!")
    exit()
    
def menu():
    menu_string = ("\nBem-vindo(a) ao Python CLI\n"+
                   "Escolha a operação que deseja efetuar:\n" +
                   "(1) Cadastrar pessoa" +
                   "\n(2) Listar todas" +
                   "\n(3) Procurar alguma" +
                   "\n(4) Atualizar registro" +
                   "\n(5) Deletar alguma" +
                   "\n(6) Sair do programa")
    
    operation = {
        1: cadastrarPessoa, 
        2: listarTodas,
        3: procurarAlguma,
        4: atualizarRegistro,
        5: deletarAlguma,
        6: sair
    }

    while (True):
        print(menu_string)
        opcao = int(input("\nDigite sua opção: "))

        if opcao < 1 or opcao > 6:
            print("Opção inválida!")
            break
        else:
            operation[opcao]()


if __name__ == "__main__":
    menu()