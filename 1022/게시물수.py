m = int(input("총페이지 건수:"))
n =  int(input("보여줄 페이지 건수:"))


def getTotalPage(m, n):
    if m & n == 0:
        return (m //n)
    else:
        return (m //n)+1

print(getTotalPage(m, n))
