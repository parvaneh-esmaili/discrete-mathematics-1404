# برنامه اي بنويسيد كه ماتريس متناظر با يك رابطه را از ورودي گرفته
# و بستارهاي بازتابي، تقارني و تراكنشي (ترانزيتيو) آن را محاسبه و چاپ كند.

# گرفتن اندازه ماتريس
n = int(input("andazeye matrix ra vared konid: "))

# گرفتن ماتريس رابطه
print("matrix rabete ra vared konid:")
R = [list(map(int, input().split())) for _ in range(n)]

# ----------------------
# بستار بازتابي (Reflexive Closure)
# ----------------------
reflexive_closure = [row[:] for row in R]
for i in range(n):
    reflexive_closure[i][i] = 1

# ----------------------
# بستار تقارني (Symmetric Closure)
# ----------------------
symmetric_closure = [row[:] for row in R]
for i in range(n):
    for j in range(n):
        if R[i][j] == 1:
            symmetric_closure[j][i] = 1

# ----------------------
# بستار تراكنشي (Transitive Closure)
# الگوريتم Floyd–Warshall براي محاسبه R+
# ----------------------
transitive_closure = [row[:] for row in R]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if transitive_closure[i][j] or (transitive_closure[i][k] and transitive_closure[k][j]):
                transitive_closure[i][j] = 1

# ----------------------
# چاپ نتايج
# ----------------------
print("\nBastar baztabi:")
for row in reflexive_closure:
    print(*row)

print("\nBastar tagharoni:")
for row in symmetric_closure:
    print(*row)

print("\nBastar terayayi (transitive):")
for row in transitive_closure:
    print(*row)
