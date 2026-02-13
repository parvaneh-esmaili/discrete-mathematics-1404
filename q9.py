# سوال 9
# برنامه‌ای بنویسید که ماتریس یک رابطه را گرفته
# متمم رابطه و معکوس رابطه را محاسبه و چاپ کند.

n = int(input("andazeye matrix ra vared konid: "))

print("matrix rabete ra vared konid:")
R = []
for i in range(n):
    R.append(list(map(int, input().split())))


complement = [[0]*n for x in range(n)]

for i in range(n):
    for j in range(n):
        if R[i][j] == 0:
            complement[i][j] = 1
        else:
            complement[i][j] = 0



inverse = [[0]*n for x in range(n)]

for i in range(n):
    for j in range(n):
        inverse[i][j] = R[j][i]


print("\nMotammam rabete:")
for row in complement:
    print(*row)

print("\nMa'koos rabete:")
for row in inverse:
    print(*row)
