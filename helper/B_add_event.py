from helper.base import DDT_edge, handle_datetime
from selenium.webdriver.common.by import By
from random import random
import math

class Add_Event_DDT_edge(DDT_edge):
    will_wait = None

    def click_add_event_btn(self):
        try:
            add_event_btn = self.find_ele(By.CSS_SELECTOR, 'button.btn.btn-primary.float-sm-right.float-right')
            self.click(add_event_btn)
            tabindex = self.find_ele(By.CSS_SELECTOR, '.modal-dialog.modal-lg.modal-dialog-scrollable').get_attribute('tabindex')
            if tabindex == '-1':
                self.wait(1)
                return False
            return True
        except:
            return False
                
    def click_day_cell(self):
        try:
            day_cells = self.find_eles(By.CSS_SELECTOR, '.day.text-sm-center.text-md-left.clickable.hasevent')
            self.click_to_ele_with_offset(day_cells[math.floor(random() * len(day_cells))], 1, 70)
            tabindex = self.find_ele(By.CSS_SELECTOR, '.modal-dialog.modal-lg.modal-dialog-scrollable').get_attribute('tabindex')
            if tabindex == '-1':
                self.wait(1)
                return False
            return True
        except:
            self.wait(1)
            return False
    
    def click_arrow(self):
        try:
            arrows = self.find_eles(By.CSS_SELECTOR, '.arrow_link')
            self.click(arrows[math.floor(random() * len(arrows))])
            return True
        except:
            return False

    def click_expand_add_event_form(self):
        try:
            expand_button = self.find_ele(By.CSS_SELECTOR, 'a.moreless-toggler')
            self.click(expand_button)
            return True
        except:
            return False

    def check_if_success(self):
        is_success = True
        try:
            if self.will_wait:
                self.wait(self.will_wait)
                self.will_wait = None
            
            while True:
                feedbacks = self.find_eles(By.CSS_SELECTOR, '.form-control-feedback.invalid-feedback')
                if len(feedbacks) > 0:
                    if any([(len(fb.text.strip()) > 0) for fb in feedbacks]):
                        is_success = False
                    close_btn = self.find_ele(By.CSS_SELECTOR, "button.close[aria-label='Close']")
                    self.click(close_btn)
                    break
        finally:
            return is_success

    def fill_in_add_event(self, record):
        while True:
            try:
                temp = self.find_ele(By.XPATH, '//*[@id="id_name"]')
                self.text(temp, record[1])
                break
            except:
                self.wait(1)

        datetime = handle_datetime(record[2])
        temp = self.find_ele(By.ID, 'id_timestart_day')
        self.click(temp)
        temp = self.find_ele(By.XPATH, f'//*[@id="id_timestart_day"]/option[{datetime[0]}]')
        self.click(temp)

        temp = self.find_ele(By.ID, 'id_timestart_month')
        self.click(temp)
        temp = self.find_ele(By.XPATH, f'//*[@id="id_timestart_month"]/option[{datetime[1]}]')
        self.click(temp)
        
        temp = self.find_ele(By.ID, 'id_timestart_year')
        self.click(temp)
        temp = self.find_ele(By.XPATH, f'//*[@id="id_timestart_year"]/option[{int(datetime[2])-1900+1}]')
        self.click(temp)
        
        temp = self.find_ele(By.ID, 'id_timestart_hour')
        self.click(temp)
        temp = self.find_ele(By.XPATH, f'//*[@id="id_timestart_hour"]/option[{int(datetime[3])+1}]')
        self.click(temp)
        
        temp = self.find_ele(By.ID, 'id_timestart_minute')
        self.click(temp)
        temp = self.find_ele(By.XPATH, f'//*[@id="id_timestart_minute"]/option[{int(datetime[4])+1}]')
        self.click(temp)

        self.click_expand_add_event_form()

        while True:
            try:
                temp = self.find_ele(By.XPATH, '//*[@id="id_descriptioneditable"]')
                self.text(temp, record[3])
                break
            except:
                self.wait(1)
        
        temp = self.find_ele(By.XPATH, '//*[@id="id_location"]')
        self.text(temp, record[4])
            
        if len(record[5]) > 0:
            self.will_wait = 5
            until_time = handle_datetime(record[5])
            temp = self.find_ele(By.XPATH, '//*[@id="id_duration_1"]')
            self.click(temp)
            temp = self.find_ele(By.ID, 'id_timedurationuntil_day')
            self.click(temp)
            temp = self.find_ele(By.XPATH, f'//*[@id="id_timedurationuntil_day"]/option[{until_time[0]}]')
            self.click(temp)

            temp = self.find_ele(By.ID, 'id_timedurationuntil_month')
            self.click(temp)
            temp = self.find_ele(By.XPATH, f'//*[@id="id_timedurationuntil_month"]/option[{until_time[1]}]')
            self.click(temp)
            
            temp = self.find_ele(By.ID, 'id_timedurationuntil_year')
            self.click(temp)
            temp = self.find_ele(By.XPATH, f'//*[@id="id_timedurationuntil_year"]/option[{int(until_time[2])-1900+1}]')
            self.click(temp)
            
            temp = self.find_ele(By.ID, 'id_timedurationuntil_hour')
            self.click(temp)
            temp = self.find_ele(By.XPATH, f'//*[@id="id_timedurationuntil_hour"]/option[{int(until_time[3])+1}]')
            self.click(temp)
            
            temp = self.find_ele(By.ID, 'id_timedurationuntil_minute')
            self.click(temp)
            temp = self.find_ele(By.XPATH, f'//*[@id="id_timedurationuntil_minute"]/option[{int(until_time[4])+1}]')
            self.click(temp)
        elif len(str(record[6])) > 0:
            if record[6] == '<null>':
                record[6] = ''
            self.will_wait = 10
            temp = self.find_ele(By.XPATH, '//*[@id="id_duration_2"]')
            self.click(temp)
            temp = self.find_ele(By.XPATH, '//*[@id="id_timedurationminutes"]')
            self.text(temp, record[6])
        else:
            temp = self.find_ele(By.XPATH, '//*[@id="id_duration_0"]')
            self.click(temp)
        
        if len(str(record[7])) > 0:
            if record[7] == '<null>':
                record[7] = ''
            temp = self.find_ele(By.XPATH, '//*[@id="id_repeat"]')
            self.click(temp)
            temp = self.find_ele(By.XPATH, '//*[@id="id_repeats"]')
            self.text(temp, record[7])
        
        temp = self.find_ele(By.XPATH, """//button[text()='

            Save
            ']""")
        self.click(temp)