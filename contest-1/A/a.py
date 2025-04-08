N = int(input())

# too slow
def tree_size_recursive(n: int) -> int:
    if n == 0:
        return 1
    else:
        return 2*n + 2 + tree_size_recursive(n-1)
    
# too slow
def tree_size(n: int) -> int:
    size = 1
    for i in range(1, n+1):
        size += 2*i + 2
    return size

# too slow
def tree_size2(n: int) -> int:
    size = 1
    while n > 0:
        size += 2*n + 2
        n -= 1
    return size

# OK
def tree_size3(n: int) -> int:
    return n*(n+3)+1

print(tree_size3(N))