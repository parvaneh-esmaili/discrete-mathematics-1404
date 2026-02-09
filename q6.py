# برنامه اي بنويسيد كه ماتريس متناظر با دو رابطه را از ورودي گرفته
# و ماتريس متناظر با تركيب آن ها را به خروجي بدهد.

# گرفتن اندازه ماتريس
n = int(input("andazeye matrix ra vared konid: "))

# گرفتن ماتريس رابطه اول
print("matrix rabete aval ra vared konid:")
R1 = [list(map(int, input().split())) for _ in range(n)]

# گرفتن ماتريس رابطه دوم
print("matrix rabete dovom ra vared konid:")
R2 = [list(map(int, input().split())) for _ in range(n)]

# ايجاد ماتريس تركيب (ابتدا همه صفر)
C = [[0]*n for x in range(n)]

# محاسبه تركيب دو رابطه
# اگر براي حداقل يک k داشته باشيم:
# R1[i][k] = 1 و R2[k][j] = 1
# آنگاه C[i][j] = 1
for i in range(n):
    for j in range(n):
        for k in range(n):
            if R1[i][k] == 1 and R2[k][j] == 1:
                C[i][j] = 1
                break

print("\nMatrise tarkib:")
for row in C:
    print(row)
