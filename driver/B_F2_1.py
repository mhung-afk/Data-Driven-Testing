from helper.B_login import Login_DDT_edge
from helper.base import handle_result
from helper.B_upload_assignment import B_upload_assignment
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


import os
cwd = os.getcwd()

class B_F2_1(Login_DDT_edge, B_upload_assignment):
    def __init__(self):
        super().__init__("https://e-learning.hcmut.edu.vn/")

    def run(self, df):
        '''Run and save result to internal buffer'''
        result = []
        self.login_BKeL()
        # self.resolve_item()
        for record in df:
            self.driver.get("https://e-learning.hcmut.edu.vn/mod/assign/view.php?id=42159&action=editsubmission")
            self.click_add_file_button()
            self.fill_file_path(os.path.join(cwd, "test-data", "F2", record[1]))
            self.fill_name_form(record[2])
            self.click_upload()
            is_success = handle_result(self.check_if_success())
            if is_success == "success":
                server_file_name = self.get_server_file_name()

                if is_success == record[3] and server_file_name == record[4]:
                    result += ["Passed"]
                else:
                    result += ["Failed"]
            else:
                server_file_name = "None"
                if is_success == record[3]:
                    result += ["Passed"]
                else:
                    result += ["Failed"]

            print(f'Test {record[0]}: Upload status: {is_success} - Filname on server: {server_file_name} - Result: {result[-1]}')

            # Refresh the page in case of error
            self.driver.refresh()
            try:
                alert = Alert(self.driver)
                alert.accept()
            except NoAlertPresentException:
                continue

        return result




