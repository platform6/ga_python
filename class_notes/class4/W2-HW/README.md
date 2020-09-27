# Homework 2
## Due date: 9/27/2020 at 6:00 PM EST via pull request
## File name: ```solution.py```

## EST TIME: 2hrs

## Problem 1: IOU!

### Skill you're practicing: Writing `for` loops to iterate over a list.

You have a list of Disney characters and you want to find out if each of them contain `i`, `o`, or `u` in their names. Loop through each character in the list and print out the following:

```
If the name contains a "u," print out the name plus "U are so Uniquely U!"
Otherwise if the name contains an "i," print out the name plus "I bet you're Impressively Intelligent!"
Otherwise if the name contains an "o," print out the name plus "O My! How Original!"
Otherwise, print the name plus "Ehh, a's and e's are so ordinary."
```

#### Starter Code

```python
disney_characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula", "scar", "flotsam", "timon"]
```

#### Expected Output

```
simba I bet you're Impressively Intelligent!
ariel I bet you're Impressively Intelligent!
pumba U are so Uniquely U!
flounder U are so Uniquely U!
nala Ehh, a's and e's are so ordinary.
ursula U are so Uniquely U!
scar Ehh, a's and e's are so ordinary.
flotsam O My! How Original!
timon I bet you're Impressively Intelligent!
```


> **Hint**: You can determine whether or not a string contains a particular character with an `if` statement. For example, `if "b" in my_string:` will be true if `my_string` contains any b's.

---

## Problem 2: If You're Cold, Sit in a Corner. It's 90 Degrees!

### Skill you're practicing: Writing `while` loops.

Wow! It's 90 degrees Fahrenheit and you are sweating buckets! Luckily you have air conditioning, but it's really old and kind of finicky. It cools the room by three degrees and shuts off, so you have to keep turning it back on until the temperature gets to where you want it to be. Seventy five sounds much more pleasant than 90, so that's what you're shooting for.

```
While the temperature is greater than 75 degrees Fahrenheit, print "The temperature is XX — crank the AC!" and subtract 3 degrees from the temperature.

Once the temperature is cool enough and the loop is done, print "75. Ahh, that's better."
```

#### Starter Code

```python
temperature = 90
```

#### Expected Output

```
Temperature is 90 — crank the AC!
Temperature is 87 — crank the AC!
Temperature is 84 — crank the AC!
Temperature is 81 — crank the AC!
Temperature is 78 — crank the AC!
75. Ahh, that's better.
```

> **Hint:** Make sure that your loop conditional is being updated each iteration. Otherwise you'll end up with an infinite loop!

---
## Read/Watch: EST TIME: 1hr 
[Python Dictionary](http://python-ds.com/python-dictionary)

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
