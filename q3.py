# سوال 3:
# _ برنامه ای بنویسید که دو ماتریس بولی را از ورودی گرفته
#  و در صورت امکان ماتریس وست و ماتریس رسند و ماتریس
#  حاصل ضرب بولی را به خروجی بدهد.

n = int(input("andazeye matrix ra vared konid: "))

print("matrix A:")
A = []
for i in range(n):
    A.append(list(map(int, input().split())))

print("matrix B:")
B = []
for i in range(n):
    B.append(list(map(int, input().split())))

# ---------------- AND ----------------
AND = [[0]*n for x in range(n)]
for i in range(n):
    for j in range(n):
        AND[i][j] = A[i][j] & B[i][j]  


# ---------------- WAST ----------------
WAST = [[0]*n for x in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if A[i][k] == 1 or B[k][j] == 1:
                WAST[i][j] = 1
                break


# ---------------- RESAND ----------------
RASAND = [[0]*n for x in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if A[i][k] == 1 and B[k][j] == 1:
                RASAND[i][j] = 1



print("\nMatrise AND:")
for row in AND:
    print(row)


print("\nMatrise WEST:")
for row in WAST:
    print(row)


print("\nMatrise RESAND (Reachability):")
for row in RASAND:
    print(row)
