"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""



def primes(number_of_primes):
    list = []
    iterator = 0


    if number_of_primes <= 0:
        raise ValueError("Number of primes is not to be set to 0.")

    if number_of_primes>=1:
        for i in range (1, 1000000000000000000):
            for j in range(1, i+1):
                if(i%j == 0):
                    iterator += 1
            if(iterator == 2):
                list.append(i)
            iterator = 0
            if len(list)==number_of_primes:
                break
    return list
