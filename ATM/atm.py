class AtmTransaction:
    def __init__(self):
        self.balance = 500

    def make_a_deposit(self, deposit_amount):
        self.balance += deposit_amount
        print('You made a deposit in the amount of {}'.format(deposit_amount))

    def make_a_withdrawal(self, withdrawal_amount):
        self.balance -= withdrawal_amount
        print('Withdrawal in the amount of {}'. format(withdrawal_amount))

    def check_balance(self):
        return self.balance


t_1 = AtmTransaction()
print(t_1.balance)
t_1.make_a_deposit(50)
print(t_1.balance)
t_1.make_a_withdrawal(30)
print(t_1.balance)