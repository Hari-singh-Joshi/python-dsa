n = 4
res = []
s = ""

for i in range(n + 1):
    s = ""
    for j in range(n - i):
        s = s + str(j + 1)
    res.append(s)

return res
