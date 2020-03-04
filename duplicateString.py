names = []
n = int(input("How many Names"));
for i in range(n):
    names.append(input())
s = set(names)
names = list(s)
for x in names:
    print(x)