# برنامه اي بنويسيد كه ماتريس متناظر با يك رابطه را از ورودي گرفته
# و ماتريس هاي متناظر با متمم و معكوس آن را به خروجي بدهد.

n = int(input("andazeye matrix ra vared konid: "))

print("matrix rabete ra vared konid:")
R = []
for i in range(n):
    row = list(map(int, input().split()))
    R.append(row)

MOTAMAM = [[0]*n for x in range(n)]
for i in range(n):
    for j in range(n):
        if R[i][j] == 0:
            MOTAMAM[i][j] = 1
        else:
            MOTAMAM[i][j] = 0

MAKOOS = [[0]*n for x in range(n)]
for i in range(n):
    for j in range(n):
        MAKOOS[j][i] = R[i][j]

print("\nMatrise Motamam:")
for row in MOTAMAM:
    print(row)

print("\nMatrise Makoos:")
for row in MAKOOS:
    print(row)
