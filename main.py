
def sgn(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def give_factors(num):
    factors = []

    i = 2
    while num != 1:
        if num % i == 0:
            num /= i
            factors.append(i)
        else:
            i += 1

    return factors


def factorize(numerator, denominator):
    n_sgn, d_sgn = sgn(numerator), sgn(denominator)
    n_factors = give_factors(numerator*n_sgn)
    d_factors = give_factors(denominator*d_sgn)

    n, d = 1, 1
    for factor in n_factors:
        if factor not in d_factors:
            n *= factor
        else:
            d_factors.remove(factor)

    for _d in d_factors:
        d *= _d

    if n != d:
        return f'{n * n_sgn * d_sgn}/{d}'
    else:
        return str(n_sgn*d_sgn)

def main():
    a = int(input("give a: "))
    b = int(input("give b: "))
    c = int(input("give c: "))

    discriminant = b*b - 4*a*c
    real = True if discriminant >= 0 else False
    d = -discriminant if discriminant < 0 else discriminant

    if d:
        m1, m2 = 1, 1

        factors = give_factors(d)

        while factors:
            factor = factors[0]
            factors.remove(factor)
            if factor in factors:
                m1 *= factor
                factors.remove(factor)

            else:
                m2 *= factor
    else:
        
        m1, m2 = 0, 0

    iota = 'i' if not real else ''

    root_1, root_2 = '', ''

    if d:
        if m2 == 1 and real:
            root_1 = factorize((-b + m1), 2*a)
            root_2 = factorize((-b - m1), 2*a)
            rational = True

        else:
            root_1 = f'{factorize(-b, 2*a)} + {iota}√{m2}({factorize(m1, 2*a)})'
            root_2 = f'{factorize(-b, 2*a)} - {iota}√{m2}({factorize(m1, 2*a)})'
            rational = False

    else:
        if m2 in [0, 1] and real:
            root_1 = factorize((-b + m1), 2*a)
            rational = True

        else:
            root_1 = f'{factorize(-b, 2*a)} + {iota})'
            rational = False

    print(f"\n\nDiscriminant: {discriminant}\n")
    print("Nature:")
    print(f'\t{'Not '*int(not real)}real')
    print(f'\t{'ir'*int(not rational)}rational')
    print(f'\t{'Not '*sgn(d)}equal\n')

    if root_2:
        print(f"Roots : {root_1}, {root_2}")
    else:
        print(f"Root : {root_1}")

while True:
    main()
    cont = int(input("continue? \n(yes : 1, no : 0): "))
    if not cont:
        break

