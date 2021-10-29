
def plus(v1, v2):
    result = 0
    result = v1 + v2
    return result

hap = 0
while True:
    f = int(input("첫번째 값을 입력하세요:"))
    s = int(input("두번째 값을 입력하세요:"))
    hap = plus(f, s)
    print("%d과 %d의 plus() 함수 결과는 %d" % (f, s, hap))


def calc(v1, v2, op):
    result = 0
    if op =='+' :
        result = v1 + v2
    elif op =='-' :
        result = v1 - v2
    elif op =='*' :
        result = v1 * v2
    elif op =='/' :
        result = v1 / v2
    return result

f = int(input("첫번째 값을 입력하세요:"))
s = int(input("두번째 값을 입력하세요:"))
t = input("수행할 연산자를 입력하세요:")

hap = calc(f,s,t)
print("%d과 %d의 %s함수 결과는 %d" % (f, s, t, hap))


#지역변수 전역변수

def func1(): #지역변수
    a = 10
    print("func()에서 a의 값 %d" % a)

def func2(): 
    print("func2()에서 a의 값 %d" % a)

a= 20 #전역변수

func1()
func2()


def func1():
    result =100
    return result

def func2() :
    print("반환값 없는 함수 실행")

hap = 0

hap = func1()
print("func1()에서 돌려준 값 ==>%d" % hap)
func2()


def para2_func(v1, v2):
    result = 0
    result = v1+v2
    return result

def para3_func(v1, v2, v3):
    result = 0
    result = v1+v2+v3
    return  result

hap= 0 
hap=para2_func(10, 20)
print("매개변수 2개의 함수 호출 결과 ==>%d" % hap)
hap=para3_func(10, 20, 30)
print("매개변수 2개의 함수 호출 결과 ==>%d" % hap)

#초기값 설정
#def para_func(v1, v2, v3 = 0):
def para_func(v1, v2, v3 = 1):
    result = 0
    result = v1+v2+v3
    return  result

hap= 0 
hap=para_func(10, 20)
print("매개변수 2개의 함수 호출 결과 ==>%d" % hap)
hap=para_func(10, 20, 30)
print("매개변수 2개의 함수 호출 결과 ==>%d" % hap)

#가변 매개변수
def para_func(*para):
    result = 0
    for num in para:
        result = result + num

    return result

hap= 0 


hap=para_func(10, 20)
print("매개변수 2개의 함수 호출 결과 ==>%d" % hap)
hap=para_func(10, 20, 30)
print("매개변수 2개의 함수 호출 결과 ==>%d" % hap)


#**로 불러올 경우 딕셔너리로 불러온다
def dic_func(**para) :
    for k in para.keys():
        print("%s --> %d 명입니다." %(k, para[k]))

dic_func(아이오아이 = 11, 소녀시대 = 8, 걸스데이  = 4, AOA = 7)
