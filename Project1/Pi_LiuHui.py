import math
def pi_LiuHui(epsilon):
    n = 6   # Sequence starts at hexagon, n-sided polygon, n = 6, 6 sided -> hexagon
    i = 1   # Incrementor for Lists
    r = 1   # Default, Radius = 1
    m = [r] # m_6 = radius = 1     (m_n is length of a side of an n-sided polygon)
    a = [0] # A_6 = 0  (This is the Area of n-sided polygon in circle of radius r)
    print(f"Epsilon = {epsilon}")
    print("i        m(n)             A(n)")
    # Print with formatting (for 0 index)
    print("{0:d}       {1:09.8f}     {2:9.8f}".format(n, m[i - 1], a[i - 1]))
    while 1:
        # m_2n = sqrt((m_n/2)^2 + (r - sqrt(r^2 - ((m_n)^2)/4))^2)
        m.append(math.sqrt((m[i - 1] / 2) ** 2 + (r - math.sqrt(r ** 2 - (m[i - 1] ** 2) / 4)) ** 2))
        # Used to keep lists same starting size
        if i == 1:
            # A_12 = 3 * m_6 * radius
            a.append(3 * m[0] * r)
        else:
            # A_2n = A_12 * 2^i * m_n
            a.append(a[1] * 2 **(i-1) * m[i-1])
        # Increment by 2*n
        n = n * 2
        # Print with formatting
        print("{0:d}       {1:09.8f}     {2:9.8f}".format(n, m[i], a[i]))
        # Delay by one cycle
        if abs(a[i] - a[i-1]) < epsilon:
            break
        # Increment
        i = i + 1

    # Calculate Percent Error by comparing to math.pi (Most accurate pi value)
    error = abs((a[i] - math.pi)/math.pi) * 100

    return a[i], error
