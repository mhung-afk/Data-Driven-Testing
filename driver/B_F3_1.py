from helper.B_login import Login_DDT_edge
from helper.base import handle_result
from helper.B_filter_event import B_filter_event
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

import os
cwd = os.getcwd()

class B_F3_1(Login_DDT_edge, B_filter_event):
    def __init__(self):
        super().__init__("https://e-learning.hcmut.edu.vn/")

    def run(self, df):
        '''Run and save result to internal buffer'''
        result = []
        self.login_BKeL()
        # self.resolve_item()
        for record in df:
            self.driver.get("https://e-learning.hcmut.edu.vn/my/")
            self.wait(3)    # 3 sec is too long?
            self.filter_event_by_date("All")
            self.wait(3)
            self.click_show_more_button()
            self.wait(3)
            all_events_num = self.count_event()

            self.filter_event_by_date(record[1])
            self.wait(3)
            self.sort_events(record[2])
            self.wait(3)
            self.search_even(record[3])
            self.wait(3)

            filtered_events_num = self.count_event()
            # print(filtered_events_num)

            # Test if events have been filtered
            if record[4] == "Yes" and filtered_events_num <= all_events_num:
                filter_event_test = "Passed"
            elif record[4] == "No" and filtered_events_num == all_events_num:
                filter_event_test = "Passed"
            else:
                filter_event_test = "Failed"

            # Test if the correct sort mode is used
            sort_test = self.is_using_sort_mode(record[5])

            if filter_event_test == "Passed" and sort_test == "Passed":
                result += ["Passed"]
            else:
                result += ["Failed"]

            print(f'Test {record[0]}: Filter event test: {filter_event_test} - Sort mode test: {sort_test} - Result: {result[-1]}')


        return result




