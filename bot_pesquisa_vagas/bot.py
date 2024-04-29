# Import for the Web Bot
from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
from services import inicia_navegacao
from services.scrapping_gupy import ScrappingGupy
from services.scrapping_glassdoor import Glassdoor
from repository.gupy import Gupy
import os
from dotenv import load_dotenv

load_dotenv()

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

scrapping_gupy = ScrappingGupy()
gupy = Gupy()

glassdor = Glassdoor()

def main():
    
    bot = inicia_navegacao()
     
    scrapping_gupy.acessar_gupy(bot)
    
    scrapping_gupy.verifica_btn(bot)
    
    scrapping_gupy.pesquisa(bot)
    
    scrapping_gupy.visualiza_vaga(bot, gupy)
    
    glassdor.acessar_gupy(bot)
    glassdor.pesquisa_glassdoor(bot)
    

    # Configure whether or not to run on headless mode
    # Wait 3 seconds before closing
    
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
