def prime_num_generator():
    num = 2
    while True:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            yield num
        num += 1

prime = prime_num_generator()
print([next(prime) for i in range(10)])
