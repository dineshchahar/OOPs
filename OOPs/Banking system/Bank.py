class Bank:
    """
        Manages customers and their accounts.
        Adheres to SRP by focusing on bank-level operations (e.g., adding customer, transfers)
         
    """

    def __init__(self,name):
        self.name = name
        self.customers = {}
    
    def add_customer(self,customer):
        if customer.customer_id not in self.customers:
            self.customers[customer.customer_id] = customer
        else:
            raise Exception("Customer already exists")
    
    def transfer_balance(self, sender_id, sender_account_number, receiver_id, receicer_account_number,amount):
        sender = self.customers.get(sender_id)
        receiver = self.customers.get(receiver_id)
        
        if not sender or not receiver:
            raise Exception("Invalid sender or receiver.")
        sender_account = sender.get_account(sender_account_number)
        receicer_account = receiver.get_account(receicer_account_number)
        if sender_account and receicer_account:
            sender_account.withdraw(amount)
            receicer_account.deposit(amount)
            