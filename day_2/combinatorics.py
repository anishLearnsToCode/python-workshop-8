a = 10

def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# permutation nPr = n! / (n -r)!
def permutation(n: int, r: int) -> int:
    assert type(n) == int
    assert type(r) == int
    assert n > 0
    assert r > 0
    assert n > r
    return factorial(n) // factorial(n - r)


# combination nCr = nPr / r!
def combination(n: int, r: int) -> int:
    return permutation(n, r) // factorial(r)
