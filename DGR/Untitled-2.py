try:
    print(x)
except NameError:
    print("Name  error occurred")
else:
    print("this will only run if on exception occurs")
finally:
    print("this will always rum")