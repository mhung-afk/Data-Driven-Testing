from helper.base import handle_result
from helper.B_create_subject import B_Create_Subject_DDT_edge
from helper.B_login import Login_DDT_edge
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


import os
cwd = os.getcwd()


class B_F1_1(Login_DDT_edge, B_Create_Subject_DDT_edge):
    def __init__(self):
        super().__init__("https://e-learning.hcmut.edu.vn/")

    def run(self, df):
        # print(df)
        result = []

        self.login_BKeL()

        self.navigate(
            'https://e-learning.hcmut.edu.vn/mod/forum/view.php?id=8740')

        for record in df:
            print('ok\n')
            # self.click_crreate_subject_btn()
            # self.fill_subject_form(record)
            # is_success = self.check_if_success()
            # print(
            #     f'{record[0]} - expected:{record[8]} - result:{handle_result(is_success)}')
            # result += [handle_result(is_success)]
            # # Refresh the page in case of error
            # self.driver.refresh()

        self.wait(5)

        return result
