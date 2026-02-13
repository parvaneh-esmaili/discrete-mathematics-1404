# برنامه اي بنويسيد كه ماتريس متناظر با يك رابطه را از ورودي گرفته
# و بستارهاي بازتابي، تقارني و تعدي آن را محاسبه و چاپ كند.

n = int(input("andazeye matrix ra vared konid: "))

print("matrix rabete ra vared konid:")
R = []
for i in range(n):
    row = list(map(int, input().split()))
    R.append(row)


# بستار بازتابي

reflexive = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        reflexive[i][j] = R[i][j]

for i in range(n):
    reflexive[i][i] = 1


# بستار تقارني

symmetric = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if R[i][j] == 1 or R[j][i] == 1:
            symmetric[i][j] = 1


# بستار تعدي (وارشال)

transitive = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        transitive[i][j] = R[i][j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if transitive[i][k] == 1 and transitive[k][j] == 1:
                transitive[i][j] = 1





print("\nBastar baztabi:")
for row in reflexive:
    print(*row)

print("\nBastar tagharoni:")
for row in symmetric:
    print(*row)

print("\nBastar ta'di (transitive):")
for row in transitive:
    print(*row)
