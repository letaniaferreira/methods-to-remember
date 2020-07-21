class Bank:

    def __init__(self):
        self.account = {}

    def create_account(self, account_number):
        """Create an account"""
        if account_number not in self.account:
            self.account[account_number] = account_number
            return 'Account {} created'.format(account_number)
        else:
            return 'Account number already being used. Check records'

    def get_account(self, account_number):
        """Get account to make deposit or withdrawal"""
        if account_number in self.account:
            return self.account[account_number]
        else:
            return 'Account {} not found'.format(account_number)

    def close_account(self, account_number):
        """Delete account"""
        if account_number in self.account:
            print('Are you sure you want to delete account {}?'.format(account_number))
            del self.account[account_number]
            return self.account

        else:
            return 'Account {} not found'.format(account_number)
