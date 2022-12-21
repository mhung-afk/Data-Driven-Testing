import time
from pandas import read_excel, DataFrame, ExcelWriter
from selenium.webdriver import Edge, ActionChains
from selenium.webdriver.remote.webelement import WebElement


class DDT_edge:
    driver = None

    def __init__(self, url):
        self.driver = Edge()
        self.driver.maximize_window()
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

    def click_to_ele_with_offset(self, ele: WebElement, x: float, y: float):
        try:
            action = ActionChains(self.driver)
            action.move_to_element_with_offset(ele, x, y).click().perform()
        except:
            raise Exception("Can't click on this element")

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
    
    def scroll_to_ele(self, by, ele: str):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_ele(by, ele)).perform()

    def accpet_refresh(self):
        try:
            a = self.driver.switch_to.alert
            a.accept()
        except:
            return

    def wait(self, secs: float):
        time.sleep(secs)


class Dataframe:
    storage = {}
    loaded_data: DataFrame = None
    excel_file = None
    sheet_name = None
    skiprows = None

    def read_excel(self, io, sheet_name, skiprows=0):
        self.excel_file = io
        self.sheet_name = sheet_name
        self.skiprows = skiprows
        self.loaded_data = read_excel(
            io=io, sheet_name=sheet_name, skiprows=skiprows)
        self.storage[sheet_name] = self.loaded_data.fillna('').to_numpy()
        # print(self.loaded_data)

    def print_df(self):
        print(self.storage)

    def write_result(self, result: list[str]):
        self.loaded_data["Result"] = result
        with ExcelWriter(self.excel_file, mode="a", if_sheet_exists="overlay") as writer:
            self.loaded_data["Result"].to_excel(
                writer, sheet_name=self.sheet_name, startrow=self.skiprows+1, startcol=self.loaded_data.shape[1]-1, header=False, index=False)


def handle_datetime(str: str):
    try:
        [date, time] = str.split(' ')
        [day, month, year] = date.split('/')
        [hour, minute] = time.split(':')
        return [day, month, year, hour, minute]
    except:
        raise Exception("Input doesn't have required datetime format")


def handle_result(is_success: bool):
    return "success" if is_success else "fail"


def handle_resultt(is_success: bool):
    return "Passed" if is_success else "Failed"
