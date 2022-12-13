from helper.B_login import Login_DDT_edge
from helper.upload_my_file import Upload_My_File_DDT_edge
from helper.base import handle_resultt
from selenium.webdriver.common.by import By


class B_F9_1(Login_DDT_edge, Upload_My_File_DDT_edge):
    def __init__(self):
        super().__init__("https://e-learning.hcmut.edu.vn/")

    def run(self, df):
        result = []
        self.login_BKeL()

        for record in df:
            self.navigate('https://e-learning.hcmut.edu.vn/user/files.php')
            self.accpet_refresh()
            self.wait(1)
            self.upload_my_file(record)
            self.wait(1)

            is_success = False

            if str(record[2]) == 'N' or str(record[4]) == 'N':
                try:
                    item = self.find_ele(
                        By.XPATH, f'//div[text()="{record[1]}"]')
                    is_success = True
                except:
                    is_success = False
            else:
                try:
                    item1 = self.find_ele(
                        By.XPATH, f'//div[text()="{record[1]}"]')
                    item2 = self.find_ele(
                        By.XPATH, f'//div[text()="{record[2]}"]')
                    is_success = True
                except:
                    is_success = False
            print(
                f'{record[0]} - expected:{record[5]} - result:{handle_resultt(is_success)}')
            result += [handle_resultt(is_success)]

        self.wait(5)

        return result
