from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager

def inicia_navegacao():
    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME

    # Uncomment to set the WebDriver path
    bot.driver_path = ChromeDriverManager().install()

    return bot

    