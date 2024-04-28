import os
from dotenv import load_dotenv
from botcity.web import WebBot, Browser, By
load_dotenv()

bot = WebBot()
class Glassdoor:
    
    def acessar_gupy(self, bot):
        bot.browse(os.getenv("link_glassdoor"))
        
    def pesquisa_glassdoor(self, bot):
        input_pesquisa = bot.find_element("searchBar-jobTitle", By.ID, waiting_time = 5000, ensure_visible = True)
        if input_pesquisa:
            try:
                input_pesquisa.send_keys(os.getenv("chave_pesquisa_1"))
                bot.key_enter()
            except Exception as e:
                print(e)
                
        
                
    # def seleciona_setor(self, bot):
        