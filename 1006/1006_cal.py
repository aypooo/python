# 20211006 파이썬 계산기,홍륜건#

# 변수 선언 #
a = int(input("a값 입력(숫자):")) # input() 함수는 사용자로부터 값을 입력받은 후 변수 a 대입#
b = int(input("b값 입력(숫자):")) # input() 함수는 사용자로부터 값을 입력받은 후 변수 a 대입# 


#산술연산자를 통한 사칙연산#
result = a+b
print(a,"+",b,"=",result)
result = a-b
print(a,"-",b,"=",result)
result = a*b
print(a,"*",b,"=",result)
result = a/b
print(a,"/",b,"=",result)
result = a%b
print(a,"%",b,"=",result)
result = a//b
print(a,"//",b,"=",result)
