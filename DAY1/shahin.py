
print('\n**Level1**********1*****************')

'''تابعی بنویسید که یک کلمه را در ورودی بگیرد و به گونه ای در خروجی برگرداند که انگار کسی که لکنت زبان دارد، این کلمه را ادا کرده است.
 به این صورت که دو حرف اول کلمه دو بار تکرار شود و بعد از آن سه علامت نقطه و سپس یک فاصله قرارداده شود. انتهای کلمه را نیز با علامت سوال پایان دهید.

نکته: فرض کنید کلمات ورودی حداقل دو حرف را دارند

نمونه های ورودی و خروجی
stutter("incredible") ➞ "in... in... incredible?"'''


def f(x):
    print(f'"{x[0:2]}... {x[0:2]}... {x}?"')

x = input('Enter:')
f(x)



print('\n***Level2************3*************')
'''برنامه ای بنویسید که تمام اعداد بین 1000 تا 3000 (هر دو شامل) را پیدا کند به طوری که هر رقم از عدد یک عدد زوج باشد.
 اعداد به دست آمده باید در یک توالی جدا شده با کاما در یک خط چاپ شوند.

نکات: در صورت ارائه داده های ورودی به سؤال، باید آن را ورودی کنسول فرض کرد.'''

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))



print('\n******Level3********3*****************')

'''تابعی بنویسید که یک جمله را در ورودی بگیرد و طولانی ترین کلمه ی آن را در خروجی برگرداند. 
اگر دو یا چند کلمه با طول مساوی، طولانی ترین بودند، آن کلمه ای که به ابتدای جمله نزدیک تر است برگردانده شود.

کاراکتر های خاصی که به کلمه چسبیده اند نیز جزء کلمه به حساب می آیند. (مثل ‘، , و …)

نمونه هایی از ورودی و خروجی
longestWord("Hello darkness my old friend") ➞ "darkness"'''


def f(x):
    m = x[0]
    for  i in x:
        if len(i) > len(m):
            m=i
    return m
s = input('Enter:')
x = s.split(' ')
print(f(x))


print('\n****Level4**************4********************')


'''کلاسی بنویسید که حجم و مساحت دایره را محاسبه کند بطوری که از کاربر ورودی دریافت کند'''

class A:
    def __init__(self,r):
        self.r = r

    def area(self):
        print(4 * 3.14 * self.r**2)

    def volume(self):
        print(4/3 *3.14 * self.r**3)
r = int(input('Enter Nmaber:'))

ob1 = A(r)
ob1.area()
ob1.volume()



print('\n**Level5*********5*************')

'''کلاسی بنویسید که نام کاربری و رمز عبور از کاربر دریافت کند به گونه ای
 که نام کاربری و رمز عبور بغییر از شاهین و 123456 قابل قبول است اما ورودی این ها باشد Not correct چاپ شود, 
  
Enter USERname:zeyni
Enter PAssWOrd:13801380

Username: zeyni  --->  PassWord: 13801380'''

class A:
    User = 'shahin'
    passw = '123456'
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def f(self):
        return self.User != self.username and self.passw != self.password

    def g(self):
        print('Username: '+self.username +'  --->  '+'PassWord: '+self.password)

username = input('Enter USERname:')
password = input('Enter PAssWOrd:')
ob1 = A(username,password)

if ob1.f() == True:
    ob1.g()
else:
    print('Not correct')
