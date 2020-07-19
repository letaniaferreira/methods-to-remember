from unittest import TestCase

from ATM.atm import AtmTransaction


class TestAtmTransaction(TestCase):
    def test_make_a_deposit(self):
        t1 = AtmTransaction()
        t1.make_a_deposit(50)
        self.assertEqual(t1.balance, 550)

    def test_make_a_withdrawal(self):
        t2 = AtmTransaction()
        t2.make_a_withdrawal(20)
        self.assertEqual(t2.balance, 480)


    def test_check_balance(self):
        t3 = AtmTransaction()
        t3.check_balance()
        self.assertEqual(t3.balance, 500)
