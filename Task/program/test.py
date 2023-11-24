import pytest
import requests


import json

# def test1():
#     response = requests.get("http://127.0.0.1:8000/getapi/")
#     res=json.loads(response.content)
#     assert response.status_code == 200
#     print(res)


def test2():
    url = "http://api.zippopotam.us/us/90210"
    response = requests.get(url)
    res = json.loads(response.content)
    print(response.status_code)
    print(res)
    print(res["country"])
    print(res["places"][0]["state"])


# LAMBDA
# x=[lambda i=i: i*i for i in range(1,6)]
# for f in x:


#     print(f())

def demo_func(x):
    return lambda a: [a+i for i in range(0, x)]


var = demo_func(6)
print(var(1))

# MAP
# n=(1,2,3,4)
# result=map(lambda x:x**2,n)
# print(list(result))

# FILTER
# a = [i for i in range(100)]
# result = filter(lambda x: x % 2 != 0, a)
# print(list(result))


# DECORATOR
# a, b = 2, 3
# def decorator(fun):
#     def add(a, b):
#         print(a+b)
#         print(fun(a, b))
#     return add

# @decorator
# def sub(a, b):
#     return(a-b)
# sub(a, b)


# def task():
#     d=dict()
#     for x in range(1,21):
#         d[x]=x**2
#     print(d)

# task()


# @pytest.mark.parametrize('x,y,z',[(10,20,30),(100,200,400)])
# def test(x,y,z):
#     assert x+y==z

# def add(x, y):
#     return x+y


# def multi(x, y):
#     return x*y

# @pytest.mark.parametrize('n1 ,n2, result',
#                          [
#                              (7, 3, 10), ('Hello', 'World', 'HelloWorld')
#                          ])
# def testadd(n1, n2, result):
#     assert add(n1, n2) == result

# def testmulti():
#     assert multi(5,6)==30
