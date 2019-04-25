def count_primes_in_list(numbers):
    primes = []
    for num in numbers:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:                
                print ("Not a Prime: "+str(num))
                is_prime = False
                break

        if is_prime and num!=0 and num!=1:
            primes.append(num)

        print(primes)
    return len(primes)


z = [23, 7, 0, 3, 3, 0, 8, 1]
print (count_primes_in_list(z))