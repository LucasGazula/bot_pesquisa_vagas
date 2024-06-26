import os
from dotenv import load_dotenv
from botcity.web import WebBot, Browser, By
from repository.gupy import Gupy
from repository.conexao_mongo import BancoGupy
from utils import log
load_dotenv()

banco_gupy = BancoGupy()
gupy = Gupy()
# //*[@id="radix-0"]/div[2]/button

class ScrappingGupy:
    
    def acessar_gupy(self, bot):
        bot.browse(os.getenv("link_gupy"))
        
    def verifica_btn(self, bot):
        btn_ok = bot.find_element('//*[@id="radix-0"]/div[2]/button', By.XPATH, waiting_time = 10000, ensure_visible = True)
        if btn_ok:
            try:
                btn_ok.click()
            except Exception as e:
                print(e)
                
    def pesquisa(self, bot):
        input_pesquisa_vaga = bot.find_element("undefined-input", By.ID, waiting_time = 5000, ensure_visible = True)
        if input_pesquisa_vaga:
            try:
                input_pesquisa_vaga.send_keys(os.getenv("chave_pesquisa_1"))
            except Exception as e:
                print(e)
        
        
        btn_lupa = bot.find_element("undefined-button", By.ID, waiting_time= 5000, ensure_visible = True)
        if btn_lupa:
            try:
                btn_lupa.click()
            except Exception as e:
                print(e)
    def visualiza_vaga(self, bot, gupy):
        local_vagas = bot.find_element('//*[@id="main-content"]/ul', By.XPATH, waiting_time = 10000, ensure_visible = True)
        local_vagas = local_vagas.find_elements_by_tag_name('li')
        
        for vaga in local_vagas:
            linhas = vaga.text
            linhas = linhas.strip().split('\n')
            if len(linhas) == 6:
                gupy.nome_empresa = linhas[0]
                gupy.nome_vaga = linhas[1]
                gupy.local_vaga = linhas[2]
                gupy.modelo_trabalho = linhas[3]
                gupy.tipo_vaga = linhas[4]
                gupy.disponibilidade_pcd = None
                gupy.data_publicacao = linhas[5]
                
                try:
                    banco_gupy.insere_vaga(gupy)
                    log('Foi possível inserir no banco de dados', "SUCESSO")
                except Exception as e:
                    log('Não foi impossível inserir no banco de dados', "FALHA")
                    print(e)                    
                      
            elif len(linhas) == 7:
                gupy.nome_empresa = linhas[0]
                gupy.nome_vaga = linhas[1]
                gupy.local_vaga = linhas[2]
                gupy.modelo_trabalho = linhas[3]
                gupy.tipo_vaga = linhas[4]
                gupy.disponibilidade_pcd = linhas[5]
                gupy.data_publicacao = linhas[6]
                
                try:
                    banco_gupy.insere_vaga(gupy)
                    log('Foi possível inserir no banco de dados', "SUCESSO")
                except Exception as e:
                    log('Não foi impossível inserir no banco de dados', "FALHA")
                    print(e)                    
                    
                
            print('------------------------------------------')

