


def is_num_prime(number, *divisors):
    divisors = [i for i in [i for i in range(1, number)] if number%i==0]
    if len(divisors) > 1: return divisors
    else: return 'This is prime number'

entry = (is_num_prime(int(input('What number foo? ---- '))))
print(entry)