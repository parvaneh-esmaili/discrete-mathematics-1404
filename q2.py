# سوال ۲:
# یک رابطه را گرفته و ماتریس آن را بسازید.

n = int(input("n ra vared konid: "))
m = int(input("m ra vared konid: "))

R = []
print("zojha ra vared konid:")
for i in range(m):
    a, b = map(int, input().split())
    R.append((a, b))

matrix = [[0]*n for _ in range(n)]

for a, b in R:
    matrix[a-1][b-1] = 1

for row in matrix:
    print(row)
