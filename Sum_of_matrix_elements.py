m = int(input())
n = int(input())
l = []
for i in range(1,m + 1):
    List = list(map(int,input().split()))
    l.append(sum(List))
print(sum(l))