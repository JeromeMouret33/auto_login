import logging
import time
import os
import re
from pages_core import Page
from init_session import Initsession
from init_session import PRODUCTION_BASE_URL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




class ReportsLocators(object):
    LOGIN_INPUT = (By.XPATH, '//*[@id="__ac_name"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="__ac_password"]')
    BUTTON_VALID = (By.XPATH, '//*[@id="__ac_password"]')



class ReportsPage(Page):
    def __init__(self, driver, base_url=''):
        super().__init__(driver, base_url)

    def credentials(self):
        self.send_credentials_login('jerome.mouret', *ReportsLocators.LOGIN_INPUT)
        self.send_credentials_password('MDP', *ReportsLocators.PASSWORD_INPUT)
        self.send_key_enter(*ReportsLocators.BUTTON_VALID)



def main():
    """ Main function """

    session = Initsession(PRODUCTION_BASE_URL)
    session.start_session()
    login = ReportsPage(session.driver, session.base_url)
    login.credentials()
    time.sleep(10)


if __name__ == '__main__':
    main()

