# W6-HW
## Due date: 10/25 at 6:00PM Eastern via pull request
## File name: ```solution.py```
## EST TIME: 2hrs

The goal is to create a class that represents a simple circle. 

By default, a `Circle` will be defined by specifying the radius as an argument like this:
```python
c1 = Circle(4)
# c1 is a Circle with radius of 4
```

The class will also include a class method to return a new circle by diameter like this:
```python
c2 = Circle.from_diameter(12)
# c2 is a circle with radius of 6
```

You should also be able to:
* Retrieve the circle’s area.
* Print the circle as a custom string; see object representation in a list of circles.
* Add two circles together to return a new circle with a radius equal to the sum of the radii.
* Multiply a circle by an integer to return a circle with a radius of `number` times the current radius
* Compare two circles to see which is bigger.
* Compare to see if two circles have equal radii.
* Sort circle objects by radius.

You will also use:
* Properties.
* A class method.
* Special methods (dunders).

Starter code:
```python
from math import pi
class Circle:
    pass

# test code
# define the first circle and display its attributes
c1 = Circle(4)
print(c1.radius, c1.diameter)
print('^^^ Expected output: 4 8 \n')
print(c1.area)
print('^^^ Expected output: 50.26548245743669 \n')

# change the diameter -- the radius and area should change correspondingly
c1.diameter = 2
print(c1.radius, c1.area)
print('^^^ Expected output: 1.0 3.141592653589793 \n')

# define a circle using the from_diameter method
c2 = Circle.from_diameter(10)
print(c2.radius, c2.area)
print('^^^ Expected output: 5.0 78.53981633974483 \n')

# create two more circles; put all the circle objects inside a list named circles
c3 = Circle(6)
c4 = Circle(1.1)
circles = [c1, c2, c3, c4]
print(circles)
print('^^^ Expected output: [Circle(1.0), Circle(5.0), Circle(6), Circle(1.1)] \n')

# sort the list of circles
print(sorted(circles))
print('^^^ Expected output: [Circle(1.0), Circle(1.1), Circle(5.0), Circle(6)] \n')

# add two circles
c5 = c3 + c4
print(c5)
print('^^^ Expected output: Circle with Radius: 7.1 \n')

# multiply a circle by a number
c6 = c3 * 5
print(c6)
print('^^^ Expected output: Circle with Radius: 30.0 \n')

# see if two circles with equal radii evaluate as equal
c4.radius = 1
print(c4 == c1)
print('^^^ Expected output: True \n')
```

## Read: NA

## How to submit homework
### Setup
- Step 1. Fork the repository
- Step 2. Clone your fork
### Submitting work
- Step 1. Commit changes in Git
- Step 2. Push to your fork
- Step 3. Submit a pull request
- Step 3.1. Add a title and comment

In the comment section, you must add the following:
```text
* Comfort level [0 to 5]
* Completeness [0 to 5]
* What was a win?
* What was a challenge?
* Any other comments:
```
