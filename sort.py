# vim:fileencoding=utf-8

lst = []

f = open("memoca.csv", "r")

for i in f:
    lst.append(i)

f.flush()
f.close()

f = open("bkup_memoca.csv", "w")

for k in lst:
    f.write(k)

f.flush()
f.close()

lst.sort()

f = open("memoca.csv", "w")

for j in lst:
    f.write(j)
    print(j.split("\n")[0])

f.flush()
f.close()

