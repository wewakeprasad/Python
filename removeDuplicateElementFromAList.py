L = [5,3,7,9,5,1,4,7]
newL = []
[ newL.append(v) for v in L if newL.count(v) == 0 ]
print(newL)

