import calculator


MAX_GENERAL = 10**9
MAX_HEAVY_M = 10**5


FUNCTIONS_CONFIG = {
    "素数判断": {
        "params": ["n"],
        "func": calculator.is_prime,
        "type": "bool",
        "desc": "判断 n 是否为素数",
    },
    "幂模运算": {
        "params": ["a", "x", "m"],
        "func": calculator.pow_mod,
        "type": "int",
        "desc": "a^x mod m",
    },
    "勒让德符号": {
        "params": ["a", "p"],
        "func": calculator.legendre_symbol,
        "type": "int",
        "desc": "Legendre 符号 (a|p)",
    },
    "欧拉函数": {
        "params": ["n"],
        "func": calculator.euler_phi,
        "type": "int",
        "desc": "φ(n)",
    },
    "模运算": {
        "params": ["a", "m"],
        "func": calculator.mod,
        "type": "int",
        "desc": "a mod m",
    },
    "阶计算": {
        "params": ["a", "m"],
        "func": calculator.order,
        "type": "int",
        "desc": "ord_m(a)",
    },
    "原根计算": {
        "params": ["m"],
        "func": calculator.primitive_root,
        "type": "list",
        "desc": "模 m 的所有原根",
    },
    "逆元计算": {
        "params": ["a", "m"],
        "func": calculator.mod_inverse,
        "type": "int",
        "desc": "a^-1 mod m",
    },
}


LEARNING_CONTENT = {
    "素数判断": "素数：只能被 1 和自身整除的大于 1 的整数。\n\n例如：2、3、5、7、11。\n\n应用：RSA、大整数分解。",
    "幂模运算": "幂模运算：计算 a^x mod m。\n\n通常采用快速幂算法优化。\n\n应用：密码学、Diffie-Hellman。",
    "勒让德符号": "勒让德符号用于判断二次剩余。\n\n(a|p)=1 表示 a 是模 p 的二次剩余。",
    "欧拉函数": "欧拉函数 φ(n)：1~n 中与 n 互素的整数个数。\n\n例如 φ(8)=4。",
    "模运算": "模运算就是求余数。\n\n例如：17 mod 5 = 2。",
    "阶计算": "元素的阶：满足 a^k ≡ 1 (mod m) 的最小正整数 k。",
    "原根计算": "原根：能够生成模 m 所有互素剩余类的数。",
    "逆元计算": "逆元：满足 a*b ≡ 1 (mod m) 的 b。\n\n只有 gcd(a,m)=1 时逆元存在。",
}
