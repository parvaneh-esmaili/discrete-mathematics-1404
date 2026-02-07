# سوال 10:
# برنامه‌ای بنویسید که با استفاده از ضرب بولی ماتریس‌ها
# بررسی کند آیا بین دو راس مسیر به طول 3 وجود دارد یا خیر.

n = int(input("Enter number of vertices: "))

matrix = []
print("Enter adjacency matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

def boolean_multiply(A, B):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if A[i][k] == 1 and B[k][j] == 1:
                    result[i][j] = 1
                    break
    return result

# محاسبه A^3
A2 = boolean_multiply(matrix, matrix)
A3 = boolean_multiply(A2, matrix)

u = int(input("Enter start vertex (0-based): "))
v = int(input("Enter end vertex (0-based): "))

if A3[u][v] == 1:
    print("Masir ba tool 3 vojood darad")
else:
    print("Masir ba tool 3 vojood nadarad")
