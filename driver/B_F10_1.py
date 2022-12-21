from helper.base import handle_result
from helper.B_test_login import Test_Login_DDT_edge
from selenium.webdriver.common.by import By

class B_F10_1(Test_Login_DDT_edge):
    def __init__(self):
        super().__init__("https://e-learning.hcmut.edu.vn/")
    def run(self,df):
        result = []

        temp = self.find_ele(By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a')
        self.click(temp)

        for record in df:
            if record[1] == 'Student':
                self.navigate(
                'https://sso.hcmut.edu.vn/cas/login?service=https%3A%2F%2Fe-learning.hcmut.edu.vn%2Flogin%2Findex.php%3FauthCAS%3DCAS')
                self.test_login_BKeL(record)
                is_success = self.check_if_success()
                print(
                    f'{record[0]} - expected:{record[3]} - result:{handle_result(is_success)}')
                result += [handle_result(is_success)]

                self.wait(5)
            else:
                homepage = self.find_ele(By.XPATH, '//*[@id="loginguestbtn"]')
                self.click(homepage)
                result += [handle_result(True)]
            return result
