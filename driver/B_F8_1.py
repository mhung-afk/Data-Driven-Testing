from helper.B_login import Login_DDT_edge
from helper.B_filter_my_courses import Filter_My_Courses_DDT_edge
from helper.base import handle_resultt
from selenium.webdriver.common.by import By


class B_F8_1(Login_DDT_edge, Filter_My_Courses_DDT_edge):
    def __init__(self):
        super().__init__("https://e-learning.hcmut.edu.vn/")

    def run(self, df):
        result = []
        self.login_BKeL()

        for record in df:
            self.navigate('https://e-learning.hcmut.edu.vn/my/courses.php')

            is_success = False
            try:
                self.filter_my_courses(record)
                is_success = True
            except:
                is_success = False

            print(
                f'{record[0]} - expected:{record[4]} - result:{handle_resultt(is_success)}')
            result += [handle_resultt(is_success)]

        self.wait(5)

        return result
