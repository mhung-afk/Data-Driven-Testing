from helper.B_login import Login_DDT_edge
from helper.B_update_picture import Update_Piicture_DDT_edge
from selenium.webdriver.common.by import By
from helper.base import handle_resultt


class B_F7_1(Login_DDT_edge, Update_Piicture_DDT_edge):
    def __init__(self):
        super().__init__("https://e-learning.hcmut.edu.vn/")

    def run(self, df):
        # print(df)
        result = []
        self.login_BKeL()

        for record in df:
            self.navigate(
                'https://e-learning.hcmut.edu.vn/user/profile.php')
            while True:
                try:
                    temp = self.find_ele(
                        By.XPATH, "// a[contains(text(),'Sửa hồ sơ cá nhân')]")
                    self.click(temp)
                    break
                except:
                    self.wait(1)
            self.updtate_picture(record)
            self.wait(2)
            is_success = False

            if str(record[1]) == "more.png":
                try:
                    self.find_ele(By.XPATH, f'//img[@title="{record[2]}"]')
                    is_success = False
                except:
                    is_success = True
            elif record[2]:
                try:
                    self.find_ele(By.XPATH, f'//img[@title="{record[2]}"]')
                    is_success = True
                except:
                    is_success = False
            else:
                try:
                    self.find_ele(By.XPATH, f'//img[@title="{record[2]}"]')
                    is_success = False
                except:
                    try:
                        self.find_ele(By.XPATH, f'//img[@class="userpicture"]')
                        is_success = True
                    except:
                        is_success = False

            print(
                f'{record[0]} - expected:{record[3]} - result:{handle_resultt(is_success)}')
            result += [handle_resultt(is_success)]

        self.wait(5)

        return result
