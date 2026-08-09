# If condition

# Let's consider the movie "Avengers". This is an 13+ Movie.

print("Enter your data of birth:")
birth_year = int(input())

current_year = 2021

age = current_year - birth_year

if(age<13):
    print("You should not watch this movie.")
else:
    print("You can watch this movie.")