# سوال ۸: ok
# بررسی کنید آیا رابطه ترتیب جزئی است یا خیر.

n = int(input("tedad aazaye majmoee ra vared konid: "))

R = []
for i in range(n):
    R.append(list(map(int, input().split())))

# بازتابی
reflexive = True
for i in range(n):
    if R[i][i] != 1:
        reflexive = False

# پادمتقارن
antisymmetric = True
for i in range(n):
    for j in range(n):
        if i != j and R[i][j] == 1 and R[j][i] == 1:
            antisymmetric = False

# تعدی
transitive = True
for i in range(n):
    for j in range(n):
        for k in range(n):
            if R[i][j] == 1 and R[j][k] == 1 and R[i][k] == 0:
                transitive = False

if reflexive and antisymmetric and transitive:
    print("rabete tartib jozii ast")
else:
    print("rabete tartib jozii nist")
