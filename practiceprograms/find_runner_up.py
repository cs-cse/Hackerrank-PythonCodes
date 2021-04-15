# Find the Runner-Up Score!


num=int(input())
ele=map(int, input().split())

ele=list(ele) 

ele.sort()
newlist1=set(ele)
newlist1.remove(max(newlist1))
secondlargest=max(newlist1)
print(secondlargest)
