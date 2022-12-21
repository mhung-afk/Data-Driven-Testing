from helper.base import DDT_edge, handle_datetime
from selenium.webdriver.common.by import By
from random import random
import math


class B_Forgot_Password_DDT_edge(DDT_edge):
    will_wait = None

    def fill_forgot_password_form(self, record):
        trial = 0
        while True:
            try:

                temp = self.find_ele(By.XPATH, '//*[@id="login"]')
                self.text(temp, record[1])
                self.wait(1)

                temp = self.find_ele(By.XPATH, '//*[@id="oldpassword"]')
                self.text(temp, record[2])
                self.wait(1)

                temp = self.find_ele(By.XPATH, '//*[@id="newpassword"]')
                self.text(temp, record[3])
                self.wait(1)

                temp = self.find_ele(By.XPATH, '//*[@id="confirmpassword"]')
                self.text(temp, record[4])
                self.wait(1)

                # temp = self.find_ele(By.XPATH, """//button[text()='Save']""")
                # self.click(temp)
                temp = self.find_ele(
                    By.XPATH, '//button[@class="btn btn-success"]')
                self.click(temp)
                self.wait(1)
                break
            except:
                trial += 1
                if trial > 3:
                    break

    def check_if_success(self):
        trial = 0
        while True:
            try:
                file_dialog = self.find_ele(
                    By.XPATH, "//div[contains(@class, 'alert-success')]")
                return True
            except:
                trial += 1
                if trial > 3:
                    return False
