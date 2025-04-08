import collections

def solve(file: str):
    n = int(input())
    c = [int(s) for s in input().split()]
    k = int(input())
    press = [int(s) for s in input().split()]
    # with open(file, 'r') as f:
    #     n = int(f.readline())
    #     c = [int(s) for s in f.readline().split()]
    #     k = int(f.readline())
    #     press = [int(s) for s in f.readline().split()]
    
    cc = collections.Counter(press)

    print(f"{n=}\n{c=}\n{k=}\n{press=}")
    print(cc)
    for i in range(1, n+1, 1):
        if cc.get(i,0) > c[i-1]:
            print("yes")
        else:
            print("no")        


if __name__ == "__main__":
    print("="*10)
    solve("input1.txt")
    # print("="*10)
    # solve("input2.txt")

    