# [Python](../../courses.md)


- [Python](#python)
  - [ZTM: Python Developer](#ztm-python-developer)
    - [Introduction](#introduction)
    - [Basics](#basics)
    - [Developer Environment](#developer-environment)
    - [Object Oriented Programming](#object-oriented-programming)
    - [Functional Programming](#functional-programming)
    - [Decorators](#decorators)
    - [Error Handling](#error-handling)
    - [Generators](#generators)
    - [Modules](#modules)
    - [Debugging, File IO](#debugging-file-io)
    - [Regular Expressions](#regular-expressions)
    - [Testing](#testing)
    - [Python Developer](#python-developer)
    - [Scripting](#scripting)
    - [Scraping](#scraping)
    - [Web Development](#web-development)
    - [Automation Testing](#automation-testing)
    - [Machine Learning and Data Science](#machine-learning-and-data-science)
    - [Conclusion](#conclusion)
  - [LinkedIn: Python Essential Training](#linkedin-python-essential-training)
  - [LinkedIn: Python Object-Oriented Programming](#linkedin-python-object-oriented-programming)
  - [LinkedIn: Level Up: Python](#linkedin-level-up-python)
  - [Coursera: Python Programming Fundamentals](#coursera-python-programming-fundamentals)
    - [Introduction](#introduction-1)
    - [Basics](#basics-1)
    - [Functions and Modules](#functions-and-modules)
    - [Data Structures](#data-structures)
    - [Error Handling and Debugging](#error-handling-and-debugging)
    - [Testing basics and version control](#testing-basics-and-version-control)
  - [Coursera: Data Analysis and Visualization with Python](#coursera-data-analysis-and-visualization-with-python)
  - [Coursera: Automation and Scripting with Python](#coursera-automation-and-scripting-with-python)
  - [Coursera: Web Development with Python](#coursera-web-development-with-python)
  - [Coursera: Advanced Python Development Techniques](#coursera-advanced-python-development-techniques)
  - [Coursera: Project Development in Python](#coursera-project-development-in-python)
  - [Udemy, Krish: Complete Python With DSA](#udemy-krish-complete-python-with-dsa)
    - [Basics](#basics-2)
  - [Educative: PDF Management in Python](#educative-pdf-management-in-python)
    - [Introduction](#introduction-2)
  - [CodeAcademy: Python](#codeacademy-python)
    - [Introduction](#introduction-3)


## ZTM: Python Developer

### Introduction


### Basics


### Developer Environment


### Object Oriented Programming


### Functional Programming


### Decorators


### Error Handling


### Generators


### Modules


### Debugging, File IO


### Regular Expressions


### Testing


### Python Developer


### Scripting


### Scraping


### Web Development


### Automation Testing


### Machine Learning and Data Science


### Conclusion


## LinkedIn: Python Essential Training

## LinkedIn: Python Object-Oriented Programming

## LinkedIn: Level Up: Python

```py
# Find Prime Factors

def get_prime_factors(number):
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1
    return factors
```


```py
# Identify a Palindrome 

import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards
```

```py
# Sort a string of words

def sort_words(input):
    words = input.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return ' '.join(words)

def sort_words(words):
    return ' '.join(sorted(words.split(), key=str.casefold)) # str.casefold ensures case insensitive sort
```

```py
# Find all list items 

def index_all(search_list, item):
    index_list = []
    for index, value in enumerate(search_list):
        if value == item:
            index_list.append([index])
        elif isinstance(search_list[index], list):
            for i in index_all(search_list[index], item):
                index_list.append([index] + i)
    return index_list
```

```py
# Play the waiting game

import time 
import random

def waiting_game():
    target = random.randint(2, 4) # target seconds to wait
    print(f'\n Your target time is {target} secodns')

    input(' --- Press Enter to Begin ---')
    start = time.perf_counter()

    input(f'\n... Press Enter again after {target} seconds ...')
    elapsed = time.perf_counter() - start

    print(f'\n Elapsed time: {elapsed: .3f} seconds')
    
    if elapsed == target:
        print('(Unbelievable! Perfect timing!)')
    elif elapsed < target:
        print(f'({target - elapsed : .3f} seconds too fast)')
    else:
        print(f'({elapsed - target: .3f} seconds too slow)')
```

```py
# Save a dictionary

# pickling --> process that serializes the python object converting it into a bite stream that can be saved into a file

import pickle

def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)
    
def load_dict(file_path):
    with open(file_path, 'rb') as file:
        retunr pickle.load(file)  

test_dict = {5: 'a', 3: 's', 9: 'h'}
save_dict(test_dict, 'ash.pickle')
recovered = load_dict('ash.pickle')
```


```py
# schedule a function 

import sched # general purpose event scheduler
import time 

def schedule_function(event_time, function, *args):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(event_time, 1, function, argument=args)
    print(f'{function.__name__} () scheduled for {time.asctime(time.localtime(event_time))}')
    s.run()

schedule_function(time.time() + 1, print, 'Howdy!', 'How are you?')
```


```py
# Send an email 

import smtplib

SENDER_EMAIL = 'vdanepalli@gmail.com'
SENDED_PASSWORD = 'dkasjjkfascjnscj'

def send_email(receiver_email, subject, body):
    message = f'Subject: {subject} \n\n {body}'
    with smtplib.SMTP('smtp.office365.com', 587) as server: # context manager; automatically closes  
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)
```


```py
# Simulate Dice

from random import randint
from collections import Counter

def roll_dice(*dice, num_trials=1_000_000):
    counts = Counter()
    for _ in range(num_trials):
        counts[sum((randint(1, sides) for sides in dice))] += 1
    
    print('\n Outcome \t Probability')

    for outcome in range(len(dice), sum(dice)+1):
        print(f'{outcome} \t {counts[outcome] * 100 / num_trials: 0.2f}%')

roll_dice(4, 6, 6 ) # percentages for 4 to 16
```

```py
# count unique words

import re 
import collections

def count_words(path):
    with open(path, 'r', encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print(f'\n Total Words: {len(all_words)}')

        word_counts = collections.Counter(all_words)

        print('\n Top 20 Words:')

        for word in word_counts.most_common(20):
            print(f'{word[0]}\t{word[1]}')
```


## Coursera: Python Programming Fundamentals

### Introduction

- Flowcharts
- Instructions - Recipe - Algorithm
- Variables
- Data Types
  - Numbers
  - Strings
  - Booleans
  - Lists
  - Dictionaries
- Operators
- Data Structures - organize collections of data
- Control flow statements
- Loops
- Functions - reusable blocks
- Statements - single line of code, specific action, single step

<br/><br/>

- Syntax(rules)
- Semantics(meaning)
- Data
- Python
  - readability, simple
  - easy maintenance
  - characteristics
    - interpreted
    - high-level
    - object-oriented (contain both data and functions)
  - general purpose - versatile
  - Django -- batteries included, rapid development, clean design -- Instagram, Disqus, Spotify
  - Flask -- Minimalist, Micro-Framework
  - Data Science -- collect, clean, analyze, visualize
    - Numpy -- numerical computing, arrays and matrices
    - Pandas -- manipulate, transform
    - Matplotlib -- charts, graphs, plots
    - Scikit-learn, Microsoft Cognitive Toolkit
  - Automation - backup, emails
  - Web Scraping -- BeautifulSoup, Scrapy
  - GameDev - PyGame
  - SciPy
  - Frameworks, Libraries, Large Community, Cross Platform Compatibility
- Indentation


<br/><br/>

- Anaconda -- distribution -- comes with packages and streamlines package management
  - Comprehensive pacakge management
  - Conda environment management -- isolated environments
  - Cross-platform compatibility
- Python interpreter -- can be slower than compiled
- Standard Library 
- PIP Package Installer for Python
- PyPI Python Pacakage Index

```bash
sudo apt-get update
sudo apt-get install ...
chmod +x filename.sh # set executable permissions
./filename.sh
```

- Jupyter Notebook -- IDE, Interactive Cells, Markdown Support, Rich Output; experiment, visualize, document
  - web-based application
  - `pip install notebook`
  - `jupyter notebook`
  - magic commands `% or %%` `%timeit`
- Anaconda -- IDE, package/conda env management, Jupyter Notebook integration
- VS Code -- code completion, debugging, git, extensions
- PyCharm


<br/><br/>

- Reading -- lexical analysis -- tokens
- Interpreting -- parsing 
- Executing -- bytecode compilation and evaluation -- bytecode is executed by Python Virtual Machine PVM
- Importing Modules
- Running python scripts with command line arguments
- Working with virtual environments

```py
import csv

with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

if ... 
elif ...
else ...

for i in range(1, 11):
    ...

while not valid_input:
    user_input = int(input(prompt_msg))

for item in lists:
    ...

import random
roll = 0
while roll!=6:
    roll = random.randint(1, 6)

```

- for loops - known iterations
- while loops - conditions
- indentation errors
- variable scope
- immutable values
- name shadowing
- circular imports
- memory management


<br/><br/>

- list -- 0 indexed, ordered, mutable, flexible
- `[]` `len(list)` 
- `list[len(list) -1]` last element
- slicing `list[start : end]
- list comprehension - for-each loop
- IndexError, ValueError
- operations
- len(list)
  - list.append(x)
  - list.insert(i, x)
  - list.remove(x)
  - list.sort() -- can only sort elements of same type
  - list.reverse()
  - list.count(x)
  - x in list
  - list.index(x)



### Basics

### Functions and Modules

### Data Structures

### Error Handling and Debugging 

### Testing basics and version control

## Coursera: Data Analysis and Visualization with Python

## Coursera: Automation and Scripting with Python

## Coursera: Web Development with Python

## Coursera: Advanced Python Development Techniques

## Coursera: Project Development in Python

## Udemy, Krish: Complete Python With DSA

### Basics

Case Sensitive, Indented, Line continuation for statement (`\`), Multiple statements in single line (separated by `;`)

```python
type(some_var)

# Numbers
big_number = 1_000_000_000_000 # int
temperature = -5.5 # float
light_speed = 3e8 # 3 * 10^8 - float
z1 = 1 + 2j # complex; can use J as well

# Sequence
string = 'Ash' # str; immutable, ordered;; ""
mylist = [3, 9] # list; mutable, ordered; []
mytuple = (3, 9) # tuple; immutable, ordered; (), (39, )
myrange = range(start, end, step) # ordered immutable

# Set
# Hashable -- do not change in its lifetime
myset = set(); {3, 9} # set: unordered, mutable, hashable items
myfronzenset = frozenset({3, 9}) # frozenset; unordered immutable, hashable items

# Map
# Keys must be hashable and unique
mydict = {}; {"name":39} # unordered/insertion-ordered mutable

boolean = True # bool immutable

myash = None # immutable

# Binary sequence
mybytes = b'ash'; b'\x01\x02' # immutable ordered sequence of bytes (0-255)
mybytearray = bytearray(b'ash') # mutable ordered

mymemoryview = memoryview(b'ash')
```

Operations

```py
+ # add, concat, merge?
    # in a + b, python tries a.__add__(b); if not implemented, tries b.__radd__(a)
    # a += b, python tries a.__iadd__(b)
    # can only add objects of compatible types
-
* # mul, repeat
/ # div, returns float
// # floor div; N/D both int then int, else float
% # modulo
** # exponentiation

==
!=
>
<
>=
<=

=
+=
-=
*=
/=
//=
%=
**=

# instances of user-defined classes are truthy unless __bool__(), __len__() returns false or 0
# Short-circuiting
and
or
not


is
is not

in
not in

&
|
^ # same 0, opp 1
~ 
<< # * 2^
>> # / 2^

"happy" if "ash" else "very happy?" # ternary operator
while (line := file.readline()): print(line) # walrus operator (:=) ; assigns value to variable as part of a larger expression

```

Operator overloading using `__dunder__` methods

`Divident = divisor * quotient + remainder`
- truncated division -- rounds quotient towards zero (c, java)
- floor division -- rounds quotient towards negative infinity (python)
- examples
  - `10 % 3` => `10 // 3` is `3` => `10 = 3 * 3 + remainder` => remainder = `1`
  - `-10 % 3` => `-10 // 3` is `-4` => `3 * -4 + remainder` => remainder = `2`
    - `0 <= result < divisor`
  - `10 % -3` => `10 // -3` is `-4` => `-3 * -4 + remainder` => remainder = `-2`
  - `-10 % -3` => `-10 // -3` is `3` => `3 * -3 + remainder` => remainder = `-1`
- rules
  - result sign matches divisor (denominator) sign
  - negative dividend, positive divisor => add positive divisor to dividend until result is non-negative; first non-negative result less than divisor is answer. 
- terminology
  - dividend = numerator = what's being shared
  - divisor = denominator = parts you are splitting into
  - quotient = number of times divisor fits into dividend
  - remainder = left overs
```py
result = (a % b + b) % b # makes sure result is between [0, |b|) even when b is -ve
index % len(sequence) # always gives a valid positive index, even when index is negative


items = ['A', 'B', 'C', 'D']
index = 6
print(items[index % len(items)]) # Output: C (6 % 4 = 2, items[2])

index = -1
print(items[index % len(items)]) # Output: D (-1 % 4 = 3, items[3])


# What hour is it 5 hours after 10 on a 12-hour clock (result 1-12)?
# Need to adjust for 0 result and make it 12
hour = 10
hours_to_add = 5
new_hour = (hour + hours_to_add) % 12
# If the result is 0, it means 12 o'clock
print(new_hour if new_hour != 0 else 12) # Output: 3

# A simpler way for 1-based cycles: (n-1 % cycle_length) + 1
hour = 10
hours_to_add = 5
new_hour_0based = (hour - 1 + hours_to_add) % 12 # 9 + 5 = 14. 14 % 12 = 2
new_hour_1based = new_hour_0based + 1            # 2 + 1 = 3
print(new_hour_1based) # Output: 3

# Day of the week (0=Mon, 6=Sun)
today = 2 # Wednesday
days_forward = 10
future_day = (today + days_forward) % 7
print(future_day) # Output: 5 (Friday)

n % 10 # last digit
n % 100 # last 2 digits
```

## Educative: PDF Management in Python

### Introduction

- High level, object-oriented, interpreted; many libraries
- PDF Portable Document Format -- structured binary file format
- ISO International Organization for Standardization
- vulnerabilities
  - Denial of Service 
  - Deflate Bomb
  - Execute Code
  - Memory Corruption


## CodeAcademy: Python

### Introduction

- Errors, Bugs, Debugging
- 