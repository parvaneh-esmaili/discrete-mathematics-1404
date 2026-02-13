
# برنامه اي بنويسيد كه ماتريس متناظر با يك رابطه را از ورودي گرفته
# سپس دو انديس كه متناظر با سطرهاي آن هستند از كاربر بگيرد
# و مشخص كند كه آيا بين آن دو انديس مسيري به طول 3 وجود دارد يا خير.

# برنامه‌ای که بررسی می‌کند آیا بین دو اندیس مسیر طول 3 وجود دارد یا نه

n = int(input("andazeye matrix ra vared konid: "))

print("matrix rabete ra vared konid:")
R = []
for i in range(n):
    R.append(list(map(int, input().split())))

a = int(input("shomare andis mabda ra vared konid: "))
b = int(input("shomare andis maghsad ra vared konid: "))



R2 = [[0]*n for x in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if R[i][k] == 1 and R[k][j] == 1:
                R2[i][j] = 1
                break



R3 = [[0]*n for x in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if R2[i][k] == 1 and R[k][j] == 1:
                R3[i][j] = 1
                break



if R3[a][b] == 1:
    print("beyn in do andis masire tool 3 vojood darad.")
else:
    print("masire tool 3 vojood nadarad.")
