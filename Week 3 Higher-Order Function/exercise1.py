# Make a summation give a closer approximation to the Pi value when the number of terms increases.

def pi_term(k):
    return 8 / ((4 * k - 3) * (4 * k - 1))


def summation(n, term):
    """Sum the first N terms of a sequence.
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


print(summation(10000000, pi_term))
