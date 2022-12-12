from helper.base import DDT_edge, handle_datetime
from selenium.webdriver.common.by import By

class B_upload_assignment(DDT_edge):
    def click_add_file_button(self):
        while True:
            try:
                button_add = self.find_ele(By.XPATH, "//a[@title=\"Thêm...\"]")
                self.click(button_add)
                break
            except:
                self.wait(1)

    def fill_file_path(self, file_path):
        while True:
            try:
                file_form = self.find_ele(By.XPATH, "//input[@name=\"repo_upload_file\"]")
                self.text(file_form, file_path)
                break
            except:
                self.wait(1)

    def fill_name_form(self, name):
        while True:
            try:
                name_form = self.find_ele(By.XPATH, "//input[@class=\"form-control\"][@name=\"title\"]")
                self.text(name_form, name)
                break
            except:
                self.wait(1)

    def click_upload(self):
        while True:
            try:
                button = self.find_ele(By.XPATH, "//*[@class=\"fp-upload-btn btn-primary btn\"]")
                self.click(button)
                break
            except:
                self.wait(1)

    def check_if_success(self):
        while True:
            try:
                # File upload is done if the filepicker is hidden
                file_dialog = self.find_ele(By.XPATH, "//*[contains(@class, 'filepicker')][contains(@class, 'moodle-dialogue-hidden')]")
                return True
            except:
                try:
                    error = self.find_ele(By.XPATH, "//h5[text()='Lỗi']")
                    return False
                except:
                    self.wait(1)

    def get_server_file_name(self):
        while True:
            try:
                span_tag = self.find_ele(By.XPATH, "//*[@id=\"ygtvcontentel4\"]/span/a[1]/span[4]")
                return span_tag.text
            except:
                self.wait(1)