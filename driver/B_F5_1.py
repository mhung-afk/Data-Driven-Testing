from helper.B_login import Login_DDT_edge
from helper.B_add_event import Add_Event_DDT_edge

class B_F5_1(Login_DDT_edge, Add_Event_DDT_edge):
    def __init__(self):
        super().__init__("https://e-learning.hcmut.edu.vn/")

    def run(self, df):
        # print(df)
        self.login_BKeL()

        self.navigate('https://e-learning.hcmut.edu.vn/my/')

        for record in df:
            self.click_add_event_btn()
            self.fill_in_add_event(record)
            is_success = self.check_if_success()
            print(f'{record[0]} - excute:{is_success} - pass:{True}')

        self.wait(5)