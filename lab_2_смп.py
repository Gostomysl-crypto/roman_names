import generator
import func_b

k = int(input('Input first num:'))
x = int(input('Input first num:'))
a_l = generator.a_l
generator.mylist(k, x)

c = []
for i in range(len(a_l)):
    a = a_l[i]
    b = [int(i) for i in str(a)]
    if func_b.isAscending(b) == True:
        c.append(a_l[i])
summa = int()
for i in range(len(c)):
    summa += int(c[i])
print('array of 100 numbers of arithmetic progression', a_l)
print('\n')
print('len of array:', len(a_l))
print('\n')
print('array of numbers by criterion "B":', c)
print('\n')
print('len of c:', len(c))
print('the sum of all numbers from an array of numbers by criterion "B":', summa)
