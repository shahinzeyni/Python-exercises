print('\n---Level2-----1-------------')
'''Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example: If the following n is given as input to the program:



Then, the output of the program should be:

2.716666666666667

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:::::: Use float() to convert an integer to a float'''




ANSWER is:


def f(x):
    p = 0
    for i in range(1, x + 1):
        sum_1 = i / (i + 1)
        p += sum_1
    return p


print(f(5))

print('\n---Level2-----2-------------')

'''Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions
we use Finally method.'''



ANSWER is:


def f(x):
    try:
        x // 0
    except ZeroDivisionError as ze:
        print('OOPs.... this wrong....!')
    finally:
        print('silam ozdad sidam miyadd......')

f(5)


print('\n---Level3-----3-------------')

''' You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is: 1: Sort based on name; 2: Then sort based on age; 3: Then sort by score. The priority is that name > age > score. If the following tuples are given as input to the program: Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 Then, the output of the program should be: [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Hints: In case of input data being supplied to the question, it should be assumed to be a console input. We use itemgetter to enable multiple sort keys.

Solutions: from operator import itemgetter, attrgetter'''



ANSWER is:


l = []
while True:
    karbar = input()
    if not karbar:
        break
    l.append(tuple(karbar.split(",")))

print(sorted(l, key=itemgetter(0, 1, 2)))




print('\n---Level5-----4-------------')

'''A**2 = B**2 + C**2 -2*B*C * Coc(alpha)
کلاس بنویسید که دارای B,C,alpha
باشد و طبق فرمول بالا طول ضلع سوم را بدست آوردید و در آخر سر مقادیر  '''


ANSWER is:


import math

class A:
    def __init__(self, b, c, alfha):
        self.b = b
        self.c = c
        self.alpha = alfha

    def radiyan(self):
        return self.alpha * 200 / 180

    def f(self):
        return ((self.b ** 2) + (self.c ** 2) - (2 * self.b * self.c * math.cos(self.radiyan() ** 0.5)))

    def perime(self):
        return self.b + self.c + self.f()

    def area(self):
        P = self.perime() / 2
        return (P * (P - self.f()) * (P - self.b) * (P - self.c)) ** 0.5


ob1 = A(10, 11, 60)
print(ob1.area())
print(ob1.perime())
