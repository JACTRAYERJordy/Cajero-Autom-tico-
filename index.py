# Caso Práctico 3: Simulación de un Cajero Automático
# Un programa que simula las operaciones básicas de un cajero automático, como depositar, retirar y verificar el saldo.

class Account:
    def __init__(self, account_number, balance=0):
        # Inicializa una cuenta con un número de cuenta en este caso es 0
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        # Esta función nos permite depositar una cantidad en la cuenta
        self.balance += amount
        print(f"Se depositaron ${amount}. Nuevo saldo: ${self.balance}")

    def withdraw(self, amount):
        # Aquí se puede retirar una cantidad de la cuenta
        if amount > self.balance:
            print("Fondos insuficientes.")
        else:
            self.balance -= amount
            print(f"Se retiraron ${amount}. Nuevo saldo: ${self.balance}")

    def check_balance(self):
        # Se encarga de verificar el saldo de la cuenta
        print(f"Saldo actual: ${self.balance}")

class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_deposit=0):
        # Crea una cuenta nueva con un número de cuenta
        if account_number in self.accounts:
            print("La cuenta ya existe.")
        else:
            self.accounts[account_number] = Account(account_number, initial_deposit)
            print(f"Cuenta {account_number} creada con un saldo de ${initial_deposit}")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

# Ejemplo de uso
atm = ATM()
atm.create_account("YACTRAYER12345", 1000)  # Crear una cuenta con número "YACTRAYER12345" y un depósito inicial de 100
account = atm.get_account("YACTRAYER12345")  # Obtener la cuenta con número "YACTRAYER12345"

# Realizar operaciones en la cuenta
if account:
    # Muestra el monto depositado
    account.deposit(50)
    # Muestra cuanto se rerira de la cuenta
    account.withdraw(30)
    # Verificamos el saldo de la cuenta 
    account.check_balance() 
