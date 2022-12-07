import time
from pandas import read_excel
from selenium.webdriver import Edge
from selenium.webdriver.remote.webelement import WebElement

class DDT_edge:
    driver = None

    def __init__(self, url):
        self.driver = Edge()
        self.driver.get(url)

    def find_ele(self, by, ele: str):
        try:
            return self.driver.find_element(by, ele)
        except:
            raise Exception("Can't get this element")

    def find_eles(self, by, ele: str):
        try:
            return self.driver.find_elements(by, ele)
        except:
            raise Exception("Can't get these elements")

    def click(self, ele: WebElement):
        try:
            ele.click()
        except:
            raise Exception("Can't click on this element")

    def text(self, ele: WebElement, text: str):
        try:
            ele.clear()
            ele.send_keys(text)
        except:
            raise Exception("Can't send text into this element")

    def navigate(self, url: str):
        self.driver.get(url)

    def wait(self, secs: float):
        time.sleep(secs)

class Dataframe:
    storage = {}

    def read_excel(self, io, sheet_name, skiprows):
        loaded_data = read_excel(io=io, sheet_name=sheet_name, skiprows=skiprows)
        self.storage[sheet_name] = loaded_data.fillna('').to_numpy()
    
    def print_df(self):
        print(self.storage)


def handle_datetime(str: str):
    try:
        [date, time] = str.split(' ')
        [day, month, year] = date.split('/')
        [hour, minute] = time.split(':')
        return [day, month, year, hour, minute]
    except:
        raise Exception("Input doesn't have required datetime format")