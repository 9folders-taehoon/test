# class  는 데이터와 기능을 함께 묶는 방법을 제공합니다.
# namespace 는 이름에서 객체로 가는 매핑입니다. 대부분의 이름 공간은 현재 파이썬 딕셔너리로 구현되어 있지만
# scope 순서 = 지역 -> 비 로컬이지만 비 글로벌 -> 마지막 직전의 스코프는 현재 모듈의 전역 이름


class MyClass:
    """A simple example class"""

    i = 12345

    def f(self):
        return "hello world"


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


# x = Complex(3.0, -4.5)
# print(x.r, x.i)
# x.count = 1
# while x.count <= 10:
#     x.count = x.count * 2
# print(x.count)
# del x.count
# print(x.count)

#
# x = MyClass()
# xf = x.f()
# while True:
#     print(xf)


# class Dog:
#     kind = "canine"
#     tricks = []
#
#     def __init__(self, name):
#         self.name = name
#         # self.tricks = []
#
#     def add_trick(self, trick):
#         # self.tricks.append(trick)
#         self.tricks.append(trick)
#
#
# d = Dog("Fido")
# e = Dog("Buddy")
# d.kind = "z"
# e.kind = "zz"
# print(d.kind)
# print(e.kind)
# d.add_trick(1)
# e.add_trick(2)
# print(d.tricks)
# print(e.tricks)

# d.add_trick("roll over")
# e.add_trick("play dead")
# print(d.tricks)


# class Warehouse:
#     purpose = "storage"
#     region = "west"
#
#
# w1 = Warehouse()
# print(w1.purpose, w1.region)
#
# w2 = Warehouse()
# w2.region = "east"
# print(w2.purpose, w2.region)
#
# print(f"---\n{w1.region}, {w2.region}")


# class Bag:
#     def __init__(self):
#         self.data = []
#
#     def add(self, x):
#         self.data.append(x)
#
#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)
#         self.add(x)
#
#
# a = Bag()
# a.addtwice(2)
# print(a.data)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         print(f"제 이름은 {self.name}입니다.")
#
#     def get_age(self):
#         print(f"제 나이는 {self.age}세 입니다.")
#
#
# class Student(Person):
#     def __init__(self, name, age, GPA):
#         super().__init__(name, age)
#         self.GPA = GPA
#
#     def get_GPA(self):
#         print(f"제 학점은 {self.GPA}입니다.")
#
#
# A = Student("부모", 19, "ETA")
# A.get_GPA()


# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)
#
#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)
#
#     __update = update
#
#
# class MappingSubclass(Mapping):
#     def update(self, keys, values):
#         for item in zip(keys, values):
#             self.items_list.append(item)
#
#
# A = MappingSubclass("asd")
# A.update("zxc", "qwe")
# print(A.items_list)

# from dataclasses import dataclass
#
#
# dataclass()
#
#
# class Employee:
#     name: str
#     dept: str
#     salary: int
#
#
# john = Employee("john", "computer lab", 1000)
# print(john.dept)
# print(john.salary)

# for e in [1, 2, 3]:
#     print(e)
# for e in (1, 2, 3):
#     print(e)
# for e in {"one": 1, "two": 2}:
#     print(e)
# for e in "123":
#     print(e)
#
# a = ["hello", "hi", "안녕"]
# print(" ,".join(a))
import datetime

# print("{}".format(datetime.datetime.utcnow() + datetime.timedelta(hours=9)))

import glob, os

