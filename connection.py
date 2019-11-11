import mysql.connector
from mysql.connector import Error

class Connection:
    def __init__(self):
        self.host='localhost'
        self.database='tree_mainframe'
        self.user='aps'
        self.password='aps2019'
    
    def insertCadastro(self, nome_usuario):
        try:
            connection = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)

            cursor = connection.cursor()
            mySql_insert_query = """INSERT INTO usuario (nome) 
                                    VALUES ('Carlos') """

            # recordTuple = (nome_usuario)
            cursor.execute(mySql_insert_query)
            connection.commit()
            print("Usuário cadastrado com sucesso")

        except mysql.connector.Error as error:
            print("Falha ao tentar cadastrar usuário {}".format(error))

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("Conexão com o banco fechada")