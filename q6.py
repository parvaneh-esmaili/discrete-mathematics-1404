# برنامه اي بنويسيد كه ماتريس متناظر با دو رابطه را از ورودي گرفته
# و ماتريس متناظر با تركيب آن‌ها را به خروجي بدهد.

n = int(input("andazeye matrix ra vared konid: "))

print("matrix rabete aval ra vared konid:")
R1 = []
for i in range(n):
    row = list(map(int, input().split()))
    R1.append(row)

print("matrix rabete dovom ra vared konid:")
R2 = []
for i in range(n):
    row = list(map(int, input().split()))
    R2.append(row)

C = [[0]*n for x in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if R1[i][k] == 1 and R2[k][j] == 1:
                C[i][j] = 1
                break

print("\nMatrise tarkib:")
for row in C:
    print(row)
