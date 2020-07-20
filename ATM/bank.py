class Bank:

    def __init__(self):
        self.account = {}

    def create_account(self, account_number):
        if account_number not in self.account:
            self.account[account_number] = account_number
            return 'Account {} created'.format(account_number)
        else:
            return 'Account number already being used. Check records'

    # def get_account(self):
    #     """Get account to make deposit or withdrawal"""
    #
    #
    # def close_account(self):