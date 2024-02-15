def say_hi(fn):

    print("This is just a setup code")

    def response():
        print("Do this before")
        fn()
        print("Do this later")

    return response


@say_hi
def say_hello():
    print("Hello")


say_hello()
say_hello()