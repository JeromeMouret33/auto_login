# this Base class is serving basic attributes for every single page inherited from ini_session class
# from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import re


class Page(object):
    def __init__(self, driver, base_url=''):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def wait_and_click_element(self, *locator):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        element = wait.until(EC.element_to_be_clickable(locator))
        #time.sleep(1)
        element.click()

    def wait_and_click_element_by_xpath(self, xpath):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()

    def wait_for_element_clickable(self, *locator):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_present(self, delay, *locator):
        element = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(locator))
        return element

    def wait_for_element_visible(self, delay, *locator):
        element = WebDriverWait(self.driver, delay).until(EC.visibility_of_element_located(locator))
        return element

    def wait_for_element_present_by_xpath(self, delay, xpath):
        element = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element

    def wait_for_element_present_by_link_text(self, delay, link_text):
        element = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.LINK_TEXT, link_text)))
        return element

    def click_element_if_appears(self, delay, *locator):
        try:
            # wait for loading element to appear
            # : need to make sure we don't prematurely check if element
            # : has disappeared before it has had a chance to appear
            element = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(locator))
            #time.sleep(1)
            element.click()

        except TimeoutException:
            # if timeout exception was raised - should be safe to assume loading has finished. 
            # : However this may not always be the case, use with caution, othwise handle appropriately.
            return

    def send_keys(self, text):
        actions = ActionChains(self.driver)
        actions.send_keys(text)
        actions.perform()

    def find_element(self, *locator):
        """ [TODO] """
        return self.driver.find_element(*locator)

    def find_element_by_link_text(self, link_text):
        """ [TODO] """
        return self.driver.find_element(By.LINK_TEXT, link_text)

    def find_elements(self, *locator):
        """ [TODO] """
        return self.driver.find_elements(*locator)

    def set_list_box(self, content, *locator):
        """ Find listbox and set content """
        listbox = self.find_element(*locator)
        Select(listbox).select_by_visible_text(content)

    def set_search_box(self, content, *locator):
        search_box = self.driver.find_element(*locator)
        search_box.click()
        search_box.send_keys(content)
        # search_box.send_keys(Keys.TAB)
        # time.sleep(1)

    def set_input_box(self, content, *locator):
        input_box = self.driver.find_element(*locator)
        # input_box.send_keys(content)
        chars_to_delete = len(input_box.get_attribute('value'))
        input_box.click()
        input_box.send_keys(Keys.END)
        for _ in range(chars_to_delete):
            input_box.send_keys(Keys.BACKSPACE)
        input_box.send_keys(content)
        input_box.send_keys(Keys.TAB)

    def set_and_validate_input_box(self, content, *locator):
        input_box = self.driver.find_element(*locator)
        input_box.send_keys(content)
        input_box.send_keys(Keys.ENTER)

    def set_text_area(self, content, *locator):
        """ Find text_area and set content """
        text_area = self.driver.find_element(*locator)
        text_area.clear()
        text_area.send_keys(content)

    def click_element(self, *locator):
        """ Click button """
        # wait = WebDriverWait(DRIVER, 30)
        # wait.until(EC.element_to_be_clickable((By.ID, button_id)))
        self.driver.find_element(*locator).click()

    def click_link(self, link_text, *locator):
        """ Click button """
        # wait = WebDriverWait(DRIVER, 30)
        # wait.until(EC.element_to_be_clickable((By.ID, button_id)))
        link_xpath = '//a[text()="{}"]'.format(link_text)
        self.driver.find_element(By.XPATH, link_xpath).click()

    def switch_to_child_window(self):
        child_window = self.driver.window_handles[1]
        self.driver.switch_to.window(child_window)

    def switch_to_main_window(self):
        main_window = self.driver.window_handles[0]
        self.driver.switch_to.window(main_window)

    def leave_alert_box(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present(), 'Timed out waiting for popup.')
            alert = self.driver.switch_to_alert()
            alert.accept()
        except TimeoutException:
            # [TODO] Manage exception
            pass

    def open(self, url):
        """ [TODO] """
        url = self.base_url + url
        self.driver.get(url)
        # self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.driver.find_element_by_name("gsft_main")))

    def get_title(self):
        """ [TODO] """
        return self.driver.title

    def get_url(self):
        """ [TODO] """
        return self.driver.current_url

    def hover(self, *locator):
        """ [TODO] """
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def right_click(self, *locator):
        """ [TODO] """
        element = self.find_element(*locator)
        ActionChains(self.driver).context_click(element).perform()


    def send_credentials_login(self, login, *locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element.send_keys(login)
        
    def send_credentials_password(self, password, *locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element.send_keys(password)

    def send_key_enter(self, *locator):
        time.sleep(3)
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element.send_keys(Keys.ENTER)