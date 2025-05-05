max_9, max_10, max_11 = 0, 0, 0

with open("input.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    while line:
        _, _, C, G = line.split()
        match C:
            case "9":
                max_9 = max(max_9, int(G))
            case "10":
                max_10 = max(max_10, int(G))
            case "11":
                max_11 = max(max_11, int(G))
        line = f.readline()

print(max_9, max_10, max_11)
