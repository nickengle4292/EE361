import math

def pi_LiuHui(epsilon):
    r = 1.0
    n = 6
    A = r ** 2 * n * 0.5
    while True:
        m = math.sqrt(r ** 2 - ((r / 2) ** 2))
        B = m * r * 0.5
        n *= 2
        A_new = n * B
        if abs(A_new - A) < epsilon:
            return n * math.sin(math.pi / n)
        A = A_new
        r = math.sqrt(r ** 2 - (m ** 2))

print(pi_LiuHui(0.000001))  # should be close to 3.141593