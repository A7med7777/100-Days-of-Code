# Debugging Code Examples

This repository contains several examples of common bugs in Python code, along with their corrected versions. Each example demonstrates a typical problem and how to fix it.

### Problem 1: Loop Range Error

#### Original Code
```python
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()
```

#### Issue
The range `range(1, 20)` generates numbers from 1 to 19, so the condition `if i == 20` is never met.

#### Fixed Code
```python
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")
my_function()
```

### Problem 2: Index Error with Random Choice

#### Original Code
```python
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
```

#### Issue
The `randint(1, 6)` generates numbers from 1 to 6, but list indices in Python are zero-based. Accessing `dice_imgs[6]` will cause an `IndexError`.

#### Fixed Code
```python
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
```

### Problem 3: Logical Error in Conditions

#### Original Code
```python
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
```

#### Issue
The condition for checking if someone is a Gen Z should include the year 1994.

#### Fixed Code
```python
year = int(input("What's your year of birth?"))
if 1980 < year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")
```

### Problem 4: Type Error in Input Handling

#### Original Code
```python
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")
```

#### Issue
The `input` function returns a string, which needs to be converted to an integer for numerical comparison. Additionally, the print statement is not properly indented and does not use an f-string.

#### Fixed Code
```python
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
```

### Problem 5: Assignment vs Comparison

#### Original Code
```python
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
```

#### Issue
The comparison operator `==` should be an assignment operator `=`.

#### Fixed Code
```python
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
```

### Problem 6: Scope Error in Loop

#### Original Code
```python
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
```

#### Issue
The `b_list.append(new_item)` line is outside the loop, so only the last item is appended.

#### Fixed Code
```python
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
```

## How to Run
1. Copy each code snippet into a Python script or interactive shell.
2. Observe the output and compare it to the expected results.
3. Modify the code as shown in the "Fixed Code" sections to correct the errors.

Feel free to modify the examples to experiment with similar issues and solutions.