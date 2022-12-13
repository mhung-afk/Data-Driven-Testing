from helper.base import DDT_edge, handle_datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class B_filter_event(DDT_edge):
    def click_show_more_button(self):
        trial = 0
        while True:
            try:
                button_add = self.driver.find_element(By.XPATH, "//button[contains(text(), \"Show more activities\") or contains(text(),\"Show more courses\")]")
                self.click(button_add)
                break
            except Exception as e:
                self.wait(1)
                # If we have waited for 4 sec but no button, maybe there is just no more event?
                trial += 1
                if trial > 3:
                    break

    def count_event(self):
        event_list = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'timeline-event-list-item')]")
        return len(event_list)

    def filter_event_by_date(self, filter):
        while True:
            try:
                # Scroll to top
                self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                drop_down_list = self.find_ele(By.XPATH, "//button[@title='Filter timeline by date']")
                #drop_down_list = self.find_ele(By.XPATH, "//a[@data-filtername='next7days']")
                self.click(drop_down_list)
                break
            except Exception as e:
                print(e)
                self.wait(1)

        filter_map = {
            "All": "all",
            "Next 7 days": "next7days",
            "Next 30 days": "next30days",
            "Next 3 months": "next3months",
            "Next 6 months": "next6months"
        }

        while True:
            try:
                filter_item = self.find_ele(By.XPATH, f"//a[@data-filtername='{filter_map[filter]}']")
                filter_item.click()
                break
            except Exception as e:
                print(e)
                self.wait(1)

    def sort_events(self, by):
        while True:
            try:
                # Scroll to top
                self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                drop_down_list = self.find_ele(By.XPATH, "//button[@title='Sort timeline items']")
                #drop_down_list = self.find_ele(By.XPATH, "//a[@data-filtername='next7days']")
                self.click(drop_down_list)
                break
            except Exception as e:
                print(e)
                self.wait(1)

        sort_map = {
            "By dates": "sortbydates",
            "By courses": "sortbycourses"
        }

        while True:
            try:
                sort_item = self.find_ele(By.XPATH, f"//a[@data-filtername='{sort_map[by]}']")
                sort_item.click()
                break
            except Exception as e:
                print(e)
                self.wait(1)

    def search_even(self, text):
        while True:
            try:
                box = self.find_ele(By.XPATH, '//*[@id="searchinput"]')
                self.text(box, text)
                break
            except:
                self.wait(1)

    def is_using_sort_mode(self, mode):
        mode_map = {
            "By courses": "view-courses",
            "By dates": "view-dates"
        }

        trial = 0
        while True:
            try:
                event_view = self.driver.find_element(By.XPATH, f"//*[@data-region='{mode_map[mode]}'][contains(@class, 'active')]")
                return "Passed"
            except Exception as e:
                self.wait(1)
                trial += 1
                if trial > 1:
                    return "Failed"