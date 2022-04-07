#python module to import

print("file two __name__ is set to : {}" .format(__name__))

def func3():
    print("Function 3 is executed")

def func4():
    print("function 4 is executed")

if __name__ == "__main__":
    print("file two executed when ran directly")
else:
    print("file two executed when imported")