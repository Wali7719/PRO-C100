class Atm:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 10000  # Initial balance for demonstration purposes

    def display_balance(self):
        print(f"Your account balance is ${self.balance}")

    def cash_withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("PIN successfully changed.")


user_atm = Atm(card_number="1234-5678-9012-3456", pin="1234")


user_atm.display_balance()


user_atm.cash_withdrawal(500)


user_atm.change_pin("4321")
