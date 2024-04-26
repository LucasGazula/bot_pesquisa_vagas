# Import for the Web Bot
from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
from model import inicia_navegacao
from model.gupy import Gupy
import os
from dotenv import load_dotenv

load_dotenv()

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

gupy = Gupy()

def main():
    
    bot = inicia_navegacao()
     
    gupy.acessar_gupy(bot)
    
    gupy.verifica_btn(bot)
    
    gupy.pesquisa(bot)
    
    gupy.visualiza_vaga(bot)

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
