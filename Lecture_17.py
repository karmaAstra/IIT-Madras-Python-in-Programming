# Original String
s = "this is The String"



print("Original String :", s)

print("-" * 50)

# Case Conversion Methods
print("Lowercase       :", s.lower())        # Converts all characters to lowercase
print("Uppercase       :", s.upper())        # Converts all characters to uppercase
print("Capitalize      :", s.capitalize())   # Capitalizes only the first character
print("Title Case      :", s.title())        # Capitalizes the first letter of each word
print("Swap Case       :", s.swapcase())     # Swaps uppercase to lowercase and vice versa

print("-" * 50)

# Checking Methods (Returns True or False)
print("Is Lowercase    :", s.islower())      # Checks if all letters are lowercase
print("Is Uppercase    :", s.isupper())      # Checks if all letters are uppercase
print("Is Title Case   :", s.istitle())      # Checks if the string is in title case
print("Is Digit        :", s.isdigit())      # Checks if all characters are digits
print("Is Alphabet     :", s.isalpha())      # Checks if all characters are alphabets
print("Is Alphanumeric :", s.isalnum())      # Checks if all characters are letters or numbers

print("-" * 50)

# Removing Characters
print("Strip           :", s.strip("-"))     # Removes '-' from both ends
print("Left Strip      :", s.lstrip("-"))    # Removes '-' from the left side
print("Right Split     :", s.rsplit("-"))    # Splits the string from the right using '-'

print("-" * 50)

# Searching and Matching
print("Starts with 't' :", s.startswith("t"))  # Checks if string starts with 't'
print("Ends with 'g'   :", s.endswith("g"))    # Checks if string ends with 'g'
print("Count of 'T'    :", s.count("T"))       # Counts occurrences of 'T'
print("Index of 's'    :", s.index("s"))       # Returns the index of the first 's'

print("-" * 50)

# Replacing Characters
print("Replace 't'->'1':", s.replace("t", "1"))  # Replaces all 't' with '1'