#Private Attributes and methods
class Account:
    def __init__ (self, acc_number, acc_password):
        self.acc_number = acc_number
        self.__acc_password = acc_password

    def reset_pass(self):
        print(self.__acc_password)

acc1 = Account("12345","asdfgh")

print(acc1.acc_number)

print(acc1.reset_pass())