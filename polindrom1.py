# my realisation with O(sqrt(n))

class PrimeNumber:

    def is_prime(n):
        d = 2
        while d*d <= n and n % d != 0:
            d += 1
        return d * d > n

def reverse_number(n, partial=0):
    if n == 0:
        return partial
    return reverse_number(n//10, partial * 10 + n % 10)


a = []

for i in range(100, 1000):
    if PrimeNumber.is_prime(i):
        a.append(i)

b = []


def maxpal(a):
    for i in range(len(a)-1, -1, -1):
        for j in range(len(a)-1, i, -1):
            if a[i]*a[j] == reverse_number((a[i]*a[j])):
                return a[i]*a[j], a[i], a[j]

print('Наибольший полиндром и два простых числа: ', maxpal(a))
