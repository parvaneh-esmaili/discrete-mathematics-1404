# سوال 9:
# برنامه‌ای بنویسید که ماتریس یک رابطه را گرفته و
# متمم رابطه و معکوس رابطه را محاسبه و چاپ کند.

n = int(input("Enter size of matrix: "))

matrix = []
print("Enter matrix rows (0 or 1):")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# متمم رابطه
complement = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(1 - matrix[i][j])
    complement.append(row)

# معکوس رابطه (ترانهاده)
inverse = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix[j][i])
    inverse.append(row)

print("\nComplement matrix:")
for row in complement:
    print(row)

print("\nInverse matrix:")
for row in inverse:
    print(row)
