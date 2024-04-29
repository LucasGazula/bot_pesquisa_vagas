from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

data = datetime.now()

class BancoGupy:
    def __init__(self):
        self.mongo_client = MongoClient(os.getenv("mongo_client"))
        self.database = self.mongo_client["pesquisa_vagas"]
        self.colecao = self.database['Vagas_Gupy']
        
    def insere_vaga(self, gupy):
        vaga =  {
            "nome_empresa" : f"{gupy.nome_empresa}",
            "nome_vaga" : f"{gupy.nome_vaga}",
            "local_vaga" : f"{gupy.local_vaga}",
            "modelo_trabalho" : f"{gupy.modelo_trabalho}",
            "tipo_vaga" : f"{gupy.tipo_vaga}",
            "disponibilidade_pcd" : f"{gupy.disponibilidade_pcd}",
            "data_publicao" : f"{gupy.data_publicacao}",
            "data_consulta": "",
            "data_cadastro" : f"{data}"
        
        }
        
        self.colecao.insert_one(vaga)
        print("inserindo vaga")
    
        
        
# mongo = BancoGupy()
# mongo.insere_vaga()