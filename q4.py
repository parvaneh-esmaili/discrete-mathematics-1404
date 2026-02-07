# سوال ۴:
# بررسی کنید آیا رابطه تقارنی است یا خیر.

n = int(input("n ra vared konid: "))

R = []
for i in range(n):
    R.append(list(map(int, input().split())))

symmetric = True
for i in range(n):
    for j in range(n):
        if R[i][j] != R[j][i]:
            symmetric = False

if symmetric:
    print("rabete tagharoni ast")
else:
    print("rabete tagharoni nist")
