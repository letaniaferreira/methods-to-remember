from ATM.account import Account


class Bank:

    def __init__(self):
        self.accounts = {}

    def create_account(self, user, pin, account_number):
        """Create an account"""
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(user, pin, account_number)
            return 'Account {} created'.format(account_number)
        else:
            return 'Account number already being used. Check records'

    def get_account(self, account_number):
        """Get account to make deposit or withdrawal"""
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return 'Account {} not found'.format(account_number)

    def close_account(self, account_number):
        """Delete account"""
        if account_number in self.accounts:
            print('Are you sure you want to delete account {}?'.format(account_number))
            del self.accounts[account_number]
            return self.accounts

        else:
            return 'Account {} not found'.format(account_number)


