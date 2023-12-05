import os
import pickle


class User:
    def __init__(self,name):
        self.name = name
        self.balance = 0

    def load_balance(self):
        try:
            with open('balances.txt', 'r' ) as file:
                for lin in file:
                    name = lin.strip().split(':')
                    if name[0] == self.name:
                        self.balance = int(self.balance)
                        break
        except FileNotFoundError:
            pass

    def save_balance(self):
        with open('balances.txt', 'a') as file:
            file.write(f"{self.name}:{self.balance}\n")

    def up_balance(self, amount):
        self.balance += amount

def menu():
    my_bills = {}

    name = input('Введите имя ')
    user = User(name)
    if os.path.exists('balances.txt''a'):
        with open('balances.txt', 'r' ) as file:
            for lin in file:
                return lin

    if name in my_bills:
        print(f"Привет, {user.name}! Твой текущий баланс: {user.balance}")
    else:
        print("Имя не найдено, создаем нового пользователя.")
        new_bill = User(name)
        my_bills[name] = new_bill

    choice = input("Хотите пополнить баланс? (yes/no): ")

    if choice.lower() == 'yes':
        amount = int(input("Введите сумму пополнения: "))
        user.up_balance(amount)
        user.save_balance()
        print(f"Баланс успешно пополнен {user.name},  текущий баланс: {user.balance}")
        print(my_bills)


menu()
