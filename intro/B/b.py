max1, max2 = 0, 0

while True:
    n = int(input())
    if n == 0: 
        break
    if n >= max1:
        max2, max1 = max1, n
    elif n > max2 and n != max1:
        max2 = n
# if max2 == 0:
#     max2 = max1

print(max1)
print(max2)
