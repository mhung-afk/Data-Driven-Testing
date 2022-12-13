from helper.B_login import Login_DDT_edge
from helper.B_add_event import Add_Event_DDT_edge
from helper.base import handle_result

class B_F5_3(Login_DDT_edge, Add_Event_DDT_edge):
    def __init__(self):
        super().__init__("https://e-learning.hcmut.edu.vn/")

    def fill_in_add_event(self, record):
        super().fill_in_add_event(record[2:])


    def run(self, df):
        # print(df)
        result = []

        self.login_BKeL()

        self.navigate('https://e-learning.hcmut.edu.vn/my/')

        for record in df:
            passed = False
            if record[1] == 'x':
                while not passed:
                    passed = self.click_arrow()
            
            passed = False
            if record[2] == 'cell':
                while not passed:
                    passed = self.click_day_cell()
            elif record[2] == 'button':
                while not passed:
                    passed = self.click_add_event_btn()

            self.fill_in_add_event(record)
            is_success = self.check_if_success()
            print(f'{record[0]} - expected:{record[10]} - result:{handle_result(is_success)}')
            result += [handle_result(is_success)]

        self.wait(5)

        return result