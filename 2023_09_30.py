numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
is_prime = True
not_primes=[]
primes=[]
for i in numbers:
    if i != 1:
        for j in range(1,i+1):
            if j != i and j != 1:
                if i % j == 0:
                    is_prime = False
                    break
                else:
                    is_prime = True
        if is_prime == True:
                primes.append(i)
        elif is_prime == False:
                not_primes.append(i)
print("Primes:", primes)
print("Not Primes:", not_primes)