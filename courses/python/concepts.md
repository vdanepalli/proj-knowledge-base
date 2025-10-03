# [General Concepts](../../courses.md)


- [General Concepts](#general-concepts)
  - [Python Decorators](#python-decorators)


## Python Decorators

```python
import functools


def do_twice(func): # takes a function as argument and wraps it with something else; this is the decorator
    
    # this line helps, to not change the function being decorated when you call help(func) or func.__name__ 
    # which otherwise would refer to this wrapper function
    @functools.wraps(func) 
    def wrapper_do_twice(*args, **kwargs): # captures the arguments passed to the function that is being decorated
        print("I am doing something")
        func(*args, **kwargs)
        return  func(*args, **kwargs) # let's say you had a return statement in the function being decorated; this helps with that.
    
    return wrapper_do_twice # this is needed to access this wrapper outside do_twice
```


```python
# ideally this is how you decorate a function

def greet():
    print("Hey fella")

greet = do_twice(greet)

greet() # prints hey fella


# this is a sugary syntax... 

@do_twice
def greet(name):
    print(f"Hey {name}")
    return name

greet # this shows greet as a regular function
# if you had not said @functools.wraps(func), this would show as 
# <function do_twice.<locals>.wrapper_do_twice at 0x.....>

return_name = greet("ASH")
```

- [Realpython primer on python decorators](https://realpython.com/primer-on-python-decorators/)