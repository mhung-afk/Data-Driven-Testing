from helper.base import DDT_edge
from selenium.webdriver.common.by import By
from random import random
import math

class Delete_Event_DDT_edge(DDT_edge):    
    def click_add_event_btn(self):
        try:
            self.scroll_to_ele(By.CSS_SELECTOR, 'button.btn.btn-primary.float-sm-right.float-right')
            add_event_btn = self.find_ele(By.CSS_SELECTOR, 'button.btn.btn-primary.float-sm-right.float-right')
            self.click(add_event_btn)
            tabindex = self.find_ele(By.CSS_SELECTOR, '.modal-dialog.modal-lg.modal-dialog-scrollable').get_attribute('tabindex')
            if tabindex == '-1':
                self.wait(1)
                return False
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
        self.wait(5)
        is_success = len([ele for ele in self.find_eles(By.CSS_SELECTOR, ".modal-dialog.modal-dialog-scrollable") if ele.get_attribute('tabindex') == '0']) <= 1
        return is_success

    def fill_in_add_event(self, record):
        while True:
            try:
                temp = self.find_ele(By.XPATH, '//*[@id="id_name"]')
                self.text(temp, record[1])
                break
            except:
                self.wait(1)
        
        self.click_expand_add_event_form()
        
        if record[2] == 'T':
            temp = self.find_ele(By.XPATH, '//*[@id="id_repeat"]')
            self.click(temp)
            temp = self.find_ele(By.XPATH, '//*[@id="id_repeats"]')
            self.text(temp, str(2))
        
        temp = self.find_ele(By.XPATH, """//button[text()='

            Save
            ']""")
        self.click(temp)

    def click_event(self, record):
        try:
            self.wait(15)
            events = self.find_eles(By.CSS_SELECTOR, "span.eventname")
            event = [e for e in events if e.get_attribute('innerHTML') == record[1]][0]
            self.click(event)
            return True
        except:
            return False
     
    def click_delete_btn(self):
        try:
            delete_event_btn = [btn for btn in self.find_eles(By.CSS_SELECTOR, "button.btn.btn-secondary") if btn.get_attribute('data-action') == 'delete'][0]
            self.click(delete_event_btn)
            return True
        except:
            self.wait(1)
            return False
    
    def click_confirm_btn(self, record):
        try:
            if record[3] == 'O':
                if record[2] == 'F':
                    confirm_btn = [btn for btn in self.find_eles(By.CSS_SELECTOR, ".btn.btn-primary") if btn.get_attribute('data-action') == 'save' and btn.get_attribute('tabindex') != '-1'][0]
                    # print(confirm_btn)
                    self.click(confirm_btn)
                elif record[2] == 'T':
                    delete_one_event_btn = [btn for btn in self.find_eles(By.CSS_SELECTOR, ".btn.btn-primary") if btn.get_attribute('data-action') == 'deleteone'][0]
                    # print(delete_one_event_btn)
                    self.click(delete_one_event_btn)
            elif record[3] == 'A':
                delete_all_event_btn = [btn for btn in self.find_eles(By.CSS_SELECTOR, ".btn.btn-secondary") if btn.get_attribute('data-action') == 'deleteall'][0]
                # print(delete_all_event_btn)
                self.click(delete_all_event_btn)
            return True
        except:
            self.wait(1)
            return False