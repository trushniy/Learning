# name = 250
# print(name)
# print(type(name))

# age = int(input('введите число:'))
# print('вот что ты ввел',age,type(age)) 


# result = 3 + 5
# print(result)


# age = 10 
# age = float(age)
# print(age,type(age))


# num4 = int(input('введи что хочешь:'))
# num5 = int(input('тоже что хочешь:'))
# print(num4 * num5,'сложил хуйню',type(num4 + num5))

# usl = 15 > 5 
# print(usl,type(usl)) # бул это правда а условие является булом из бравл старса

# =! числа не равны (10=!10)
# == числа равны (10==10)

# num2 = int(input('число сучара:'))  
# usl = num2 >30 and num2 % 3 == 1  # если номер больше 30 (например 31)то тру но там енд оно работает как * и типо тру и фолс например, то будет 1 * 0 = 0 
# print(usl) 
 
print('пидорас?','ответь 1=да или 0=нет')
num1 = int(input())
if num1 == 1:
    print('понятно все')
elif num1 == 0:
    print('не верю, всё равно пидорас')
else:
    print('в итоге все понятно с тобой')