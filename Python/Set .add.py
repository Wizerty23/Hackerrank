# Enter your code here. Read input from STDIN. Print output to STDOUT

s = set("")
n = int(input())
for _ in range(n):
    s.add(input())

print(len(s))
