from helper.base import DDT_edge
from selenium.webdriver.common.by import By


class Filter_My_Courses_DDT_edge(DDT_edge):
    def Fillter_Groupingdropdown(self, data):
        if data == 'N':
            return
        temp = self.find_ele(By.ID, 'groupingdropdown')
        self.click(temp)

        while True:
            try:
                filter = self.find_ele(
                    By.XPATH, f"//a[@data-value='{data}']")
                self.click(filter)
                break
            except:
                self.wait(1)

    def Filter_search(self, data):
        if data == 'N':
            return
        while True:
            try:
                temp = self.find_ele(By.ID, 'searchinput')
                self.text(temp, str(data))
                break
            except:
                self.wait(1)

    def Fillter_Sortingdropdown(self, data):
        if data == 'N':
            return

        temp = self.find_ele(By.ID, 'sortingdropdown')
        self.click(temp)

        while True:
            try:
                filter = self.find_ele(
                    By.XPATH, f"//a[@data-value='{data}']")
                self.click(filter)
                break
            except:
                self.wait(1)

    def filter_my_courses(self, record):
        self.Fillter_Groupingdropdown(str(record[1]))
        self.Fillter_Sortingdropdown(str(record[3]))
        self.Filter_search(str(record[2]))
        self.wait(1)
