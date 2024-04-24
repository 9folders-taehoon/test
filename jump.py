# class Error(Exception):
#     pass
#
#
# def n(nick):
#     if nick == "바보":
#         4 / 0
#     print(nick)
#
#
# try:
#     n("바보")
#     n("천사")
#
# except Exception as e:
#     print(type(e))
#     print(type(str(e)))


# def positive(x):
#     return x > 0
#
#
# print(list(filter(positive, ([1, -3, 2, 0, -5, 6]))))
#
# import datetime
#
# a = datetime.date(2024, 3, 31)
# b = datetime.date(2022, 4, 22)
# c = b - a
# # print(type(a))
# # print(type(b))
# # print(type(c))
# # print(c.days)
# print(a.isoweekday())
# import datetime
# import time

# # 2024년 4월 2일
# print(datetime.date(2024, 4, 2))
# # 0은 월요일 6은 일요일
# print(datetime.date(2024, 4, 2).weekday())
# # 1은 월요일 7은 일요일
# print(datetime.date(2024, 4, 2).isoweekday())
# # 현재 시간을 실수 형태로 표시
# print(time.time())
# # time.struct_time(tm_year=2023, tm_mon=5, tm_mday=21, tm_hour=16, tm_min=48, tm_sec=42, tm_wday=1, tm_yday=141, tm_isdst=0) 형태로 표시
# print(time.localtime())
# # 시간을 튜플형태로 반환
# print(time.asctime(time.localtime(time.time())))
# # 현재 시간만 튜플형태로 반환
# print(time.ctime())
# # 시간 관련된 포맷 코드 사용
# print(time.strftime("%H", time.localtime(time.time())))
# # 시간 간격을 두고 루프 실행가능
# for i in range(10):
#     print(i)
#     time.sleep(2)

# import math

# # 최대 공약수
# print(math.gcd(23, 120, 55590))
# # 최소 공배수
# print(math.lcm(20, 120, 55590))


# def add(data):
#     result = 0
#     for i in data:
#         result += i
#     return result
#
#
# data = [1, 2, 3, 4, 5]
# result = add(data)
# print(result)

# 함수 사용
# import functools

#
# data = [1, 2, 3, 4, 5]
# # result = functools.reduce(lambda x, y: x + y, data)
# print((lambda x, y: x + y, data))

# 정렬의 키로 사용
# from operator import itemgetter
#
# students = [
#     {"name": "jane", "age": 22, "grade": "A"},
#     {"name": "dave", "age": 32, "grade": "B"},
#     {"name": "sally", "age": 17, "grade": "B"},
# ]
#
# result = sorted(students, key=itemgetter("name"), reverse=True)
# print(result)

# 파일을 복사하거나 이동할 때 사용
# import shutil
# 복사
# shutil.copy("원래 경로", "이동 경로")
# 이동
# shutil.move("원래 경로", "이동 경로")

# 특정 디렉터리에 있는 파일 이름을 알야야 할 때

# import glob
#
# print(glob.glob("/Users/taehoon/7folders/test/*"))

# 객채의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게하는 모듈
# import pickle
# import json

#
# f = open("test.txt", "a")
# data = {1: "python", 2: "you need"}
# pickle.dump(data, f)
# json.dump(data, f)
# f.close()
#
# f = open("test.txt", "r")
# print(f.read())
# data = json.load(f)
# print(data)
# data = pickle.load(f)
# print(data)

# import os

# a = os.environ
# print(a.get("REWORK_ENV"))
# print(os.getcwd())
# os.system("ls")

# # 시스템 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 리턴
# f = os.popen("ls")
# print(f)
# print(f.readlines())
# f.close()
# print(f)
# print(f.read())

# import zipfile

# with zipfile.ZipFile("mytext.zip", "w") as myzip:
#     myzip.write("test.txt")
#     myzip.write("testfile.txt")

# with zipfile.ZipFile("mytext.zip") as myzip:
#     myzip.extract("test.txt")

# import time
# import threading


# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print("working:%s\n" % i)
#
#
# print("Start")
#
#
# t = []
# for i in range(5):
#     aa = threading.Thread(target=long_task)
#     t.append(aa)
#     aa.start()
#     # aa.join()
#
# for i in t:
#     i.join()
# for i in t:
#     i.start()
#
# for i in t:
#     i.join()

# print("End")

# import tempfile
#
# filename = tempfile.mkstemp()
# print(filename)
# with tempfile.TemporaryFile() as t:
#     t.write(b"hello")
#     t.seek(0)
#     print(t.read())

# with open("testfile.txt", "wb") as f:
#     f.write(b"test")
#     f.close()

# s = "hello i'm kim"
# print(s.encode("utf-8"))


