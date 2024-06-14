def my_decorator(func):
    def test():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
        def test2():
            print("asdafa")
            func()
            print("safsafsa")
        test2()
    return test

@my_decorator
def say_hello():
    print("Hello!")

say_hello()