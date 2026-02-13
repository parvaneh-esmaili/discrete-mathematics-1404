# سوال ۲: 
# یک رابطه را گرفته و ماتریس آن را بسازید.

n = int(input("tedad aazaye majmoee ra vared konid: "))
m = int(input("tedad zoje moratab hara vared konid: "))

R = []
print("zoj ha ra vared konid:")
for i in range(m):
    R.append(map(int, input().split()))

MATRIS = [[0]*n for x in range(n)]

for i, j in R:
    MATRIS[i-1][j-1] = 1

for row in MATRIS:
    print(row)


