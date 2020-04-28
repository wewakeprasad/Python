def product (a):
    prod = 1
    result = []
    for x in a :
        prod *= x
    for x in a :
        result.append(prod / x) 

    return result
