def big_fibonacci(n):
    fib = [1,1]
    i = 0
    
    while True:
        if (n == len(str(fib[i]))): 
            return fib[i]
        j = i + 1
        fib.append(fib[i] + fib[j])
        i+=1
        