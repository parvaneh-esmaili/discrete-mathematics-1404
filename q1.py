# سوال 1 ok
#  : جدول درستی گزاره مرکب

op = input("amalgar ra vared konid (and / or): ")

values = [1 , 0]

print("p q | result")
print("------------")

for p in values:
    for q in values:
        if op == "and":
            result = p and q
        else:
            result = p or q

        print(p, q, "|", result)
