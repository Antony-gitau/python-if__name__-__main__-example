#python file one module 

from file2 import func3
print("file one __name__ is set to : {}". format(__name__))

def func1():
    print("function one is executed")

def func2():
    print("function two is executed")


if __name__ == "__main__":
    print("file one executed when ran directly")
    func2()
    func3()
else:
    print('file one executed when imported')