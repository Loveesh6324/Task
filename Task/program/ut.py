import pytest
import requests
import json

#API Test:
def test1():
    url = "http://api.zippopotam.us/us/90210"
    response = requests.get(url)
    res = json.loads(response.content)
    print(response.status_code)
    print(res)
    print(res["country"])
    print(res["places"][0]["state"])


#Testing Function
def multi(x, y):
    return x*y

def testmulti():
    assert multi(5, 6) == 30


#Parameters Test
@pytest.mark.parametrize('x,y,z', [(10, 20, 30), (100, 200, 400)])
def test(x, y, z):
    assert x+y == z


def add(x, y):
    return x+y

@pytest.mark.parametrize('n1 ,n2, result',[(7, 3, 10), ('Hello', 'World', 'HelloWorld')])
def testadd(n1, n2, result):
    assert add(n1, n2) == result
