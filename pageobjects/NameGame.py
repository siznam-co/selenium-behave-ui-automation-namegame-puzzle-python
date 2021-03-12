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

        # TODO: Verify there is title "name game" shown at the top of page.
        # TODO: Verfiy by default intial values for tries,correct, and streak are equal to zero
        if self.browser.title == self.constants[
            "page_title"] and self.tries == '0' and self.correct == '0' and self.streak == '0':
            return True
        else:
            return False

    previous_person_name = ""

    def click_random_person(self):
        global chosen_person_name
        while self.correct != -1:
            given_person_name = self.get_element_text(self.find_element(self.locator_dictionary["given_person"]))
            # TODO: Verify there is heading "who is [name]" is available above the images.
            print("Who is " + given_person_name + "?")
            # TODO: Verify name and displayed photos change after selecting the correct answer
            assert self.previous_person_name != given_person_name, "Person is repeated"
            self.bool = 0
            while self.bool < 5:
                r = random.choice(self.list_fix)
                # TODO: Verify , once we selected wrong person's image the banner cannot be unselected
                if r not in self.list_rnd:
                    self.bool = self.bool + 1
                    self.list_rnd.append(r)
                    random_number = str(r)
                    print(random_number)
                    # rnd_locator_person = './/div[@class = "photo"][' + random_number + ']'
                    rnd_locator_person = './/div[text() ="' + random_number + '"]/parent::div'
                    rnd_locator_person_name = rnd_locator_person + '/div[2]'
                    # TODO: Verify, on selecting image the name of person's appear
                    chosen_person_name = self.get_element_text(self.find_element((By.XPATH, rnd_locator_person_name)))
                    self.click_element(self.find_element((By.XPATH, rnd_locator_person)))
                    # TODO: Verify in start, on first unsuccessful attempt there is increment of one in tries only.
                    self.tries = str(int(self.tries) + 1)
                    # TODO: Verify, on successful attempt image name and heading name are same.
                    if self.get_attribute(self.find_element((By.XPATH, rnd_locator_person)),
                                          "class") == "photo correct":
                        print(
                            "Correct person selected at " + str(self.bool) + " attempt, which is " + chosen_person_name)
                        time.sleep(5)
                        self.bool = 6
                        # TODO: Verify on first successful attempt there is increment of one in tries,correct and
                        #  streak counts. And Verify, name of person in heading and images change on successful attempt.
                        self.correct = str(int(self.correct) + 1)
                        self.streak = str(int(self.streak) + 1)
                        self.list_rnd.clear()
                    else:
                        # TODO: Verify, when user selects a wrong person after some successful attempts, the streak
                        #  value changes to zero
                        self.streak = 0
                else:
                    self.bool = self.bool

            if self.get_element_text(self.find_element(self.locator_dictionary["tries_count"])) == self.tries:
                if self.get_element_text(self.find_element(self.locator_dictionary["correct_count"])) == self.correct:
                    if self.get_element_text(self.find_element(self.locator_dictionary["streak_count"])) == self.streak:
                        print(
                            "All counts correct: " + self.tries + " tries / " + self.correct + " correct / " + self.streak + " streak")
                        print("--------")
                        continue

    def click_correct_person(self):
        while self.correct != 261:
            given_p = self.get_element_text(self.find_element(self.locator_dictionary["given_person"]))
            correct_p_photo = './/div[text() = "' + given_p + '"]/parent::div'
            # chosen_person = self.get_element_text(self.find_element(self.locator_dictionary["correct_person"]))
            self.click_element(self.find_element((By.XPATH, correct_p_photo)))
            time.sleep(5)
