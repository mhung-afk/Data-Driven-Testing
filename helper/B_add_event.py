from helper.base import DDT_edge, handle_datetime
from selenium.webdriver.common.by import By

class Add_Event_DDT_edge(DDT_edge):
    def click_add_event_btn(self):
        while True:
            try:
                # add_event_button = self.find_ele(By.XPATH, """//button[text()='
                #     Sự kiện mới
                # ']""")
                add_event_btn = self.find_ele(By.CSS_SELECTOR, 'button.btn.btn-primary.float-sm-right.float-right')
                self.click(add_event_btn)
                break
            except:
                self.wait(1)

    def click_expand_add_event_form(self):
        expand_button = self.find_ele(By.CSS_SELECTOR, 'a.moreless-toggler')
        self.click(expand_button)

    def check_if_success(self):
        self.wait(1)
        try:
            close_btn = self.find_ele(By.CSS_SELECTOR, "button.close[aria-label='Close']")
            self.click(close_btn)
            return False
        except:
            return True

    def fill_in_add_event(self, record):
        print(record)

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

        temp = self.find_ele(By.XPATH, '//*[@id="id_descriptioneditable"]')
        self.text(temp, record[3])
        
        temp = self.find_ele(By.XPATH, '//*[@id="id_location"]')
        self.text(temp, record[4])
            
        if len(record[5]) > 0:
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
            print(str(int(record[6])))
            temp = self.find_ele(By.XPATH, '//*[@id="id_duration_2"]')
            self.click(temp)
            temp = self.find_ele(By.XPATH, '//*[@id="id_timedurationminutes"]')
            self.text(temp, str(int(record[6])))
        else:
            temp = self.find_ele(By.XPATH, '//*[@id="id_duration_0"]')
            self.click(temp)
        
        if len(str(record[7])) > 0:
            print(str(int(record[7])))
            temp = self.find_ele(By.XPATH, '//*[@id="id_repeat"]')
            self.click(temp)
            temp = self.find_ele(By.XPATH, '//*[@id="id_repeats"]')
            self.text(temp, str(int(record[7])))
        
        temp = self.find_ele(By.XPATH, """//button[text()='

            Save
            ']""")
        self.click(temp)