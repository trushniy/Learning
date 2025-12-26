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

# class user:
#    def __init__(self,name2,height,fat,weight):
#       self.name = name2
#       self.height = height
#       self.fat = fat
#       self.weight = weight
#    def print_user(self):
#       print('имя:',self.name,',рост:',self.height,',толстый?',self.fat,'и сколько вес?',self.weight)

# user21 = user('maks',150,'yes',1500)
# user190 = user('messenger',290,'no',10)

# user21.print_user()
# user190.print_user()


# str2 = "Egorultramegasuperdota2" # [начало,конец,шаг]
# print(str2[0:4])                   # [начало,конец]
#                                     # [номер]
# lastindex = str2[-5]
# print(lastindex)   = Ищет так же только с концав

# str10 = "1230031023002401401285167445717571257166923487126577"
# print(str10.find('2')) #первая цифра
# print(str10.rfind('2')) #последняя цифра
# print(str10.index('f')) #ОШИБКА,find бы так не поступила
# print(str10.rindex('5')) # тоже самое что find and rfind, только ошибку выдает если что  


# strpisya = "HUILO"
# strpisya = strpisya.lower() lower= низкие буквы
# print(strpisya)

# strpopa = "hUilOO"         
# strpopa = strpopa.upper()      upper= большие буквы
# print(strpopa)

#replace что заменить,на что заменить,сколько раз
# strkaka = '101000101000'
# strkaka = strkaka.replace('0','*',5)
# print(strkaka)

#append(x)
# list1 = [1,2,3,4,5]
# list1.append(104)
# #remoe(x)

# list1.remove(5)
# print(list1)

#insert(i,x) del[i] insert как append только вставляет куда хочешь
# делит как ремув только ищет по индексу а не по числу
# list2 = [0,1,2,4,6,8,2,0,2,4]
# list2.insert(4,"hello")
# del list2[4]
# print(list2)

#метод сорт (sort), сортирует список 
# lst = [15,25,612,643,1267,5,1,4]
# lst.sort()
# print(lst)
#чтобы сделать по убыванию пишем = lst.sort(reverse = True)

# str1.split = может из строки сделать список например:
# str1 = '1!2!3!4!5!6!7'
# lst = str1.split("!")
# print(lst)

# dict = {'name':'Egor','age':150} #dict = ключ-значение 
# dict['password'] = 'password1'  # можно добавить
# del dict['name'] #можно удалить
# print(dict) 

#dict2 = dict(name = 'Egor',age=150,password='password1') # 2 вариация dict
# print(list(dict2.keys())) # можно посмотреть ключи = name,age,password
# print(list(dict2.values())) # можно посмотреть значения = Egor,150,password1
# print(list(dict2.items())) # и ключи и значения
# print(dict2.get('name')) # получает ключи 
# print(dict2.pop('name')) # удаляет и возвращает 


# МНОЖЕСТВА!!!
# list = [1,2,76,3,6,5,1,5,12,5,56,8,8,34,356]
# set1 = set(list)
# print(set1)

# set2 = set()
# set2.add('s')
# print(set2)

# friz = frozenset('fawatafashnelepepe')
# print(list(friz))

# open(путь,режим)r w 
# file = open('learning\Test.txt')
# test = file.read() #read- считывает ваш файл
# test = file.readline() # test42 = file42.readline() # считывает строчку
# test = file.readlines()# test42 = file42.readlines() # считывает строчки
# print(test)

# file = open('learning\Test.txt','r')
# list = []
# for i in file:
#    list.append(i)
# print(list) 
# file.close()

# with open('learning\Test.txt','w')as f:
#    f.write('ura 12')

# try: # попробует выполнить 
#    file = open('learning\Test.txt','r')
#    file.write('25')
# except Exception as e: # если ошибка то выйдет это = print('не получилось')
#    print('не получилось',e)
# finally:
#    file.close()
#    print('file closed') 

#импорт 
# def print_age(age):
#    print('тебе:',age)

#lambda
funciya = lambda x,y : x*y
print(funciya(10,150))

#map делает из списка str в список int
# list0 = ['123','1125','9651','15','17','192']
# list0 = list(map(int,list0))
# print(list0)

# list1 = [1,2,3,4,5,6,7]
# list1 = list(map(lambda x : x*2,list1))
# print(list1)

#filter отфильтровывает лист ваш
list2 = ['Egor','Pasha','makarik','Petya','Vorona','hihi']
list3 = list(filter(lambda name: len(name) > 4, list2))
print(list3)

#zip
list4 = [1,2,3,4,5]
stc = 'abcd'
tuple = (True,True,False,False)
pasha = list(zip(list4,tuple,stc))
print(pasha)