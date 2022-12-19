from helper.base import DDT_edge
from selenium.webdriver.common.by import By

class Sign_Up(DDT_edge):
    def check_if_success(self):
        while True:
            try:
                is_success = True
                style = self.find_ele(By.ID, 'signupModal').get_attribute('class')
                if style == 'modal fade':
                    warn = self.find_ele(By.XPATH, '/html/body/div[3]').get_attribute('class')
                    if warn == 'alert alert-warning alert-dismissible fade show':
                        is_success = False
                else:
                    is_success = False
                    close_btn = self.find_ele(By.XPATH, '//*[@id="signupModal"]/div/div/div[1]/button')
                    self.click(close_btn)
                return is_success
            except:
                self.wait(0.5)

    def sign_up(self, record):
        print(record)

        while True:
            try:
                temp = self.find_ele(By.XPATH, '//*[@id="navbarSupportedContent"]/button[2]')
                self.click(temp)
                style = self.find_ele(By.ID, 'signupModal').get_attribute('style')
                if style == 'display: none;':
                    self.wait(0.5)
                else:
                    break
            except:
                self.wait(0.5)

        while True:
            try:
                temp = self.find_ele(By.XPATH, '//*[@id="username"]')
                self.text(temp, record[1])
                break
            except:
                self.wait(0.5)

        temp = self.find_ele(By.XPATH, '//*[@id="firstName"]')
        self.text(temp, record[2])
        
        temp = self.find_ele(By.XPATH, '//*[@id="lastName"]')
        self.text(temp, record[3])

        temp = self.find_ele(By.XPATH, '//*[@id="email"]')
        self.text(temp, record[4])

        temp = self.find_ele(By.XPATH, '//*[@id="phone"]')
        self.text(temp, record[5])
        
        temp = self.find_ele(By.XPATH, '//*[@id="password"]')
        self.text(temp, record[6])
        
        temp = self.find_ele(By.XPATH, '//*[@id="cpassword"]')
        self.text(temp, record[7])

        temp = self.find_ele(By.XPATH, '//*[@id="signupModal"]/div/div/div[2]/form/button')
        self.click(temp)