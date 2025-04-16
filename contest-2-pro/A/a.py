# Найдите такое число x что x**2 + sqrt(x) = C, с точностью не менее 6 знаков после точки.

def findX(C, eps=1e-7):
    left = 1.0
    right = C / 2
    while right - left > eps:
        x = (right + left) / 2
        val = x**2 + x**0.5
        if val < C:
            left = x
        else:
            right = x
    return round((right + left) / 2, 6)

print(findX(float(input())))

            