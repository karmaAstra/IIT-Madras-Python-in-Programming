s = "Good"
print(s*5)
print(s == "Good")  #True
print(s == "good")  #False 
print("apple" < "banana") #True --> Comparison is done based on the ASCII values of the characters.
#                               --> Comparison is based on the first character of the string. 
#                               --> If they are equal, then comparison is done 
#                               --> based on the second character and so on.
print("apple" < "Apple") #False --> ASCII value of 'a' is greater than ASCII value of 'A'
# ASCII value of 'a' is 97 and ASCII value of 'A' is 65.
# So the value of 'A' is less than the value of 'a'. Hence, "apple" < "Apple" is False.
print("abcde" > "abcdg") #False --> Comparison is done based on the first character of the string.


# Negative indexing in strings:
s = "Good"
print(s[-1]) #d
print(s[-2]) #o