n_lines, n_points = map(lambda x: int(x), input().split())

lines = []
for i in range(n_lines):
    lines.append(tuple(map(lambda x: int(x), input().split())))

# print(n_lines, n_points)
# print(lines)

for p in input().split():
    pp = int(p)
    count = 0
    for line in lines:
        if line[0] <= pp <= line[1]:
            count+=1
    print(count, end=" ")
