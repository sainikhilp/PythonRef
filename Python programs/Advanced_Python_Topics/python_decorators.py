# decorators allows you to add new functionality to the existing function

 
def new_decorator(original_func):

    def wrap_function():

        print("Some lineso of code before original function")
        original_func()
        print("Some lines of code after original func")

        
    return wrap_function

def original_func():
    print("hi i am original function")


wrap_function=new_decorator(original_func)
wrap_function()



