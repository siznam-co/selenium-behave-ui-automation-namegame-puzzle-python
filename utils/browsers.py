import os
import platform

import urllib3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
#from utils.general import is_headless
# If you have SSL verify error
# cd "/Applications/Python 3.6/"
# sudo "./Install Certificates.command"


def browsers(context, name):

    name = name.lower()
    headless = context.config.userdata.get("headless", "false").lower()
    if name == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        if headless == "true":
            chrome_options.add_argument("--headless")
        context.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
    elif name == 'firefox':
        if headless == "true":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--headless")
        context.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif name == 'safari':
        if platform.system().lower() != "darwin":
            raise OSError("Safari tests can be run only on MacOS")
        context.browser = webdriver.Safari(executable_path=os.path.join("usr", "bin", "safaridriver"))
    else:
        raise KeyError('This browser is not supported by this automation script at this time')

    context.browser.set_page_load_timeout(time_to_wait=100)
    context.browser.implicitly_wait(15)
    context.config.setup_logging()
    context.browser.set_window_size(1920, 1080)
    context.browser.maximize_window()
    return context.browser
