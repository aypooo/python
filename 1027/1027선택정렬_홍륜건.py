a = [35,9,2,87,17]
'''
#삽입정렬
for i in range(1, len(a)):
    for j in range(i,0,-1):
        if a[j] <a[j-1]:
            a[j],a[j-1] = a[j-1],a[j]

print(a)


#버블정렬

for i in range(len(a)-1,0,-1):
    for j in range(len(i)):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1], a[j]
print(a)

#선택 정렬
# 안쪽 for문으로 i 값 다음 부터 모든 배열을 비교해서  min_idx 구해서
# i 값보다 min_idx 가 작으면 교환 크면 다음 i값으로 넘어간다.
#반복
for i in range(len(a)-1):
    min_idx =i
    for j in range(i+1,len(a)):
        if a[j]< a[min_idx]:
            min_idx = j
            a[i],a[min_idx] = a[min_idx],a[i]
            print(a)


'''
#퀵 소트
import sys

def quick_sort(arr):
    if len(arr) == 1:
        return arr    
    pivot = a[len(arr)//2]
    l ,g, e = [] ,[] ,[]
    for i in arr:
        if i > pivot:
            g.append(i)
        elif i < pivot:
            l.append(i)
        else:
            e.append(i)

    return quick_sort(l) + e + quick_sort(g)

sys.setrecursionlimit(10000)
quick_sort(a)

#보고 했는데 안돌아갑니다 ㅜ

