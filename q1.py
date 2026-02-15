# سوال 1 ok
#  : جدول درستی گزاره مرکب

op = input("amalgar ra vared konid (and / or): ")

values = [1 , 0]

print("p q | result")
print("------------")

for i in values:
    for j in values:
        if op == "and":
            result = i and j
        else:
            result = i or j
        print(i, j, "|", result)
