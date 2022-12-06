from helper.base import DDT_edge
from selenium.webdriver.common.by import By
from constant import USERNAME, PASSWORD

class Login_DDT_edge(DDT_edge):
    def login_BKeL(self):
        temp = self.find_ele(By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a')
        self.click(temp)

        temp = self.find_ele(By.XPATH, '//*[@id="region-main"]/div/div/div/div/div[3]/a[1]')
        self.click(temp)

        temp = self.find_ele(By.XPATH, '//*[@id="username"]')
        self.text(temp, USERNAME)

        temp = self.find_ele(By.XPATH, '//*[@id="password"]')
        self.text(temp, PASSWORD)

        temp = self.find_ele(By.XPATH, '//*[@id="fm1"]/div[4]/input[4]')
        self.click(temp)