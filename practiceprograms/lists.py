# Lists


l=list()
n=int(input())
for i in range(0,n):
    commands = input()
    if "insert" in commands:
        val=commands.split(" ")
        l.insert(int(val[1]), int(val[2]))
    elif "print" in commands:
        print(l)
    elif "remove" in commands:
        val=commands.split(" ")
        l.remove(int(val[1]))
    elif "append" in commands:
        val=commands.split(" ")
        l.append(int(val[1]))
    elif "sort" in commands:
        l.sort()
    elif "pop" in commands:
        l.pop()
    elif "reverse" in commands:
        l.reverse()
    else:
        print("Input Incorrect")