class Account:

    def __init__(self, user, pin, number):
        self.user = user
        self.pin = pin
        self.number = number
        self.balance = 0

    def check_balance(self):
        return self.balance

    def make_a_deposit(self, deposit_amount):
        self.balance += deposit_amount
        print('You made a deposit in the amount of {}'.format(deposit_amount))

    def make_a_withdrawal(self, withdrawal_amount):
        self.balance -= withdrawal_amount
        print('Withdrawal in the amount of {}'. format(withdrawal_amount))