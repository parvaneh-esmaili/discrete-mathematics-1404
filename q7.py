# سوال ۷: ok
# بررسی کنید آیا رابطه پادمتقارن است یا خیر.

# n = int(input("tedad aazaye majmoee ra vared konid: "))

# R = []
# for i in range(n):
#     R.append(list(map(int, input().split())))

# antisymmetric = True
# for i in range(n):
#     for j in range(n):
#         if i != j and R[i][j] == 1 and R[j][i] == 1:
#             antisymmetric = False

# if antisymmetric:
#     print("rabete pad-motagharen ast")
# else:
#     print("rabete pad-motagharen nist")




# برنامه اي بنويسيد كه ماتريس متناظر با يك رابطه را از ورودي گرفته
# و ماتريس هاي متناظر با متمم و معكوس آن را به خروجي بدهد.

# گرفتن اندازه ماتريس
n = int(input("andazeye matrix ra vared konid: "))

# گرفتن ماتريس رابطه
print("matrix rabete ra vared konid:")
R = [list(map(int, input().split())) for _ in range(n)]

# محاسبه ماتريس متمم
# اگر R[i][j] = 0 باشد، در متمم 1 مي‌شود و برعكس
MOTAMAM = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if R[i][j] == 0:
            MOTAMAM[i][j] = 1
        else:
            MOTAMAM[i][j] = 0

# محاسبه ماتريس معكوس (ترانهاده)
# جايگزيني سطرها با ستون‌ها
MAKOOS = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        MAKOOS[j][i] = R[i][j]

# چاپ نتايج
print("\nMatrise Motamam:")
for row in MOTAMAM:
    print(row)

print("\nMatrise Makoos:")
for row in MAKOOS:
    print(row)
