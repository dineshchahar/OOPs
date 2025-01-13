class Customer:
    """ 
        Represents a customer managing multiple accounts.
        Adheres to SRP by focusing on customer-related actions (e.g, adding accounts)
        
    """
    def __init__(self,customer_id,name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = []
        
    def add_account(self, account):
        self.accounts.append(account)
        
    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
    def show_accounts(self):
        for account in self.accounts:
            print(f"{type(account).__name__}:{account.account_number},Balance:{account.balance}")
        