from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


class conexaoMongo:
    def __init__(self):
        self.mongo_client = MongoClient(os.getenv("mongo_client"))
        self.database = self.mongo_client["pesquisa_vagas"]
        self.colecao = self.database['Vagas_Gupy']
        
    def insere_vaga(self):
        vaga =  {
            "nome_empresa" : "",
            "nome_vaga" : "",
            "local_vaga" : "",
            "modelo_trabalho" : "",
            "tipo_vaga" : "",
            "disponibilidade_pcd" : "",
            "data_publicao" : "",
            "data_consulta": "",
            "data_cadastro" : ""
        
        }
        
        self.colecao.insert_one(vaga)
        print("inserindo vaga")
    
        
        
mongo = conexaoMongo()
mongo.insere_vaga()