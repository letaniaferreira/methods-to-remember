class bank:

    def __init__(self):
        self.account = {}

    def create_account(self, account_number):
        if account_number not in self.account:
            self.account['number'] = account_number
        else:
            print('Account number already being used. Check records')
