# Make this code DRY

def same_length(a, b):
    """Return whether positive integers a and b have the same number of digits."""
    return find_length(a) == find_length(b)


def find_length(x):
    x_digits = 0
    while x > 0:
        x = x // 10
        x_digits = x_digits + 1
    return x_digits


print(same_length(50, 70))
print(same_length(50, 100))
print(same_length(10000, 12345))
