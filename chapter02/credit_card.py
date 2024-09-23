class CreditCard:
    def __init__(self, customer: str, bank: str, acnt: str, limit: int) -> None:
        """Create a new credit card instance

        The initial balance is zero

        customer the name of the customer(e.g 'John Bowman')
        bank     the name of the bank (e.g 'California Savings')
        acnt     the account identifie (e.g, '5391 0375 9387 5309')
        limit    credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self) -> str:
        """Return name of the customer"""
        return self._customer

    def get_bank(self) -> str:
        return self._bank

    def get_account(self) -> str:
        """Return the card identifying number (typically stored as a string)"""
        return self._account

    def get_limit(self) -> int:
        """Return Current credit limit"""
        return self._limit

    def get_balance(self) -> int:
        """Return current balance"""
        return self._balance

    def charge(self, price) -> int:
        """
        Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:  # if charge would exceed limit
            return False  # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balances"""
        self._balance -= amount

    # def __len__(self):
    #     return self._balance


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees"""

    def __init__(
        self, customer: str, bank: str, acnt: str, limit: int, apr: float
    ) -> None:
        """
        Create new predetory credit card instance.

        The initial balance is zero

        customer  the name of the customer (e.g 'John Bowman')
        bank      the name of the bank (e.g California Savings')
        acnt      the account identifier (e.g '5391 0275 9387 5309')
        limit     credit limit (measured in dollars)
        apr       annual percentage rate (e.g 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    
    def charge(self, price: float):
        """
        Charge given price to the card, assuming sufficient credit limit

        Return True if charge was processed
        Return False and assess $5 fee if charge is denied
        """
        success = super().charge(price)
        if not success:
            self._balance += 5 # assess penalty
        return success # caller expects return value
    
    def process_month(self):
        """Access monthly interest on outstanding balance"""
        if self._balance > 0:
            # if positive balance covert APR to monthly multipicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
if __name__ == "__main__":
    wallet = [
        CreditCard("John Bowman", "Carlifornia Savings", "5391 0375 9387 2500", 2500),
        CreditCard("John Bowman", "Carlifornia Federal", "3486 0399 3500", 3500),
        CreditCard("John Bowman", "Carlifornia Finance", "5391 0375 9387 5309", 5000),
    ]

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * 3)
        wallet[2].charge(3 * val)


for c in range(3):
    print("Customer =", wallet[c].get_customer())
    print("Bank = ", wallet[c].get_bank())
    print("Account = ", wallet[c].get_account())
    print("Balance = ", wallet[c].get_balance())
    while wallet[c].get_balance() > 100:
        wallet[c].make_payment(100)
        print("New balance = ", wallet[c].get_balance())
    print()
