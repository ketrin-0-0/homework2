#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1

Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# print("First exercise")
# for i in range(5):
#     print(i+1,")", 0)
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

# print("Second exercise")
# count = 0
# for i in range(10):
#     digit = input("2 ex")
#     if int(digit) == 5: count+=1
# print("there are ", count, "five numbers")

'''
Задача 3

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
#print("Third exercise")
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# print("Fourth exercise")
# mul = 1
# for i in range(2,11):
#      mul*=i
# print(mul)
'''
Задача 5

Вывести цифры числа на каждой строчке.
'''
#print("Fifth exercise")
# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6

Найти сумму цифр числа.
'''
# print("Sixth exercise")
# number = 768
# sum_number = 0
# while number>0:
#     sum_number += number%10
#     number = number//10
# print(sum_number)


'''
Задача 7

Найти произведение цифр числа.
'''
# print("Seventh exercise")
# number = 768
# mul_number = 1
# while number>0:
#     mul_number *= number%10
#     number = number//10
# print(mul_number)
'''
Задача 8

Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# print("Eighth exercise")
# integer_number = 213413
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9

Найти максимальную цифру в числе
'''
# print("Eighth exercise")
# integer_number = 253413
# max_num = -1
# while integer_number>0:
#     n = integer_number%10
#     if n > max_num: max_num = n
#     integer_number = integer_number//10
# print("Max number:", max_num)
'''
Задача 10

Найти количество цифр 5 в числе
'''
# print("Tenth exercise")
# integer_number = 2143
# count = 0
# while integer_number>0:
#     if integer_number%10 == 5:
#         count+=1
#     integer_number = integer_number//10
# print("There are",count,"five numbers")