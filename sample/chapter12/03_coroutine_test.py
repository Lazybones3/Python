#1.生成器可以产出值，也可以接收值（调用方传进来的值）
def gen_func():
    html = yield "http://projectsedu.com"
    print(html)
    yield 2
    yield 3
    return "bobby"

if __name__ == "__main__":
    gen = gen_func()
    #启动生成器的方式有两种：next(),send()
    url = next(gen)
    # 在调用send发送非None值之前，我们必须启动一次生成器，两种方式1.gen.send(None) 2.next(gen)
    # url = gen.send(None)
    # download url
    html = "bobby"
    #send方法可以传递值到生成器内部，同时还可以重启生成器执行到下一个yield位置
    gen.send(html)
    # print(gen.send(html))