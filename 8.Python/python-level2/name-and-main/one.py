def func():
    print("fun() in one.py")

print("top level one.py")

if __name__ == '__main__':
    print("one.py is being run directly")

else:
    print("one.py has been imported")