# modules = []
#
# for module_file in glob.glob("*.py"):
#     try:
#         module_name, ext = os.path.splitext(os.path.basename(module_file))
#         print(f"module_name = {module_name} ext = {ext}")
#         module = __import__(module_name)
#         print(f"module = {module}")
#         modules.append(module)
#         print(f"modules = {modules}")
#     except ImportError:
#         pass
#
#     for module in modules:
#         module.hello()
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import datetime
#
#
# def generate_report():
#     # 여기에서 보고서를 생성하는 코드를 작성합니다.
#     # 예를 들어, 파일에서 데이터를 읽거나 API로부터 데이터를 가져오는 등의 작업을 수행합니다.
#     report_content = "이것은 gpt 가 짜준 리포트 메일 코드입니다람쥐"
#     return report_content
#
#
# def send_email(sender_email, sender_password, recipient_email, subject, body):
#     msg = MIMEMultipart()
#     msg["From"] = sender_email
#     msg["To"] = recipient_email
#     msg["Subject"] = subject
#
#     msg.attach(MIMEText(body, "plain"))
#
#     server = smtplib.SMTP("smtp.naver.com", 587)
#     server.starttls()
#     server.login(sender_email, sender_password)
#     text = msg.as_string()
#     server.sendmail(sender_email, recipient_email, text)
#     server.quit()
#
#
# if __name__ == "__main__":
#     # 보고서 생성
#     report = generate_report()
#
#     # 이메일 설정
#     sender_email = "djwrktls@naver.com"  # 발신자 이메일
#     sender_password = "rlaxognsWkd1234"  # 발신자 이메일 비밀번호
#     recipient_email = "taehoon.kim@9folders.com"  # 수신자 이메일
#     subject = "델리버뤼 - " + datetime.date.today().strftime("%Y-%m-%d")
#     body = report
#
#     # 이메일 보내기
#     send_email(sender_email, sender_password, recipient_email, subject, body)

# coffee = 10
# while True:
#     money = int(input("돈을 넣어줍쇼"))
#     if money == 300:
#         print("커피 가져가쇼")
#         coffee -= 1
#         print("남은 커피는 %d개 입니다" % coffee)
#
#     elif money > 300:
#         print("커피 가져가쇼")
#         coffee -= 1
#         money = money - 300
#         print("남은 커피는 %d개 이고 거슬음돈은 %d원 입니다" % (coffee, money))
#
#     else:
#         print("커피 가격이 부족함돠")
#         print("%d원을 가져가쇼" % money)
#
#     if coffee == 0:
#         break


# class SmartPhone:
#     def __init__(self, brand, informations, details):
#         self._brand = brand
#         self._informations = informations
#
#     def __str__(self):
#         return f"str: {self._brand} - {self._informations}"
#
#     def __repr__(self):
#         return f"repr: {self._brand} - {self._informations}"
#
#     def get_information(self):
#         print(f"Current Id : {id(self)}")
#         print(
#             f"SmartPhone Detail Info : {self._brand} {self._informations.get('price')}"
#         )
#
#         P1 = SmartPhone("Iphone", {"color": "white", "price": 10000})
#         P2 = SmartPhone("Galaxy", {"color": "black", "price": 8000})
#
#         P1.detail_info()
#
#         print(P1.__class__, P2.__class__)
#         print(id(P1.__class__), id(P2.__class__))
#
#
# SmartPhone().get_information()
# 함수 이름 = lambda 매개변수.... : 표현식
# a = lambda a, b: a + b
# result = a(1, 2)
# print(result)

# with open("test.txt", "a") as f:
#     for i in range(1, 11):
#         data = "%d번째입니다.\n" % i
#         f.write(data)

# with open("test.txt", "r") as f:
#     # for i in f.read():
#     #     print(i)
#     print(type(f))

# import sys
#
# args = sys.argv
# for i in args[1:]:
#     print(i.upper(), end=" ")


# class C:
#     def __init__(self, first, second):
#         self.result = 0
#         self.first = first
#         self.second = second
#
#     def add(self):
#         result = self.first + self.second
#         return result
#
#     def sub(self):
#         self.result
#         return self.result
#
#     def mul(self):
#         self.result
#         return self.result
#
#     def div(self):
#         return self.first / self.second
#
#
# class MoreC(C):
#     def pow(self):
#         result = self.first**self.second
#         return result
#
#
# class SafeC(C):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second
#
#
# # cal1 = C()
# # cal2 = C()
#
# # cal1.set_data(1, 2)
# a = SafeC(4, 0)
# print(a.div())


# class Family:
#     lastname = "김"
#
#
# a = Family()
# b = Family()
# Family.lastname = "박"
# a.lastname = "p"
# b.lastname = "k"
# print(a.lastname)
# print(b.lastname)

PI = 3.141592


class Math:
    def solv(self, r):
        return PI * (r**2)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
