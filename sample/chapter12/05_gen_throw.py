def gen_func():
    # yield "http://projectsedu.com"
    try:
        yield "http://projectsedu.com"
    except Exception as e:
        pass
    yield 2
    yield 3
    return "bobby"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, "download error")