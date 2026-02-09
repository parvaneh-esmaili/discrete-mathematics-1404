# سوال ۲: ok
# یک رابطه را گرفته و ماتریس آن را بسازید.

n = int(input("tedad aazaye majmoee ra vared konid: "))
m = int(input("tedad zoje moratab hara vared konid: "))

R = []
print("zoj ha ra vared konid:")
for i in range(m):
    a, b = map(int, input().split())
    R.append((a, b))

matrix = [[0]*n for x in range(n)]

for a, b in R:
    matrix[a-1][b-1] = 1

for row in matrix:
    print(row)


