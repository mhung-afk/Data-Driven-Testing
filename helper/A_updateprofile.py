from helper.base import DDT_edge
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Update_Profile(DDT_edge):
    def update_profile(self, record):
        while True:
            try:
                temp = self.find_ele(By.XPATH, '//*[@id="firstName"]')
                self.text(temp, record[1])
        
                temp = self.find_ele(By.XPATH, '//*[@id="lastName"]')
                self.text(temp, record[2])

                temp = self.find_ele(By.XPATH, '//*[@id="email"]')
                self.text(temp, record[3])

                temp = self.find_ele(By.XPATH, '//*[@id="phone"]')
                self.text(temp, record[4])
        
                temp = self.find_ele(By.XPATH, '//*[@id="password"]')
                self.text(temp, record[5])
                break
            except:
                break
    def check_success(self):
        while True:
            try:
                is_success = True
                temp = self.find_ele(By.XPATH, '/html/body/div[3]/div/div[2]/div/form/button')
                self.click(temp)
                alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present)
                alert_text = alert.text
                alert.accept()
                if alert_text == ("Update failed, please try again.") or alert_text == ("Password is incorrect."): 
                    is_success = False
                else: is_success = True
                return is_success
            except:
                self.wait(0.5)
