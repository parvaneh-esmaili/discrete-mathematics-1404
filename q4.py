
# برنامه ای بنویسید که ماتریس متناظر با یک رابطه را از ورودی گرفته ok
# و گراف جهت دار متناظر با آن را ترسیم نماید.

n = int(input("andazeye matrix ra vared konid: "))

# گرفتن ماتریس رابطه
print("matrix rabete ra vared konid:")
R = [list(map(int, input().split())) for _ in range(n)]

print("\nYal haye graf jahat-dar:")

# بررسی درایه‌های ماتریس و چاپ یال‌ها
for i in range(n):
    for j in range(n):
        if R[i][j] == 1:
            print(f"{i} -> {j}")
