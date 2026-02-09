# سوال 3: ok
# _ برنامه ای بنویسید که دو ماتریس بولی را از ورودی گرفته
#  و در صورت امکان ماتریس وست و ماتریس رسند و ماتریس
#  حاصل ضرب بولی را به خروجی بدهد.
n = int(input("andazeye matrix ra vared konid: "))

print("matrix A:")
A = [list(map(int, input().split())) for x in range(n)]

print("matrix B:")
B = [list(map(int, input().split())) for x in range(n)]

AND = [[A[i][j] & B[i][j] for j in range(n)] for i in range(n)]

OR = [[A[i][j] | B[i][j] for j in range(n)] for i in range(n)]

C = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] |= A[i][k] & B[k][j]

print("\nMatrise AND:")
for row in AND:
    print(row)

print("\nMatrise OR:")
for row in OR:
    print(row)

print("\nMatrise Zarb Booli:")
for row in C:
    print(row)
