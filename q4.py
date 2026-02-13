
# برنامه ای بنویسید که ماتریس متناظر با یک رابطه را از ورودی گرفته ok
# و گراف جهت دار متناظر با آن را ترسیم نماید.

n = int(input("andazeye matrix ra vared konid: "))

print("matrix rabete ra vared konid:")
R = []
for i in range(n):
    row = list(map(int, input().split()))
    R.append(row)

print("\nYal haye graf jahat-dar:")

for i in range(n):
    for j in range(n):
        if R[i][j] == 1:
            print(f"{i + 1} -> {j + 1}")
