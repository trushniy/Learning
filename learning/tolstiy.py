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

# =! числа не равны (10=!11)
# == числа равны (10==10)

# num2 = int(input('число сучара:'))  
# usl = num2 >30 and num2 % 3 == 1  # если номер больше 30 (например 31)то тру но там енд оно работает как * и типо тру и фолс например, то будет 1 * 0 = 0 
# print(usl) 
 
# print('пидорас?','ответь 1=да или 0=нет')
# num1 = int(input())
# if num1 == 1:
#     print('понятно все')
# elif num1 == 0:
#     print('не верю, всё равно пидорас')
# else:
#     print('в итоге все понятно с тобой')

# print('введите число,второе число,знак')
# num1 = int(input())
# num2 = int(input())
# str = input('введи знак')
# if str == '+':
#    print(num1 + num2)
# elif str == '/':
#    print(num1 / num2)
# elif str == '*': 
#    print(num1 * num2)
# elif str == '-':
#    print(num1 - num2)
# elif str == '**':
#    print(num1 ** num2)
# elif str == '%':
#    print(num1 % num2)
# else:
#    print('не дели на ноль')

# num11 = 1000

# while num11 > -2:
#    print(num11)
#    num11 = num11 - 7
#    import time
# time.sleep(15)

# str = 'poka' # вот так for работает, перебирает буквы в словах типо пока будет п о к а
# for i in str:
#    print(i) 

# range(начало. конец. шаг) пример:
# for i in range(0,21,5):
#    print(i)

# len(строка) - сколько символов строке столько цифр
# str15 = 'pisunbobra'
# for l in range(len(str15)):
#     print(l)

# #def- функция, короче когда лень одно и тоже писать в коде деф делаешь оно пишет как то по уебанскому (пример:)
# def print_hello(name,age):
#    print('твое имя:',name,'твой возраст:',age)
# print_hello("собака",10)
# print_hello("кошка",20)

# def sumstr(str1,str2):
#    result = (str1 + str2)
#    return result

# st1 = "ты"
# st2 = "дурак"

# print(sumstr(st1,st2)) #ура получилась ты дурак!!!

# class User:
#    def __init__(self, name, age, password):
#       self.name = name
#       self.age = age
#       self.password = password
   
#    def print_user(self):
#       print('Имя:', self.name, 'Возраст:', self.age, 'Пароль:', self.password)

# user61 = User('Egor', 13, 'Kirill')
# user61.print_user()

class user:
   def __init__(self,name2,height,fat,weight):
      self.name = name2
      self.height = height
      self.fat = fat
      self.weight = weight
   def print_user(self):
      print('имя:',self.name,',рост:',self.height,',толстый?',self.fat,'и сколько вес?',self.weight)

user21 = user('maks',150,'yes',1500)
user190 = user('messenger',290,'no',10)

user21.print_user()
user190.print_user()
