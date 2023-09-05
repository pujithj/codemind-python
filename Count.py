n = int(input())
List = list(map(int,input().split()))
l = [0,0]
for i in List:
    if i % 2 == 0:
        l[0] += 1
    else:
        l[1] += 1
print(l[0],l[1])