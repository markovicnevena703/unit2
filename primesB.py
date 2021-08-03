from prime import is_prime

def primes_below(n):
    l = []
    i = 2
    while (i < n):
        if (is_prime(i) == True):
            l.append(i)
        i+=1
    return l
