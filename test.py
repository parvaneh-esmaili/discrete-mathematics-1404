# n = int(input('enter the size of the matris: '))

# m = []

# print('enter matris: ')

# for i in range(n):
#     s = list(map(int, input().split()))
#     m.append(s)



# tagaroni = [[0] * n for i in range(n)]

# for i in range(n):
#     for j in range(n):

#         if m[i][j] == 1 or m[j][i] == 1:
#             tagaroni[j][i] = 1



# for s in tagaroni:
#     print(s)


# matris =input()

# print (matris)



n = int(input('enter the size of the matris: '))

m1 = []

print('enter first matris: ')
for i in range(n):
    m1.append(list(map(int, input().split())))


m2 = []
print('enter second matris: ')
for i in range(n):
    m2.append(list(map(int, input().split())))


# for i in m2:
#     print(i)

# print()

# for i in m1:
#     print(i)

AND = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        AND[i][j] = m1[i][j] + m2[i][j]
      

for i in AND:
    print(i)        