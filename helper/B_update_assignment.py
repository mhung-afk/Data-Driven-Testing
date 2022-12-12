from helper.base import DDT_edge, handle_datetime
from selenium.webdriver.common.by import By

class B_update_assignment(DDT_edge):
    def click_add_file_button(self, xpath):
        while True:
            try:
                button_add = self.find_ele(By.XPATH, xpath)
                self.click(button_add)
                break
            except:
                self.wait(1)

    def fill_file_path(self, xpath, file_path):
        while True:
            try:
                file_form = self.find_ele(By.XPATH, xpath)
                self.text(file_form, file_path)
                break
            except:
                self.wait(1)

    def fill_name_form(self, xpath, name):
        while True:
            try:
                name_form = self.find_ele(By.XPATH, xpath)
                self.text(name_form, name)
                break
            except:
                self.wait(1)

    def click_upload(self, xpath):
        while True:
            try:
                button = self.find_ele(By.XPATH, xpath)
                self.click(button)
                break
            except:
                self.wait(1)

    def check_if_success(self, xpath):
        try:
            error = self.find_ele(By.XPATH, xpath)
            return False
        except:
            return True