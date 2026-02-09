# برنامه اي بنويسيد كه ماتريس متناظر با يك رابطه ترتيب جزئي را از ورودي گرفته
# و مشخص كند كه آيا آن رابطه يك ترتيب كامل هست يا خير.

# گرفتن اندازه ماتريس
n = int(input("andazeye matrix ra vared konid: "))

# گرفتن ماتريس رابطه ترتيب جزئي
print("matrix rabete tartib joz'i ra vared konid:")
R = [list(map(int, input().split())) for _ in range(n)]

# بررسي مقايسه‌پذيري (Totality / Comparability)
# براي هر دو عنصر متفاوت i و j بايد:
# يا i <= j باشد يا j <= i

total = True

for i in range(n):
    for j in range(n):
        if i != j:
            if R[i][j] == 0 and R[j][i] == 0:
                total = False
                break

# نتيجه نهايي
if total:
    print("\nIn rabete yek tartib kamel ast.")
else:
    print("\nIn rabete tartib kamel nist.")
