#if else

# n=int(input())
# if n%2!=0:
#     print("Weird")
# elif n%2==0 and (n>=2 and n<=5):
#     print("Not Weird")
# elif n%2==0 and (n>=6 and n<=20):
#     print("Weird")
# elif n%2==0 and n>20:
#     print("Not Weird")

# ******************************************************

# Arithmetic Operators

# a=int(input())
# b=int(input())
# print(a+b)
# print(a-b)
# print(a*b)

# ******************************************************

# Python: Division

# a=int(input())
# b=int(input())
# print(int(a/b))
# print(float(a/b))

# ******************************************************

# Loops

# n=int(input())
# for i in range(n):
#     print(i*i)
# print("\r")

# ******************************************************

# Write a function

# def is_leap(year):
#     leap = False
#     if year%4==0:
#         leap= True
#         if year%400==0:
#             leap=True
#             if year%100==0:
#                 leap=False
#     return leap

# year = int(input())
# print(is_leap(year))

# ******************************************************

# List Comprehensions

# a=int(input())
# b=int(input())
# c=int(input())
# n=int(input())
# a=a+1
# b=b+1
# c=c+1
# newl=[[A,B,C] for A in range(a) for B in range(b) for C in range(c) if A+B+C!=n]
# print(newl)

# ******************************************************

# Find the Runner-Up Score!


# num=int(input())
# ele=map(int, input().split())

# ele=list(ele) 

# ele.sort()
# newlist1=set(ele)
# newlist1.remove(max(newlist1))
# secondlargest=max(newlist1)
# print(secondlargest)

# ******************************************************

# Nested Lists


# dic={}
# s=list()
# for i in range(int(input())):
#     name=input()
#     score=float(input())
#     if score in dic:
#         dic[score].append(name)
#     else:
#         dic[score]=[name]
#     if score not in s:
#         s.append(score)
# m=min(s)
# s.remove(m)
# m1=min(s)
# dic[m1].sort()
# for i in dic[m1]:
#     print(i)
# print("\n")    
# print(dic.keys())
# print("\n")    
# print(dic.values())


# ******************************************************

# Finding the percentage

# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores

# query_name = input()
# if query_name==name:
#     a=student_marks[query_name]
#     sum_a=sum(a)
#     avg=sum_a/3
#     print("%.2f"%(avg))


# ******************************************************

# Lists


# l=list()
# n=int(input())
# for i in range(0,n):
#     commands = input()
#     if "insert" in commands:
#         val=commands.split(" ")
#         l.insert(int(val[1]), int(val[2]))
#     elif "print" in commands:
#         print(l)
#     elif "remove" in commands:
#         val=commands.split(" ")
#         l.remove(int(val[1]))
#     elif "append" in commands:
#         val=commands.split(" ")
#         l.append(int(val[1]))
#     elif "sort" in commands:
#         l.sort()
#     elif "pop" in commands:
#         l.pop()
#     elif "reverse" in commands:
#         l.reverse()
#     else:
#         print("Input Incorrect")

# ******************************************************
    
# Tuples   


# n = int(input())
# integer_list = map(int, input().split())
# t=tuple(integer_list)
# print(hash(t))
