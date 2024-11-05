"""
FizzBuzz розрахунок
Author: Andrii

Скрипт формує вихідну послідовність, що відповідає властивостям числа n:
якщо число можна поділити на 3 без залишку, замість числа буде виведено Fizz.
якщо число ділиться на 5 без залишку, результат відображатиме Buzz замість числа.
якщо дане число ділиться і на 3, і на 5, замість числа буде надруковано FizzBuzz.
якщо число не можна поділити на 3 або 5, воно буде надруковано в оригіналі.

"""

class FizzBuzz:
    def __init__(self, n):
        self.n = n

    '''
    :param input value - кількість значень для обробки :
    :return list of output Values :
    '''
    def calculate(self):
        finalList = []
        c = int(self.n)
        i = 1
        while i <= c:
            if ( i % 3 == 0 and i % 5 == 0 ):
                finalList.append(str(i) + " - FizzBuzz")
            elif (i % 3 == 0):
                finalList.append(str(i) + " - Fizz")
            elif (i % 5 == 0):
                finalList.append(str(i) + " - Buzz")
            else:
                finalList.append(i)
            i += 1
        return finalList



