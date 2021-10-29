
myList = [30, 10, 20]
print("현재 리스트 :%s" %myList)

myList.append(40)
print("append(40) 후의 리스트 : %s" % myList)

print("pop() 으로 추출한 값 : %s" % myList.pop())
print("pop() 후의 리스트 : %s" % myList)

myList.sort()
print("sort() 후의 리스트 : %s " % myList)

myList.reverse()
print("reverse() 후의 리스트 : %s " % myList)

print("20 값의 위치 : %d" % myList.index(20))

myList.insert(2, 222)
print("insert(2, 222) 후의 리스트 : %s " % myList)

myList.remove(222)
print("remove(222) 후의 리스트 : %s " % myList)

myList.extend([77,88, 77])
print("extend([77,88, 77]) 후의 리스트 : %s " % myList)

print("77 값의 개수 : %d"  % myList.count(77))



aa = []
bb = []
value =0

for i in range(0, 10) :
    aa.append(value)
    value+=2
    print(aa)

for i in range(0, 10) :
    bb.append(aa[9-i])
    print(bb)
print(" bb[0]은 %d, bb[99]는 %d 입력됨 " % (bb[0], bb[9] ))

#2차원 배열                                

list1 = []
list2 = []
value = 1

for i in range(0, 3) :
    for k in range(0, 4) :
        list1.append(value)
        value += 1
    list2.append(list1)
    list1 = []

for i in range(0, 3) :
    for k in range(0, 4) :
        print("%3d" % list2[i][k], end = " ")
    print(" ")

list1 = []
list2 = []
value = 1

#1차원 배열
for i in range(0,10):
    list1.append(i)
    print(list1)

#
list1 = []
list2 = []
value = 1
for i in range(0,3):
    for k in range(i,4):
        list1.append(value)
        value += 1        
    list2.append(list1)
    list1 = []

print(list1)
print(list2)


#튜플 : 한번 만들고 나면 변경 할 수 없는 집합
#리스트는 대괄호[]로 생성하고 튜플은 소괄호 ()로 생성, 딕셔너리는 중괄호{}로 생성
#튜플은 값을 수정할 수 없으며 읽기만 가능하므로 읽기 전용의 자료를 저장할 때 사용

mytuple =(1,2,3)
print(type(mytuple))
print(mytuple)
print(mytuple[1]) #튜플과 리스트의 공통점: 인덱스로 값을 불러올 수 있음
#mytuple[1]  = 20 #튜플값은 수정할 수 없음.

mytuple1 = 1,2,3
print(type(mytuple1))
print(mytuple1)

mytuple2 = (1,)# 하나의 값만 튜플로 치정하고 싶을때 ",쉼표를 뒤에 넣는다. 


#딕셔너리 : 인덱스가 아닌 키로 값을 지정
#리스트의 인덱스 대신 키 사용, 딕셔너리는 키를 이용하여 값을 찾아낼 때 편리
#딕셔너리는 리스트와 달리 값을 순서를 지켜주지 않는다.

#학생 정보의 리스트 표현
student1 = [20,'홍길동', '빅데이터']
print(student1[0])

#학생 정보의 딕셔너리 표현
student2 = {'학번' : 20, '이름' : '홍길동', '전공' : '빅데이터'}
print(student2['학번'])
#print(student2[0]) #인덱스로 호출시 에러남, 키로 출력해야한다. 


#딕셔너리에 값 추가
student2['연락처'] = '010-123-4567'#새로운 키와 값 대입 : 새로운 키가 마지막에 추가
print(student2)
student2['연락처'] = '010-123-0000'#기존의 키에 값 대입 : 기존 키 값 변경
print(student2)

# 딕셔너리는 remoce(), append()  함수를 적용할 수 없다.
#student2.append('010-0123-4566')

student2.pop('전공') #pop()함수로 딕셔너리의 특정키의 값 삭제
print(student2)
del(student2['이름'])#del 구문으로 디셔너리의 특정키의 값 삭제
print(student2)

#딕셔너리와 리스트의 공통점, 튜플은 수정이 불가능
student2.clear() #clear() 함수를 사용하면 딕셔너리와 리스트의 내용이 모두 지워짐
print(student2)
      
