def uppercase_decorator(function):
    def wrap():
        text = function()
        return text.upper()

    return wrap

@uppercase_decorator
def hello_world():
    return 'hello world'


print(hello_world())