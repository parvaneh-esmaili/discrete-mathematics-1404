# سوال ۵:
# بررسی کنید آیا رابطه داده‌شده هم‌ارزی است یا خیر.

n = int(input("tedad aazaye majmoee ra vared konid: "))


print("matrix rabete ra vared konid:")
R = []
for i in range(n):
    row = list(map(int, input().split()))
    R.append(row)

# بازتابی
reflexive = True
for i in range(n):
    if R[i][i] != 1:
        reflexive = False

# تقارنی
symmetric = True
for i in range(n):
    for j in range(n):
        if R[i][j] != R[j][i]:
            symmetric = False

# تعدی
transitive = True
for i in range(n):
    for j in range(n):
        if R[i][j] == 1:
            for k in range(n):
                if R[j][k] == 1 and R[i][k] != 1:
                    transitive = False


if reflexive and symmetric and transitive:
    print("rabete ham-arzi ast")
else:
    print("rabete ham-arzi nist")
