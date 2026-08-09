# alpha ="abcdefghijklmnopqrstuvwxyz"

# # i = 25
# # print(alpha[i])
# # print(alpha[i+1])
# # print(alpha[i+2])
# # print(alpha[i+3]) --> it will give a error

# i = 27

# print(alpha[i%26]) # it wont give error as 27%26 == 1 as it gives the reminded.




# This is popularly called as Caesar Cipher in cryptography
alpha ="abcdefghijklmnopqrstuvwxyz"

s = "dinesh"
# i will print the sift of 1 latter like ejofti

t = ""
i = 0
k = 1

t = t + alpha[((alpha.index(s[i + 0]))+k)%26]
t = t + alpha[((alpha.index(s[i + 1]))+k)%26]
t = t + alpha[((alpha.index(s[i + 2]))+k)%26]
t = t + alpha[((alpha.index(s[i + 3]))+k)%26]
t = t + alpha[((alpha.index(s[i + 4]))+k)%26]
t = t + alpha[((alpha.index(s[i + 5]))+k)%26]

print(t)
