numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#          0  1  2  3  4  5  6  7  8  9   10  11  12  13  14
#Primes: [2, 3, 5, 7, 11, 13]            Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)-1):
    is_prime = False
    for g in range(2, i+1):
        #print(i,g)
        if numbers[i+1] % g == 0:
            is_prime = True
    if is_prime == True:
        not_primes.append(numbers[i+1])
        is_prime = False
    else:
        primes.append(numbers[i+1])

print(f'primes {primes}')
print(f'not_primes {not_primes}')

