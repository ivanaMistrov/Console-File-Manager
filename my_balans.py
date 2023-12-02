class User:
    def __init__(self, name):
        self.name = [name]
        self.balance = 0

    def load_balance(self):
        try:
            with open('balances.txt', 'r' ) as file:
                for line in file:
                    user_name = line.strip().split(':')
                    if user_name == self.name:
                        self.balance = int(balance)
                        break
        except FileNotFoundError:
            pass

    def save_balance(self):
        with open('balances.txt', 'a') as file:
            file.write(f"{self.name}balanc:{self.balance}\n")

    def up_balance(self, amount):
        self.balance += amount


def menu():
    nam = input("Введите имя: ")
    user = User(nam)

    user.save_balance()
    if user.balance == 0:
        print("Имя не найдено, создаем нового пользователя.")

    else:
        print(f"Привет, {user.name}! Твой текущий баланс: {user.balance}")

    choice = input("Хотите пополнить баланс? (да/нет): ")
    if choice.lower() == 'да':
        amount = int(input("Введите сумму пополнения: "))
        user.up_balance(amount)
        user.save_balance()
        print(f"Баланс успешно пополнен. Твой текущий баланс: {user.balance}")




