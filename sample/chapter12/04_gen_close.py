def gen_func():
    # GeneratorExit继承自BaseException
    # try:
    #     yield "http://projectsedu.com"
    # except GeneratorExit:
    #     raise StopIteration
    yield "http://projectsedu.com"
    yield 2
    yield 3
    return "bobby"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.close()
    print(next(gen))