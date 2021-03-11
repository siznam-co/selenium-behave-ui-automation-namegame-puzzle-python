from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os, time


class BASEPAGE():
    
    WAIT = 10

    def __init__(self, context):
        self.browser = context.browser

    def find_element(self, by):
        try:
            wait = WebDriverWait(self.browser, self.WAIT)
            element = wait.until(EC.visibility_of_element_located(by))
            return element
        except TimeoutException as timeOutExcept:
            try:
                return self.browser.find_element(*by)
            except NoSuchElementException as e:
                print(e)
                return None

    def find_elements(self, by):
        try:
            wait = WebDriverWait(self.browser, self.WAIT)
            wait.until(EC.visibility_of_element_located(by))
            return self.browser.find_elements(*by)
        except:
            try:
                return self.browser.find_elements(*by)
            except NoSuchElementException as e:
                print(e)
                return None

    def click_element(self, element):
        try:
            element.click()
        except:
            try:
                self.wait = WebDriverWait(self.browser, self.WAIT)
                self.wait.until(EC.element_to_be_clickable(element))
                element.click()
            except:
                time.sleep(5)
                ActionChains(self.browser).move_to_element(element).perform()
                element.click()

    def hover_over_element(self, element):
        try:
            ActionChains(self.browser).move_to_element(element).perform()
        except Exception as e:
            print(e)

    def send_text_to_element(self, element, str_keys):
        try:
            element.send_keys(str_keys)
        except NoSuchElementException:
            self.wait = WebDriverWait(self.browser, self.WAIT)
            self.wait.until(EC.visibility_of_element_located(element))
            element.send_keys(str_keys)

    def get_element_text(self, element):
        try:
            return element.text
        except NoSuchElementException:
            self.wait = WebDriverWait(self.browser, self.WAIT)
            self.wait.until(EC.visibility_of_element_located(element))
            return element.text

    def get_element_value(self, element):
        try:
            element.get_value()
        except NoSuchElementException:
            self.wait = WebDriverWait(self.browser, self.WAIT)
            self.wait.until(EC.visibility_of_element_located(element))
            element.getValue()

    def is_element_displayed(self, by):
        try:
            self.wait = WebDriverWait(self.browser, self.WAIT)
            element = self.wait.until(EC.visibility_of(self.find_element(by)))
            return element.is_displayed()
        except:
            return False

    def get_attribute(self, element, attributes):
        try:
            return element.get_attribute(attributes)
        except NoSuchElementException:
            self.wait = WebDriverWait(self.browser, self.WAIT)
            self.wait.until(EC.visibility_of_element_located(element))
            return element.get_attribute(attributes)

    def get_download_file(self, fileName):
        cwd = os.getcwd()
        downloadfolder = cwd+"\\downloads\\"
        return os.path.isfile(downloadfolder + fileName)

    def remove_download_files(self):
        cwd = os.getcwd()
        downloadfolder = cwd + "\\downloads\\"
        fileList = os.listdir(downloadfolder)
        for fileName in fileList:
            os.remove(downloadfolder + "\\" + fileName)

    def swipe(self, card, dir):
        action_chains =  ActionChains(self.browser)
        action_chains.move_to_element(card).click().perform()
        if dir.lower() == "right":
            action_chains.click_and_hold(card).move_by_offset(1000,0).release().perform()
        elif dir.lower == "left":
            action_chains.click_and_hold(card).move_by_offset(-1000, 0).release().perform()
        else:
            action_chains.click_and_hold(card).move_by_offset(0, 1000).release().perform()

        time.sleep(5)

    def wait_till_process(self):
        print("Waiting till process")
        tries = 5
        while (tries > 0):
            try:
                elem = self.browser.find_element_by_xpath("//div[contains(@class, 'sk-spinner')]")
                if elem.is_displayed():
                    time.sleep(1)
                    tries = tries - 1
                else:
                    break
            except:
                break

    """def click_checkbox(self, checkbox, condition):
        if ( checkbox.is_selected() != condition):
            self.click_element(checkbox)"""