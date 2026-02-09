# برنامه اي بنويسيد كه ماتريس متناظر با يك رابطه ترتيب جزئي را از ورودي گرفته
# و ترتيب توپولوژيك متناظر با آن را به خروجي بدهد.

# گرفتن اندازه ماتريس
n = int(input("andazeye matrix ra vared konid: "))

# گرفتن ماتريس رابطه ترتيب جزئي
print("matrix rabete tartib joz'i ra vared konid:")
R = [list(map(int, input().split())) for _ in range(n)]

# محاسبه درجه ورودي (in-degree) هر راس
# اگر j -> i باشد، درجه ورودي i يكي زياد مي‌شود
in_degree = [0] * n

for i in range(n):
    for j in range(n):
        if i != j and R[j][i] == 1:
            in_degree[i] += 1

# ليست رئوس با درجه ورودي صفر
queue = []

for i in range(n):
    if in_degree[i] == 0:
        queue.append(i)

topo = []

# الگوريتم كاهن (Kahn)
while len(queue) > 0:
    v = queue.pop(0)
    topo.append(v)

    # حذف يال‌هاي خروجي v
    for u in range(n):
        if R[v][u] == 1 and v != u:
            in_degree[u] -= 1
            if in_degree[u] == 0:
                queue.append(u)

# چاپ نتيجه
if len(topo) == n:
    print("\nTartib topolojik:")
    for x in topo:
        print(x + 1, end=" ")
else:
    print("\nIn rabete daare cycle ast va tartib topolojik nadarad.")
