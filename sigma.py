

def sigma(x, sum=0):
    if x < 1:
        return(sum)
    sum = sigma(x-1, sum + x)
    return(sum)

# print (sigma(3))
# print(sigma(2))

# print(sigma(5))
# print(sigma(6))
print(sigma(500))