# سوال ۱:
# جدول درستی AND و OR را نمایش دهید.

A = [0, 1]
B = [0, 1]

print("AND")
for a in A:
    for b in B:
        print(a, b, a and b)

print("OR")
for a in A:
    for b in B:
        print(a, b, a or b)
