from unittest import TestCase

from ATM.account import Account


class TestAccount(TestCase):
    def test_new_account_balance_is_zero(self):
        acc_1 = Account('Joe', 1234, 56578)
        self.assertEqual(acc_1.balance, 0)

    def test_check_balance(self):
        acc_1 = Account('Joe', 1234, 56578)
        self.assertEqual(acc_1.check_balance(), acc_1.balance)

    def test_make_a_deposit(self):
        acc_1 = Account('Joe', 1234, 56578)
        acc_1.make_a_deposit(300)
        self.assertEqual(acc_1.check_balance(), 300)

    def test_make_a_withdrawal(self):
        acc_1 = Account('Joe', 1234, 56578)
        acc_1.make_a_withdrawal(50)
        self.assertEqual(acc_1.check_balance(), -50)
