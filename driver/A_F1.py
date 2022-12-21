from helper.base import handle_result
from helper.A_signup import Sign_Up
from constant import PORT


class A_F1(Sign_Up):
    def __init__(self):
        super().__init__(f"http://localhost:{PORT}/OnlinePizzaDelivery/")

    def run(self, df):
        ini_row = ['ini', 'hung', 'initial', 'data',
                   'test@example', '0123456789', '123456', '123456', '']
        self.sign_up(ini_row)
        self.check_if_success()

        result = []

        for record in df:
            self.sign_up(record)
            is_success = self.check_if_success()
            print(
                f'{record[0]} - expected:{record[8]} - result:{handle_result(is_success)}')
            result += [handle_result(is_success)]

        self.wait(1)

        return result
