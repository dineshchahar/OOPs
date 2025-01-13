from .account import Account

class SavingAccount(Account):
    """
        Represents a saving account with tiered interest rates.
        adheres  to the liskov substitution Principle (LSP) by extending the Account with altering o9t
    """
    
    def calculate_interest(self):
        if self.balance < 5000:
            rate = 0.03
        elif self.balance <10000:
            rate = 0.05
        else:
            rate = 0.07
        return self.balance * rate