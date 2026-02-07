# سوال ۶:
# بررسی کنید آیا رابطه تعدی است یا خیر.

n = int(input("n ra vared konid: "))

R = []
for i in range(n):
    R.append(list(map(int, input().split())))

transitive = True
for i in range(n):
    for j in range(n):
        for k in range(n):
            if R[i][j] == 1 and R[j][k] == 1 and R[i][k] == 0:
                transitive = False

if transitive:
    print("rabete taadi ast")
else:
    print("rabete taadi nist")
