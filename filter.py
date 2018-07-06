def is_odd(n):
    return n%2 == 1
print filter(is_odd, range(1,16))

def not_empty(s):
    return s and s.strip()
print filter(not_empty, ['A', '', 'B', None, 'C', '     '])

#practice
def is_prime(n):
    if n<=2:
        return False
    if n%2 == 0:
        return False
    for i in range(3, n, 2):
        if n%i == 0:
            return False
    return True
print filter(is_prime, range(1, 101))