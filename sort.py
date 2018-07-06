L=[36,5,12,9,21]
print sorted(L)

L=[36,5,12,9,21]
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted(L, reversed_cmp)

L2=['bob', 'about', 'Zoo', 'Credit']
def cmp_ignore_case(s1, s2):
    u1=s1.upper()
    u2=s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(L2, cmp_ignore_case)