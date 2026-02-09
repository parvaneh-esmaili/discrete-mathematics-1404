
# ok
# برنامه اي بنويسيد كه ماتريس متناظر با يك رابطه را از ورودي گرفته
# سپس دو انديس كه متناظر با سطرهاي آن هستند از كاربر بگيرد
# و مشخص كند كه آيا بين آن دو انديس مسيري به طول 3 وجود دارد يا خير.

# گرفتن اندازه ماتريس
n = int(input("andazeye matrix ra vared konid: "))

# گرفتن ماتريس رابطه
print("matrix rabete ra vared konid:")
R = [list(map(int, input().split())) for _ in range(n)]

# گرفتن انديس هاي مبدا و مقصد
a = int(input("shomare andis mabda ra vared konid: "))
b = int(input("shomare andis maghsad ra vared konid: "))

# محاسبه R^3 (حاصل ضرب بولي سه‌باره)
# ابتدا ضرب اول R * R => R2
R2 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            R2[i][j] |= R[i][k] & R[k][j]

# سپس ضرب دوم R2 * R => R3
R3 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            R3[i][j] |= R2[i][k] & R[k][j]

# بررسي وجود مسير طول 3 بين a و b
if R3[a][b] == 1:
    print("beyn in do andis masire tool 3 vojood darad.")
else:
    print("masire tool 3 vojood nadarad.")
