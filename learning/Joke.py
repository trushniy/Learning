# print('пидорас?','ответь True или False')
# str = input()
# if str == True:
#      print('понятно все')
# elif str == False:
#      print('не верю, всё равно пидорас')
# else:
#      print('в итоге все понятно с тобой')

# print('пидорас?','да или нет')
# str1 = input()
# if str1 == 'да':
#      print('понятно все')
# elif str1 == 'нет':
#      print('не верю, всё равно пидорас')
# else:
#      print('в итоге все понятно с тобой')

with open(r'learning\Test.txt', encoding='utf-8') as file:
    test42 = file.read()
print(test42)