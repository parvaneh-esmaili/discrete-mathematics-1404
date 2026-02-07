# سوال ۷:
# بررسی کنید آیا رابطه پادمتقارن است یا خیر.

n = int(input("n ra vared konid: "))

R = []
for i in range(n):
    R.append(list(map(int, input().split())))

antisymmetric = True
for i in range(n):
    for j in range(n):
        if i != j and R[i][j] == 1 and R[j][i] == 1:
            antisymmetric = False

if antisymmetric:
    print("rabete pad-motagharen ast")
else:
    print("rabete pad-motagharen nist")
