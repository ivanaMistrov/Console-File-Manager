
import os
import pickle

FILE_NAME = 'orders_pickle.data'

orders = []
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'rb') as f:
        orders = pickle.load(f)

while True:
    print('1. Добавить покупку')
    print('2. История покупок')
    print('3. Выход')
    choise = input('Введите номер: ')
    if choise == '1':
        name = input('Введите название: ')
        cost = int(input('Введите цену: '))
        order = (name, cost)
        orders.append(order)
    elif choise == '2':
        for order in orders:
            print(order)
    elif choise == '3':
        with open(FILE_NAME, 'wb') as f:
            pickle.dump(orders, f)
        break
    else:
        print('Неправильно введены даные')