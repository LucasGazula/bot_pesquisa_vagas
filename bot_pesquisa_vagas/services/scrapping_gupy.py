import os
from dotenv import load_dotenv
from botcity.web import WebBot, Browser, By
load_dotenv()

# //*[@id="radix-0"]/div[2]/button

class Gupy:
    
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
    def visualiza_vaga(self, bot):
        local_vagas = bot.find_element('//*[@id="main-content"]/ul', By.XPATH, waiting_time = 10000, ensure_visible = True)
        local_vagas = local_vagas.find_elements_by_tag_name('li')
        
        for vaga in local_vagas:
            linhas = vaga.text
            linhas = linhas.strip().split('\n')
            for linha in linhas:
                print(linha)
            print('------------------------------------------')
