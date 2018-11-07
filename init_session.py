""" init_session automation main module """
import glob, os

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PRODUCTION_BASE_URL = 'http://ecampusbordeaux.epsi.fr/login_form'

class Initsession:
    """ Main init_session automation process """
    def __init__(self, base_url=''):
        self.base_url = base_url
        self.timeout = 30
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-fullscreen")
        self.chrome_options.add_experimental_option("useAutomationExtension", False)
        self.downloads = r"C:\tmp\reports"

        self.chrome_options.add_experimental_option("prefs", {
        "download.default_directory": self.downloads,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
        })

        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        # self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 120)

    def start_session(self, forced_page=''):
        """ start automated session """
        self.driver.get(self.base_url + forced_page)
        print("WAITING FOR HOMEPAGE ...")
        self.wait.until(EC.presence_of_element_located((By.ID, "__ac_password")))
        print("STARTING ...")


    
def main():
    """ Main function """


if __name__ == '__main__':
    main()
