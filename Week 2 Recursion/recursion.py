def fac(n):
    if n == 0:
        return 1
    else:
        return fac(n - 1) * n


print(fac(12))
print()


def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)


countdown(5)
print("Happy recursion day")
print()


def gcd(a, b):
    if a < b:
        return gcd(a, b - a)
    elif b > a:
        return gcd(a - b, a)
    else:
        return a


print(gcd(68, 119))
print()


def gcd_recursive(a, b):
    while a != b:
        if a < b:
            b = b - a
        elif b < a:
            a = a - b
    return a


print(gcd_recursive(68, 119))
print()


def reverse(str):
    if str == "":
        return str
    else:
        return reverse(str[1:]) + str[0]


print(reverse("reenigne"))
print()


def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(n // 10)


print(sum_digits(314159265))
print()


def is_palindrome(s):
    if len(s) < 2:
        return True
    if s[0].lower() != s[-1].lower():
        return False
    return is_palindrome(s[1:-1])


print(is_palindrome("Refer"))
print(is_palindrome("Referrer"))
print()


# palindrome check by use reverse function too

def reverse2(str):
    if str == "":
        return str
    else:
        return reverse(str[1:]) + str[0]


def is_palindrome2(s):
    return reverse(s.lower()) == s.lower()


print(is_palindrome2("Refer"))
print(is_palindrome2("Referrer"))
