from helper.base import DDT_edge
from selenium.webdriver.common.by import By

class Add_Event_DDT_edge(DDT_edge):
    def click_add_event_btn(self):
        add_event_button = self.find_ele(By.CSS_SELECTOR, 'button.btn.btn-primary.float-sm-right.float-right')
        self.click(add_event_button)
        self.wait(1)

    def click_expand_add_event_form(self):
        expand_button = self.find_ele(By.CSS_SELECTOR, 'a.moreless-toggler')
        self.click(expand_button)

    def fill_in_add_event(self):
        print(self.data)
        # name_inp = DDT.find_ele(By.XPATH, '//*[@id="id_name"]')
        # DDT.text(name_inp, 'ass')

        # datetime = handle_datetime('15/06/1975 11:59')
        # timestart_day_inp = DDT.find_ele(By.ID, 'id_timestart_day')
        # DDT.click(timestart_day_inp)
        # opt_timestart_day_inp = DDT.find_ele(By.XPATH, f'//*[@id="id_timestart_day"]/option[{datetime[0]}]')
        # DDT.click(opt_timestart_day_inp)