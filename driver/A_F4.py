from helper.base import handle_result
from helper.A_updateprofile import Update_Profile
from constant import PORT

class A_F4(Update_Profile):
    def __init__(self):
        super().__init__(f"http://localhost:{PORT}/OnlinePizzaDelivery/")
    def run(self,df):
        ini_row = ['ini','quang','nguyen','test@example','0123456789','123456','']
        self.update_profile(ini_row)
        self.check_success()
        result = []

        for record in df:
            self.update_profile(record)
            is_success = self.check_success()
            print(f'{record[0]} - expected:{record[6]} - result:{handle_result(is_success)}')
            result += [handle_result(is_success)]

        self.wait(1)

        return result