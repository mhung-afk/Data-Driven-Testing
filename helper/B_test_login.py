from helper.base import DDT_edge
from selenium.webdriver.common.by import By


class Test_Login_DDT_edge(DDT_edge):
    def test_login_BKeL(self,record):
        # temp = self.find_ele(By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a')
        # self.click(temp)

        # temp = self.find_ele(By.XPATH, '//*[@id="region-main"]/div/div/div/div/div[3]/a[1]')
        # self.click(temp)
        while True:
            try:
                temp = self.find_ele(By.XPATH, '//*[@id="username"]')
                self.text(temp,record[1])
                self.wait(1)

                temp = self.find_ele(By.XPATH, '//*[@id="password"]')
                self.text(temp,record[2])
                self.wait(1)
        
                temp = self.find_ele(By.XPATH, '//*[@id="fm1"]/div[4]/input[4]')
                self.click(temp)
                self.wait(1)
                break
            except:
                break

    def check_if_success(self):
        while True:
            try:
                homepage = self.find_ele(By.XPATH, '//*[@id="page-site-index"]')
                return True
            except:
                try:
                    error = self.find_ele(By.XPATH, 'document.querySelector("#msg")')
                    return False
                except:
                    self.wait(1)
                
