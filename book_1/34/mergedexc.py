sep = '-' * 45 + '\n'

# Исключения генерируются и перехватываются
print(sep + 'EXCEPTION RAISED AND CAUGHT')
try:
    x = 'spam'[99]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

# Исключения не генерируются
print(sep + 'NO EXCEPTION RAISED')

try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

# Исключения не генерируются c конструкцией else
print(sep + 'NO EXCEPTION RAISED, WITH ELSE')

try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')

# Исключения генерируется, но не перехватывается
print(sep + 'NO EXCEPTION RAISED, WITH ELSE')

try:
    x = 1/0
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')