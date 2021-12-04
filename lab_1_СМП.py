

a_dict = input()
a = eval(a_dict)
print(type(a))


s_d = dict()
for v in range(len(a)):  # formatting keys and values of input d[{"a":1}, {"a":2}, {"a":5}, {"a":10}]ata
    s_d.update({str(list(a[v].keys())[0])+str(v+1): int(list(a[v].values())[0])})
print(s_d)

s = list(s_d.values())  # create a list with values of dictionary
print('Unsorted list of values: ', s)
for i in range(-1, len(s)):  # selection sort
    minimum = i

    for j in range(i + 1, len(s)):
        if s[j] < s[minimum]:
            minimum = j

        s[minimum], s[i] = s[i], s[minimum]

print('Sorted list of values: ', s)

sum = 0

for i in range(len(s)):
    p = (6 * s[i]) * 0.5  # semi-perimeter of hexagon with a side s[i]
    sum = sum + p
    # print('Semi-perimeter of a regular hexagon with a side', s[i], '=', p)
print('The sum of the semiperimeters =', sum)
