'''
import func


func.func1()
func.func2()
func.func3()

#from 으로 불러오면 모듈명 생략가능
from func import *

func1()
func2()
func3()


import sys

print(sys.builtin_module_names)


from calc import *

in1 = float(input("첫 번째 숫자를 입력하세요 :"))
op = input("연산자(+,-, *,/)를 입력하세요 :")
in2 = float(input("두 번째 숫자를 입력하세요 :"))

print()
print("***모듈로 작성한 계산기 호출 결과***")

if op == '+':
    print("%5.1f+%5.1f = %5.1f" %(in1, in2, plus(in1,in2)))
elif op == '-':
    print("%5.1f+%5.1f = %5.1f" %(in1, in2, minus(in1,in2)))
elif op == '*':
    print("%5.1f+%5.1f = %5.1f" %(in1, in2, multiply(in1,in2)))
elif op == '/':
    print("%5.1f+%5.1f = %5.1f" %(in1, in2, divide(in1,in2)))
else:
    print("연산자를 모르겠네요. ㅜㅠ")

#리스트와 반복문 실습
a,b,c,d = 0,0,0,0
hap = 0

a = int(input("1번째 숫자 : "))
b = int(input("2번째 숫자 : "))
c = int(input("3번째 숫자 : "))
d = int(input("4번째 숫자 : "))

hap = a + b + c + d

print("합계 ==> %d" % hap)

#리스트 활용
a,b,c,d = 0,0,0,0
aa= [0,0,0,0]
hap = 0

aa[0] = int(input("1번째 숫자 : "))
aa[1] = int(input("2번째 숫자 : "))
aa[2] = int(input("3번째 숫자 : "))
aa[3] = int(input("4번째 숫자 : "))

hap = aa[0] + aa[1] + aa[2] + aa[3]

print("합계 ==> %d" % hap)


#리스트와 append() 함수 활용
#aa = [0, 0, 0, 0]
aa = []
#aa.append(0)
#aa.append(0)
#aa.append(0)
#aa.append(0)

for i in range(4):
    aa.append(0)

print(aa)

for i in range(4):
    aa[i] = int(input("숫자를 입력하세요"))
    print(aa)
print(aa)

for i in range(4):
    hap = hap + aa[i]
    print(hap)
print(hap)

hap = 0
aa = []
for i in range(4):
    aa.append(0)
    aa[i] = int(input("숫자를 입력하세요"))
    hap = hap + aa[i]
    print(aa)
print(hap)

'''

a = [1,8,7,3,2,9,4,1,6,5]
for i in a:
    if a[i] != a[-1]:
        if a[i] > a[i+1]:
            del a[i]
            print(a)    
           
                    
