from prime import is_prime

def is_palindrome(n):
    i = 0
    s = str(n)
    while (i <= (len(str(n))//2)):
        if (s[i] != s[len(s) - i - 1]):
            return False
        i+=1
    return True



l = []
j = 10000
while (j < 100000):
    if (is_palindrome(j) and is_prime(j)):
        l.append(j)
    j+=1

print(l)
