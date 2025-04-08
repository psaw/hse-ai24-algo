from array import array

yy, xx = map(lambda x: int(x), input().split())

m = []
for _ in range(yy):
    m.append(array('B', list([int(x) for x in input().split()])))

# print(m)

smax = 1 # искомый макс размер квадрата. 1 гарантировано есть

def is_square(m, x, y, size) -> bool:
    for dy in range(size):
        if sum(m[y+dy][x:x+size]) != size:
            return False
    return True


for s in range(2, min(xx, yy)+1):
    for y in range(yy-s+1):
        for x in range(xx-s+1):
            if is_square(m, x, y, s):
                smax = s
    if smax != s:
        break

print(smax)