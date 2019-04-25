print("0. The student number is: 17033081")

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


z = [1, 7, 0, 3, 3, 0, 8, 1]
print ("1. The number of prime numbers in this student number is:" + str(count_primes_in_list(z)))



from random import randint
print("2. The random number is" + str(randint(25,50)))

"The number of strings to be generated is: 7"

"4. List of strings"
import random
import string
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
print ("0 - ", randomString(5) )
print ("1 - ", randomString(7) )
print ("2 - ", randomString(5) )
print ("3 -", randomString(7) )
print ("4 -", randomString(5) )
print ("5 -", randomString(7) )
print ("6 -", randomString(5) )

"5. Sorted List"
def find_vowels_1(data, vowels='aeiou'):
    # return the number of occurrences of each vowel in a string
    return [(v, data.count(v)) for v in vowels ]

print("0 - chfkg " + str(find_vowels_1('chfkg')))
print("1 - knvswem" + str(find_vowels_1('knvswem')))
print("2 - uheoz" + str(find_vowels_1('uheoz')))
print("3 - dyntlfe" + str(find_vowels_1('dyntlfe')))
print("4 - vlzuj " + str(find_vowels_1('vlzuj')))
print("5 - joxwbsj" + str(find_vowels_1('joxwbsj')))
print("6 - eowrk" + str(find_vowels_1('eowrk')))





