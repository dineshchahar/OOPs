from .current_account import CurrentAccount

class BusinessAccount(CurrentAccount):
    """
        Represents a Business Account with heigher overdraft limits.
        Extends the CurrentAccount while adhering the to OCP and LSP principles. 
    """
    
    def __init__(self, account_number, balance=0, overdraft_limit=5000):
        super().__init__(account_number, balance, overdraft_limit)