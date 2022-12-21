from helper.base import DDT_edge, handle_datetime
from selenium.webdriver.common.by import By
from random import random
import math


class B_Create_Subject_DDT_edge(DDT_edge):
    will_wait = None

    def click_crreate_subject_btn(self):
        trial = 0
        while True:
            try:
                create_subject_btn = self.driver.find_element(
                    By.XPATH, "//a[contains(text(), \"Thêm một chủ đề thảo luận mới\") or contains(text(),\"Add discussion topic\")]")
                self.click(create_subject_btn)
                break
            except:
                self.wait(1)
                trial += 1
                if trial > 3:
                    break

    def fill_subject_form(self, record):
        trial = 0
        while True:
            try:
                temp = self.find_ele(By.XPATH, '//*[@id="id_subject"]')
                self.text(temp, record[1])
                self.wait(1)

                temp = self.find_ele(By.XPATH, '//*[@id="id_messageeditable"]')
                self.text(temp, record[2])
                self.wait(1)

                temp = self.find_ele(By.XPATH, '//*[@id="id_submitbutton"]')
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
                error = self.driver.find_element(
                    By.XPATH, "//div[contains(@class, 'show') and contains(@class, 'collapse') and @id='collapseAddForm']")
                return False
            except:
                try:
                    done = self.driver.find_element(
                        By.XPATH, "//div[contains(@class, 'collapse') and @id='collapseAddForm']")
                    return True
                except:
                    trial += 1
                    if trial > 3:
                        return False
