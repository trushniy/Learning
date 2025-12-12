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

# print(sumstr(st1,st2))



# okay go try hard-code

import json
import os
from datetime import datetime

class Student:
    def __init__(self, name, age, grades=None):
        self.name = name
        self.age = age
        self.grades = grades if grades else {}
        self.registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)
    
    def get_average(self, subject=None):
        if subject:
            return sum(self.grades.get(subject, [])) / len(self.grades.get(subject, [1]))
        else:
            all_grades = []
            for grades_list in self.grades.values():
                all_grades.extend(grades_list)
            return sum(all_grades) / len(all_grades) if all_grades else 0
    
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'grades': self.grades,
            'registration_date': self.registration_date
        }

class StudentManager:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = {}
        self.load_data()
    
    def load_data(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for student_id, student_data in data.items():
                        student = Student(
                            student_data['name'],
                            student_data['age'],
                            student_data['grades']
                        )
                        student.registration_date = student_data['registration_date']
                        self.students[student_id] = student
        except Exception as e:
            print(f"ошибка загрузки данных: {e}")
    
    def save_data(self):
        try:
            data = {}
            for student_id, student in self.students.items():
                data[student_id] = student.to_dict()
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"ошибка сохранения данных: {e}")
    
    def add_student(self, student_id, name, age):
        if student_id not in self.students:
            self.students[student_id] = Student(name, age)
            self.save_data()
            return True
        return False
    
    def get_statistics(self):
        if not self.students:
            return "нет студентов в базе данных"
        
        total_students = len(self.students)
        avg_age = sum(student.age for student in self.students.values()) / total_students
        
        all_averages = []
        subject_stats = {}
        
        for student in self.students.values():
            student_avg = student.get_average()
            if student_avg > 0:
                all_averages.append(student_avg)
            
            for subject, grades in student.grades.items():
                if subject not in subject_stats:
                    subject_stats[subject] = []
                subject_stats[subject].extend(grades)
        
        overall_avg = sum(all_averages) / len(all_averages) if all_averages else 0
        
        stats = f"""
статистика студентов
всего студентов: {total_students}
средний возраст: {avg_age:.1f} лет
общий средний балл: {overall_avg:.2f}

статистика по предметам"""
        for subject, grades in subject_stats.items():
            avg_grade = sum(grades) / len(grades)
            stats += f"\n{subject}: средний балл {avg_grade:.2f} ({len(grades)} оценок)"
        
        return stats

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def matrix_multiply(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    
    if cols1 != rows2:
        return None
    
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

print("сложная программа")
manager = StudentManager()

manager.add_student("001", "иван петров", 20)
manager.add_student("002", "мария сидорова", 19)
manager.add_student("003", "алексей козлов", 21)

manager.students["001"].add_grade("математика", 5)
manager.students["001"].add_grade("математика", 4)
manager.students["001"].add_grade("физика", 5)

manager.students["002"].add_grade("математика", 4)
manager.students["002"].add_grade("химия", 5)
manager.students["002"].add_grade("физика", 4)

manager.students["003"].add_grade("математика", 3)
manager.students["003"].add_grade("история", 5)

manager.save_data()

print(manager.get_statistics())

print("\nчисла фибоначчи (первые 10)")
fib_numbers = list(fibonacci_generator(10))
print(fib_numbers)

print("\nумножение матриц")
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result_matrix = matrix_multiply(matrix_a, matrix_b)
print(f"матрица a: {matrix_a}")
print(f"матрица b: {matrix_b}")
print(f"a × b = {result_matrix}")

print("\nобработка данных")
numbers = list(range(1, 21))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = list(filter(is_prime, numbers))
squares = list(map(lambda x: x**2, primes))
print(f"простые числа от 1 до 20: {primes}")
print(f"их квадраты: {squares}")

data_analysis = {
    'numbers': numbers,
    'primes': primes,
    'even': [x for x in numbers if x % 2 == 0],
    'odd': [x for x in numbers if x % 2 == 1]
}

print(f"\nанализ чисел от 1 до 20:")
for category, values in data_analysis.items():
    print(f"{category}: {len(values)} элементов, сумма: {sum(values)}")
