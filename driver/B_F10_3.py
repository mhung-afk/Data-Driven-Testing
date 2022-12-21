from helper.base import handle_result
from helper.B_test_login import Test_Login_DDT_edge
from selenium.webdriver.common.by import By

class B_F10_3(Test_Login_DDT_edge):
    def __init__(self):
        super().__init__("https://e-learning.hcmut.edu.vn/")
    def run(self,df):
        result = []

        self.navigate(
            'https://sso.hcmut.edu.vn/cas/login?service=https%3A%2F%2Fe-learning.hcmut.edu.vn%2Flogin%2Findex.php%3FauthCAS%3DCAS')
        for record in df:
            self.test_login_BKeL(record)
            is_success = self.check_if_success()
            print(
                f'{record[0]} - expected:{record[3]} - result:{handle_result(is_success)}')
            result += [handle_result(is_success)]

        self.wait(5)

        return result