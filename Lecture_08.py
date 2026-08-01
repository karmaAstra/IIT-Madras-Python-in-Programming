# s = "coffee"
# t = "bread"

# print(s)
# print(t)
# print(s+t) # concatenation

# print(s[1:3]) # index 'of' starting from 1 to 3 but not including 3
# print(s[3:5]) # index 'fe' starting from 3 to 5 but not including 5

s = '0123456789'
a = s[4]
b = s[3]

print(a)
print(b)

print(a+b) # concatenation of a and b. Its not an Integer addition. Its a string concatenation. So the output will be 43 and not 7

a = int(s[4])
b = int(s[3])

print(a + b) # Now the output will be 7 because we have type casted the string to Integer