from unittest import TestCase

from ATM.bank import Bank


class TestBank(TestCase):
    def test_create_account(self):
        b1 = Bank()
        self.assertEqual(b1.create_account(1234), 'Account 1234 created')

    def test_cannot_create_duplicate_account(self):
        b1 = Bank()
        b1.create_account(1234)
        self.assertEqual(b1.create_account(1234), 'Account number already being used. Check records')

    def test_cannot_get_account(self):
        b1 = Bank()
        self.assertEqual(b1.get_account(2345), 'Account 2345 not found')

    def test_get_account(self):
        b1 = Bank()
        b1.create_account(1234)
        self.assertEqual(b1.get_account(1234), 1234)
