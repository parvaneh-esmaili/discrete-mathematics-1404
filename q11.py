# برنامه اي بنويسيد كه ماتريس متناظر با يك رابطه ترتيب جزئي را از ورودي گرفته
# و يال هاي نمودار هاس متناظر با آن را چاپ كند.

# گرفتن اندازه ماتريس
n = int(input("andazeye matrix ra vared konid: "))

# گرفتن ماتريس رابطه
print("matrix rabete tartib joz'i ra vared konid:")
R = [list(map(int, input().split())) for _ in range(n)]

print("\nYal haye nemudar Hasse:")

# پيدا كردن يال هاي نمودار هاس
# يال (i , j) در هاس است اگر:
# 1) R[i][j] = 1
# 2) i != j
# 3) هيچ k اي وجود نداشته باشد كه i -> k و k -> j

for i in range(n):
    for j in range(n):
        if i != j and R[i][j] == 1:
            cover = True
            for k in range(n):
                if k != i and k != j:
                    if R[i][k] == 1 and R[k][j] == 1:
                        cover = False
                        break
            if cover:
                print(i + 1, "->", j + 1)
