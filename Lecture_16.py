# Keywords -> These are the mains words in Python and can not be used as variable names

# Rules for defining variables:
# A - Z and a - z and all numbers between 0 - 9 are allowed in variable names
# Special characters are not allowed except for the underscore (_)
# Should not start with a number

# Multiple Assignment

x,y = 3,4
print(x) # 3
print(y) # 4

x,y = y,x
print(x) # 4
print(y) # 3

x = y = z = 10
print(x,y,z) # All are 10