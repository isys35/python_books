def action2():
    print(1 + [])  # Генерирует TypeError


def action1():
    try:
        action2()
    except TypeError:  # Самый последний cовпадающий try
        print('inner try')  # внутренний оператор try

try:
    action1()
except TypeError:  # Здесь только в случае повторной генерации исключения в action1
    print('outer try') #  внешний оператор try

