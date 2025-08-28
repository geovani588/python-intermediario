# Introduçao as Generator functions em Python
# generator = (n for n in range(10000000))
# generator funcoes que sabem pausar

# def generator(n=0):
#     #return 1
#     yield 1 # pausar
#     return 'ACABOU'

# gen = generator(n=0)
# print(next(gen))


def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=100)
for n in gen:
    print(n)