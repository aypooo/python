a = [1,8,7,3,2,9,4,1,6,5]

for i in range(1,len(a)):
    for j in range(i,0,-1):
        if a[j] < a[j-1]:
            a[j],a[j-1] = a[j-1],a[j]
            print(a)
print(a)
print("%d 이(가) 최소값" % a[0])
print("%d 이(가) 최대값" % a[-1])
