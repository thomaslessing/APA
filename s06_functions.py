def myfunction():
    print('This is my function')

print(myfunction, type(myfunction), id(myfunction))
a = myfunction
print(a, type(a), id(a))

myfunction()
a()