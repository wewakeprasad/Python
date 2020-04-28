def isPrime(n):
    if n==1:
        return False
    for t in range(2,n):
        if n % t ==0:
            return False
    return True
