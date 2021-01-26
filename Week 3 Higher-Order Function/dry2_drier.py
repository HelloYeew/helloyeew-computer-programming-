# Make this code DRY

from math import pi, sqrt


def find_area(r,k):
    assert r > 0, 'A length must be positive'
    return r * r * k


def area_square(r):
    """Return the area of a square with side length R."""
    return find_area(r, 1)


def area_circle(r):
    """Return the area of a circle with radius R."""
    return find_area(r, pi)


def area_hexagon(r):
    """Return the area of a regular hexagon with side length R."""
    return find_area(r, 3 * sqrt(3) / 2)


print(area_square(8))
print(area_circle(8))
print(area_hexagon(8))
print(area_circle(-8))
