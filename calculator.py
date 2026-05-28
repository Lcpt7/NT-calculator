import math


# 模运算
def mod(a: int, m: int):
    return a % m


# 幂模运算
def pow_mod(a: int, x: int, m: int):
    return pow(a, x, m)


# 判断素数
def is_prime(n: int):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


# 勒让德符号
def legendre_symbol(a: int, p: int):
    if not is_prime(p) or p == 2:
        raise ValueError("请输入奇素数 p")

    res = pow(a, (p - 1) // 2, p)
    if res == 0:
        return 0
    return 1 if res == 1 else -1


# 欧拉函数
def euler_phi(n: int):
    if n <= 0:
        raise ValueError("请输入正整数 n")

    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


# 获取因子
def getfactors(n: int):
    if n <= 0:
        raise ValueError("请输入正整数 n")

    factors = []
    limit = math.isqrt(n)
    for i in range(1, limit + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)


# 获取素因子
def prime_factors(n: int):
    if n <= 0:
        raise ValueError("请输入正整数 n")

    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2

    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.add(p)
            n //= p
        p += 2

    if n > 1:
        factors.add(n)
    return factors


# 计算阶
def order(a: int, m: int):
    if a <= 0:
        raise ValueError("请输入正整数 a")
    if m <= 1:
        raise ValueError("请输入大于 1 的整数 m")
    if math.gcd(a, m) != 1:
        raise ValueError("a 和 m 必须互素")

    factors = getfactors(euler_phi(m))
    for x in factors:
        if pow(a, x, m) == 1:
            return x
    return None


# 判断是否有原根
def has_primitive_root(m: int):
    if m == 2 or m == 4:
        return True
    if m <= 1:
        return False

    n = m
    if n % 2 == 0:
        n //= 2
        if n % 2 == 0:
            return False

    for p in range(3, math.isqrt(n) + 1, 2):
        if n % p == 0:
            if not is_prime(p):
                return False
            while n % p == 0:
                n //= p
            return n == 1
    return is_prime(n)


# 求所有原根
def primitive_root(m: int):
    if not has_primitive_root(m):
        return None

    phi_m = euler_phi(m)
    factors = prime_factors(phi_m)
    powers = sorted(phi_m // factor for factor in factors)

    generator = None
    for i in range(1, m):
        if math.gcd(i, m) != 1:
            continue
        if all(pow(i, power, m) != 1 for power in powers):
            generator = i
            break

    if generator is None:
        return None

    roots = []
    for d in range(1, phi_m + 1):
        if math.gcd(d, phi_m) == 1:
            roots.append(pow(generator, d, m))
    return sorted(roots)


# 求逆元
def mod_inverse(a: int, m: int):
    if math.gcd(a, m) != 1:
        raise ValueError("a 和 m 必须互素")
    return pow(a, -1, m)
