from helper.B_login import Login_DDT_edge
from helper.B_add_event import Add_Event_DDT_edge

class B_F5_1(Login_DDT_edge, Add_Event_DDT_edge):
    def __init__(self):
        super().__init__("https://e-learning.hcmut.edu.vn/")

    def run(self):    
        self.login_BKeL()

        self.navigate('https://e-learning.hcmut.edu.vn/my/')

        self.click_add_event_btn()

        self.fill_in_add_event()

        self.click_expand_add_event_form()

        self.wait(5)