# import traceback
#
#
# def a():
#     return 1 / 0
#
#
# def b():
#     a()


# def main():
#     try:
#         b()
#     except:
#         print("오류가 발생했습니다.")
#         print(traceback.format_exc())


# main()
# aaa = {"name": "suzy", "age": "31", "job": "singer"}
# import json

# with open("info.json") as f:
#     data = f.read()
#     print(data)
#     f.seek(0)
#     d = json.load(f)
#     print(d)
#
# with open("info.json", "w") as f:
#     json.dump(aaa, f)
#
# with open("info.json", "r") as f:
#     print(f.read())
# z = json.dumps(aaa, ensure_ascii=False, indent=2)
# print(type(aaa))
# print(z)
# print(type(json.loads(z)))

# import urllib.request
# import ssl
#
# context = ssl.
#
#
# def get_wiki(page):
#     resource = "https://wikidocs.net/{}".format(page)
#     with urllib.request.urlopen(resource) as s:
#         with open("wikidocs_%s.html" % page, "wb") as f:
#             f.write(s.read())


# get_wiki(12)

# import webbrowser

# webbrowser.open_new("http://python.org")
# webbrowser.open("http://python.org", 2)

# import faker
#
# f = faker.Faker("ko-KR")
# test = [(f.name(), f.address()) for i in range(30)]
# print(test)

# from fractions import Fraction
# import sympy
#
# x, y = sympy.symbols("x y")
# f = sympy.Eq(x * Fraction("2/5"), 1760)

# d = []


# def gugu(dan):
#     [d.append(dan * i) for i in range(1, 10)]
#     return d
#
#
# print(gugu(2))


# def gongbaesu(n, a, b):
#     hap = 0
#     for i in range(1, n):
#         if i % a == 0 or i % b == 0:
#             hap = hap + i
#     return hap
#
#
# print(gongbaesu(1000, 3, 5))

# result = 0
# for n in range(1, 1000):
#     if n % 3 == 0 or n % 5 == 0:
#         result += n
# print(result)

# 함수 이름은? get_total_page
# 입력받는 값은? 게시물의 총 개수(m), 한 페이지에 보여 줄 게시물 수(n)
# 출력하는 값은? 총 페이지 수


# def total_page(m, n):
#     if m % n == 0:
#         return m // n
#     else:
#         return m // n + 1
#
#
# print(total_page(302, 10))
# print(26 // 7)
#
# import sys
#
# option = sys.argv[1]
# memo = sys.argv[2]
#
# if option == "-a":
#     with open("memo.txt", "a") as f:
#         f.write(memo)
#         f.write("\n")
#
# if option == "-v":
#     with open("memo.txt") as f:
#         print(f.read())

# import os
#
#
# def search(dirname):
#     try:
#         filename = os.listdir(dirname)
#         for i in filename:
#             full = os.path.join(dirname, i)
#             if os.path.isdir(full):
#                 search(full)
#             else:
#                 ext = os.path.splitext(full)[-1]
#                 if ext == ".py":
#                     print(full)
#     except PermissionError:
#         pass
#
#
# search("/Users/taehoon/7folders")

# 컴퓨터에서 문자를 처리하고자 각각의 문자 셋을 정해놓고 문자를 처리했다.(영어권) 127개의 문자만 다룸
# 비 영어권 유니코드
# 유니코드 문자열은 인코딩 없이 그대로 파일에 적거나 다른 시스템으로 전송할 수 없다...
# a = "한글"
# b = a.encode("euc-kr")


# with open("euc_kr.txt", "wb") as f:
#     f.write(b)
#
# with open("euc_kr.txt", encoding="euc-kr") as f:
#     aaaa = f.read()
# data = aaaa + "\n" + "영어"
#
# with open("euc_kr.txt", encoding="euc-kr", mode="a") as f:
#     f.write(data)

# with open("euc_kr.txt", encoding="euc-kr", mode="r") as f:
#     print(f.read())


# class Mul:
#     def __init__(self, m):
#         self.m = m
#
#     def __call__(self, n):
#         return self.m * n
#
#
# if __name__ == "__main__":
#     mul3 = Mul(3)
#     mul5 = Mul(5)
#
#     print(mul3(10))
#     print(mul5(10))


# class MyClass:
#     def __init__(self):
#         print("MyClass 인스턴스가 생성되었습니다.")
#
#     def __call__(self):
#         print("__call__ 메서드가 호출되었습니다.")
#         print("전달된 인자:")
#
#
# # MyClass의 인스턴스 생성
# obj = MyClass()
#
# # 인스턴스를 함수처럼 호출
# obj()


# def mul(m):
#     def wrapper(n):
#         return m * n
#
#     return wrapper
#
#
# if __name__ == "__main__":
#     mul5 = mul(5)
#
#     # print(mul3(10))
#     m = mul5(2)
#     print(m)

