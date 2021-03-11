from random import randint, seed

from selenium.webdriver.support.wait import WebDriverWait

from .common.basepage import BASEPAGE
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.general import *
import time


class NameGame(BASEPAGE):
    # random_number = str(randint(1, 5))
    # rnd_locator_person = './/div[@class = "photo"][' + random_number + ']'
    # rnd_locator_person_name = rnd_locator_person + '/div[2]'

    tries = 0
    correct = 0
    streak = 0

    list_fix = [1, 2, 3, 4, 5]
    list_rnd = []
    bool = 0

    locator_dictionary = {
        "given_person": (By.ID, 'name'),
        "correct_person": (By.CLASS_NAME, 'name'),
        "person": (By.XPATH, 'rnd_locator_person'),
        "person_name": (By.XPATH, 'rnd_locator_person_name'),
        "tries_count": (By.CLASS_NAME, 'attempts'),
        "correct_count": (By.CLASS_NAME, 'correct'),
        "streak_count": (By.CLASS_NAME, 'streak')
    }

    constants = {
        "page_title": "name game"
    }
    urls = {
        "Home": "/name-game/"
    }

    def go_to(self, link):
        base_url = get_setting("URL", "url")
        self.browser.get(base_url + self.urls[link])
        # Counts at start
        time.sleep(5)
        self.tries = self.get_element_text(self.find_element(self.locator_dictionary["tries_count"]))
        self.correct = self.get_element_text(self.find_element(self.locator_dictionary["correct_count"]))
        self.streak = self.get_element_text(self.find_element(self.locator_dictionary["streak_count"]))

        if self.browser.title == self.constants[
            "page_title"] and self.tries == '0' and self.correct == '0' and self.streak == '0':
            return True
        else:
            return False

    def click_random_person(self):
        global chosen_person_name
        while self.correct != -1:
            given_person_name = self.get_element_text(self.find_element(self.locator_dictionary["given_person"]))
            # print(self.random_number + " first")
            # chosen_person_name = self.set_person_locators()
            self.bool = 0
            while self.bool < 5:
                r = random.choice(self.list_fix)
                if r not in self.list_rnd:
                    self.bool = self.bool + 1
                    self.list_rnd.append(r)
                    random_number = str(r)
                    print(random_number)
                    # rnd_locator_person = './/div[@class = "photo"][' + random_number + ']'
                    rnd_locator_person = './/div[text() ="' + random_number + '"]/parent::div'
                    rnd_locator_person_name = rnd_locator_person + '/div[2]'
                    chosen_person_name = self.get_element_text(self.find_element((By.XPATH, rnd_locator_person_name)))
                    self.click_element(self.find_element((By.XPATH, rnd_locator_person)))
                    self.tries = str(int(self.tries) + 1)
                    if self.get_attribute(self.find_element((By.XPATH, rnd_locator_person)),
                                          "class") == "photo correct":
                        time.sleep(5)
                        self.bool = 6
                        self.correct = str(int(self.correct) + 1)
                        self.streak = str(int(self.streak) + 1)
                        self.list_rnd.clear()
                    else:
                        self.streak = 0
                else:
                    self.bool = self.bool

            if self.get_element_text(self.find_element(self.locator_dictionary["tries_count"])) == self.tries:
                if self.get_element_text(self.find_element(self.locator_dictionary["correct_count"])) == self.correct:
                    if self.get_element_text(self.find_element(self.locator_dictionary["streak_count"])) == self.streak:
                        print("All counts correct: "+self.tries+" tries / "+self.correct+" correct / "+self.streak+" streak")
                        print("--------")
                        continue

    def click_correct_person(self):
        while self.correct != 261:
            given_p = self.get_element_text(self.find_element(self.locator_dictionary["given_person"]))
            correct_p_photo = './/div[text() = "' + given_p + '"]/parent::div'
            # chosen_person = self.get_element_text(self.find_element(self.locator_dictionary["correct_person"]))
            self.click_element(self.find_element((By.XPATH, correct_p_photo)))
            time.sleep(5)
