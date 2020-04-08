"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print(f'{z} {x % y}')

# Use the 'format' string method to print the same thing
turtle_love = "My mom said {} as much as I like eating {} fish and {} clams."
print(turtle_love.format("I like turtles", 10, 2.24552))

# Finally, print the same thing using an f-string
print(f"My mom said {z} as much as I like eating {x} fish and {y} clams.")