# import time
#
#
# def elapsed(original_func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = original_func(*args, **kwargs)
#         end = time.time()
#         print("함수 수행시간: %f 초" % (end - start))
#         return result
#
#     return wrapper
#
#
# @elapsed
# def myfunc(msg):
#     print("'%s'를 출력합니다" % msg)
#
#
# # deco_myfunc = elapsed(myfunc)
# # deco_myfunc()
# myfunc("You need python")


# def trace(func):
#     def wrapper():
#         print(func.__name__, "함수 시작")
#         func()
#         print(func.__name__, "함수 끝")
#
#     return wrapper
#
#
# @trace
# def hello():
#     print("hello")
#
#
# def world():
#     print("world")
#
#
# hello()

# a = [1, 2, 3]
# b = "hello"
# ia = iter(a)
# ib = iter(b)
#
# for i in ia:
#     print(i)
#
# print(next(ia))

# 이터레이터는 반복가능한... next를하면 객체를 던져주는...
# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.position = len(self.data) - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.position < 0:
#             raise StopIteration
#         result = self.data[self.position]
#         self.position -= 1
#         return result
#
#
# if __name__ == "__main__":
#     i = MyIterator([1, 2, 3, 4])
#     for item in i:
#         print(item)


# 제너레이터는 이터레이터를 생성해 주는 함수!!!
# def mygen():
#     yield "a"
#     yield "b"
#     yield "c"
#
#
# g = mygen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def mygen():
#     for i in range(1, 1000):
#         result = i * i
#         yield result
#
#
# gen = mygen()
# for i in range(10):
#     print(next(gen))

# gen = (i * i for i in range(1, 1000))
# print(type(gen))


# 1부터 1000까지
# class G:
#     def __init__(self):
#         self.data = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         result = self.data * self.data
#         self.data += 1
#         if self.data >= 100:
#             print("끄태 도달")
#             raise StopIteration
#         return result
#
#
# a = G()
# for i in range(100):
#     print(next(a))

# import time
#
#
# def long_job():
#     print("job start")
#     time.sleep(1)
#     return "done"
#
#
# list_job = [long_job() for i in range(5)]
# print(list_job.__len__())


# 데코

# import time
#
#
# def test(func):
#     def wrapper(n):
#         ax = 0
#         print("start")
#         func(n)
#         print("end")
#
#     return wrapper
#
#
# @test
# def te(n):
#     print("%d 번" % n)
#     time.sleep(1)
#
#
# te(1)


# def need_password(func):
#     def wrapper(*args, **kwargs):
#         password = "1234"
#         input_pw = input("비밀번호를 입력하세요")
#         if input_pw == password:
#             result = func(*args, **kwargs)
#         else:
#             result = "잘못된 비밀번호 입니다"
#         return print(result)
#
#     return wrapper
#
#
# source = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]
#
#
# @need_password
# def get_avg(source: list):
#     for index, point in enumerate(source):
#         print(f"{index+1}번, 평균 : {sum(point)/len(point):.1f}")
#
#
# get_avg(source)


# def exist_id(func):
#     def wrapper(*args):
#         input_data = input("sex")
#         if input_data == "w":
#             func(args)
#         else:
#             return print("no")
#
#     return wrapper
#
#
# @exist_id
# def login_test(text):
#     print("%s" % text)
#
#
# login_test("hello m.r my yesterday")

# import time
# import threading
#
#
# def long_job():
#     for i in range(5):
#         print("%d start" % i)
#         time.sleep(1)
#         print("%d done" % i)
#
#
# threads = []
#
# for i in range(5):
#     a = threading.Thread(target=long_job)
#     threads.append(a)
#
# for i in threads:
#     i.start()


# #동적 언어와 정적 언어
# a=1
# print(type(a))
#
# a='1'
# print(type(a))
# 변수의 타입을 동적으로 변경 가능

# 어노테이션 -> 힌트 개념


# num : int = 1
# 화살표는 리턴값의 타입을 정해주는거네
# def add(a: int, b: int) -> int:
#     return a + b
#
#
# x = add(4, 5.5)
# print(x)

# data = """
# park 800905-1049118
# kim  700905-1059119
# """
#
# for i in data.split("\n"):
#     print(i)
#     for word in data.split(" "):
#         print(word)
#     # i[-7:].replace()


# import re
#
# p = re.compile("[a-z]+")
# m = p.match("2")
# print(m)
#
# reg_domain = (
#     r"^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|"
#     r"([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|"
#     r"([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\."
#     r"([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$"
# )

import calendar
from datetime import datetime

print(1, calendar.monthrange(2024, 4)[1])


# last_day = calendar.monthrange(date.year)
