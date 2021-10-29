n = int(input("숫자를 입력해주세요:"))

a = [0, 10, 20, 30, 40, 50]
b = 0

for i in range(0,len(a)):
    if n == a[i]:
        print("%d 의 값은 %d번 위치에 있습니다." % (n, i+1))
        b=1

if b == 0:
    print("%d 의 값은 목록에 없습니다." % (n))
       
