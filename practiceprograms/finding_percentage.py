
# Finding the percentage

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
if query_name==name:
    a=student_marks[query_name]
    sum_a=sum(a)
    avg=sum_a/3
    print("%.2f"%(avg))