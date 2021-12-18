# Дебильный калькулятор v2

from colorama import init
from colorama import Fore, Back, Style

init()

print( Fore.BLACK )
print( Back.GREEN )

what = input('Что делаем? (+, -, *, /): ')

a = float(input('Введи первое число: '))
b = float(input('Введи второе число: '))

if what == '+':
    c = a + b
    print( Back.YELLOW )
    
    print('Результат: ' + str(c))
elif what == '-':
    c = a - b
    print('Результат: ' + str(c))
elif what == '*':
    c = a * b
    print('Результат: ' + str(c))
elif what == '/':
    c = a / b
    print('Результат: ' + str(c))
else:
    print('Ты ввел неверную операцию, дурилка')
    
   
