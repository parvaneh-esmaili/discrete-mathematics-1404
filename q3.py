# سوال ۳:
# بررسی کنید آیا رابطه بازتابی است یا خیر.

n = int(input("n ra vared konid: "))

R = []
for i in range(n):
    R.append(list(map(int, input().split())))

reflexive = True
for i in range(n):
    if R[i][i] != 1:
        reflexive = False

if reflexive:
    print("rabete baztabi ast")
else:
    print("rabete baztabi nist")
