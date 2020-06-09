"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%),
# print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
# print("x is%3d, y is%5.2f, z is%18s" %(x, y, '"{}"'.format(z)))
print("x is %d, y is %0.2f, z is %s" % (x, y, '"{}"'.format(z)))
# print('%(language)s has %(number)03d quote types.' %
#   {'language': "Python", "number": 2})
# output will be
# Python has 002 quote types.

# Use the 'format' string method to print the same thing
print('x is {}, y is {}, z is {}'.format(
    x, "{:.2f}".format(y), '"{}"'.format(z)))

# Finally, print the same thing using an f-string
print(f'x is {x}, y is {"{:.2f}".format(y)}, z is {z}')
