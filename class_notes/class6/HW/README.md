# Homework 3
## Due date: 10/04/2020 at 6:00 PM EST via pull request
## File name: ```solutions.py```

## EST TIME: 2hrs
- Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.  For example, if  s = 'azcbobobegghakl', your program should print:  Number of vowels: 5

- Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print Number of times bob occurs is: 2 

- Ask the user to input a string and then reversal the given input.  Input:  "Programming in Python" Output: nohtyP ni gnimmargorP 

- Write a program that accepts a sentence and calculate the number of uppercase letters and lowercase letters. Suppose the following input is supplied to the program. Input: Hello World  Output: UPPERCASE: 2, LOWERCASE: 9. You may count space as lowercase.

- Write a program that accepts a comma-separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically. Suppose the following input is supplied to the program: without, hello, bag, world Then, the output should be: bag, hello, without, world

- Ask the user to enter a string, and check if it is a palindrome. If yes, print True, or else print False.

## Starter code


```python
class Vowels:
	def __init__(self, str_input):
		pass

	def check_vowels(self):
		pass


class StringCount:
	def __init__(self, str_input):
		pass

	def find_bob(self):
		pass


class StringReversal:
	def __init__(self, str_input):
		pass

	def reversed_string(self):
		pass


class UpperLower:
	def __init__(self, str_input):
		pass

	def count_upper_lower(self):
		pass


class SortWords:
	def __init__(self, str_input):
		pass

	def split_alpha(self):
		pass


class PalindromeChecker:
	def __init__(self, str_input):
		pass

	def check_palindrome(self):
		pass


question1 = Vowels("Hello World")
question1.check_vowels()
print("==============\n")

question2 = StringCount("HelloWorldbobsureshbosigerabob")
question2.find_bob()
print("==============\n")

question3 = StringReversal("Programming in Python")
question3.reversed_string()
print("==============\n")

question4 = UpperLower("Hello World")
question4.count_upper_lower()
print("==============\n")

question5 = SortWords("without,hello,bag,world")
question5.split_alpha()
print("==============\n")

question6a = PalindromeChecker("Suresh")
question6a.check_palindrome()

print("==============\n")
question6b = PalindromeChecker("pullup")
question6b.check_palindrome()

```



## Read/Watch: EST TIME: 1hr N/A
[What is inheritance?](https://www.educative.io/edpresso/what-is-class-inheritance-in-python)

## How to submit homework
### Setup
- Step 1. Fork the repository
- Step 2. Clone your fork
### Submitting work
- Step 1. Create a folder for the specific homework
- Step 2. Push to your fork
- Step 3. Submit a pull request
- Step 3.1. Add a title (First name, Last Name) and comment

In the comment section, you must add the following:
```text
* Comfortability [0 to 5]
* Completeness [0 to 5]
* What was a win?
* What was a challenge?
* Any other comments
```
