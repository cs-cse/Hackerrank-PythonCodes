# Nested Lists


dic={}
s=list()
for i in range(int(input())):
    name=input()
    score=float(input())
    if score in dic:
        dic[score].append(name)
    else:
        dic[score]=[name]
    if score not in s:
        s.append(score)
m=min(s)
s.remove(m)
m1=min(s)
dic[m1].sort()
for i in dic[m1]:
    print(i)
print("\n")    
print(dic.keys())
print("\n")    
print(dic.values())