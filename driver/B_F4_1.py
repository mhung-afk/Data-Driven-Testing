from helper.base import handle_result
from helper.B_forgot_password import B_Forgot_Password_DDT_edge
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


import os
cwd = os.getcwd()


class B_F4_1(B_Forgot_Password_DDT_edge):
    def __init__(self):
        super().__init__("https://e-learning.hcmut.edu.vn/")

    def run(self, df):
        # print(df)
        result = []

        self.navigate(
            'https://account.hcmut.edu.vn/')

        for record in df:
            self.fill_forgot_password_form(record)
            is_success = self.check_if_success()
            print(
                f'{record[0]} - expected:{record[1]} - result:{handle_result(is_success)}')
            result += [handle_result(is_success)]

        self.wait(5)

        return result
