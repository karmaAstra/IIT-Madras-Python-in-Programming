# alpha ="abcdefghijklmnopqrstuvwxyz"

# # i = 25
# # print(alpha[i])
# # print(alpha[i+1])
# # print(alpha[i+2])
# # print(alpha[i+3]) --> it will give a error

# i = 27

# print(alpha[i%26]) # it wont give error as 27%26 == 1 as it gives the reminded.

alpha ="abcdefghijklmnopqrstuvwxyz"

s = "dinesh"
# i will print the sift of 1 latter like ejofti

print(alpha[(alpha.index(s[2])+1)%26])
