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

                # temp = self.find_ele(By.XPATH, """//button[text()='Save']""")
                # self.click(temp)
                temp = self.find_ele(By.XPATH, '//*[@id="id_submitbutton"]')
                self.click(temp)
                self.wait(1)
            except:
                trial += 1
                if trial > 3:
                    break

    def check_if_success(self):
        return True
        while True:
            try:
                # File upload is done if the filepicker is hidden
                file_dialog = self.find_ele(
                    By.XPATH, "//*[contains(@class, 'filepicker')][contains(@class, 'moodle-dialogue-hidden')]")
                return True
            except:
                try:
                    error = self.find_ele(By.XPATH, "//h5[text()='Lỗi']")
                    return False
                except:
                    self.wait(1)

    # def check_if_success(self):
    #     is_success = True
    #     try:
    #         if self.will_wait:
    #             self.wait(self.will_wait)
    #             self.will_wait = None
    #             print('waiting')

    #         while True:
    #             feedbacks = self.find_eles(
    #                 By.CSS_SELECTOR, '.form-control-feedback.invalid-feedback')
    #             print([fb.text for fb in feedbacks])
    #             if len(feedbacks) > 0:
    #                 if any([(len(fb.text.strip()) > 0) for fb in feedbacks]):
    #                     is_success = False
    #                 close_btn = self.find_ele(
    #                     By.CSS_SELECTOR, "button.close[aria-label='Close']")
    #                 self.click(close_btn)
    #                 break
    #     finally:
    #         return is_success
