# List Comprehensions

a=int(input())
b=int(input())
c=int(input())
n=int(input())
a=a+1
b=b+1
c=c+1
newl=[[A,B,C] for A in range(a) for B in range(b) for C in range(c) if A+B+C!=n]
print(newl)