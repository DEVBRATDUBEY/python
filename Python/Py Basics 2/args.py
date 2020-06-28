# *args **kwargs = keywords argument
# here args and kwargs is just variable
# on one and two star matter
# Rule: params, *args,default parameters,**kwargs
# * example
def super_func(*args):
    print(*args)
    print(args)  # it is tuple
    return sum(args)


print(super_func(1, 2, 3, 4, 5))


# ** example
def super_func(*args, **kwargs):
    print(kwargs)  # it return a dictionary
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))
