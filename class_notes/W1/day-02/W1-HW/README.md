# Homework 1
## Due date: 9/20/2020 at 6:00 PM EST via pull request
## File name: ```solution.ipynb```

## EST TIME: 2hrs
You have a robot who communicates in a series of beeps and boops. You usually get the gist of what he means, but just once it would be nice to know what's really on his mind! 
You've noticed a pattern in the beeps and boops, and it seems like the number of beeps and boops correspond to specific letters.

**Example Code**

```python
beeps = 2
boops = 6
total = beeps + boops
print(total) # prints 8
```

---

## Problem: Decoding R2D2


You got a result of `8`. Now, look that up in the corresponding key-value chart:

|  Code | Letter | Code | Letter |
|  ------ | ------ | ------ | ------ |
|  1 | A | 14 | N |
|  2 | B | 15 | O |
|  3 | C | 16 | P |
|  4 | D | 17 | Q |
|  5 | E | 18 | R |
|  6 | F | 19 | S |
|  7 | G | 20 | T |
|  8 | H | 21 | U |
|  9 | I | 22 | V |
|  10 | J | 23 | W |
|  11 | K | 24 | X |
|  12 | L | 25 | Y |
|  13 | M | 26 | Z |


---

## Problem: Decoding R2D2

So, according to the chart, the first letter is `H`! It's your job to figure out the rest of the message! Here is the full list of inputs you've got written down.

```
2 beeps, 6 boops
0 beeps, 5 boops
9 beeps, 3 boops
4 beeps, 8 boops
10 beeps, 5 boops
BOP! (pretty sure this is a space!)
11 beeps, 12 boops
5 beeps, 5 boops
1 beep, 17 boops
5 beeps, 7 boops
4 beeps, 0 boops
```

---

## Problem: Decoding R2D2

In a separate file, print out the numerical total for each beep-boop combo as we did above. In a comment, write the letter that the number corresponds to.

**Example Code**

```python
# H
beeps = 2
boops = 6
total = beeps + boops
print(total)
```

---

## Problem: Decoding R2D2

**Expected Output**

```
8
5
12
12
15
23
10
18
12
4
```

---

## Read/Watch: EST TIME: 1hr 
N/A

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
