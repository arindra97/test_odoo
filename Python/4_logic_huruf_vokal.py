# Input the words
word = input("Input / Masukan kata : ")

# define the vowels
vowels = ['a','i','u','e','o']

# declare the vocal
vocal = 0
# count of words containing vowels
for i in word:
    if(i in vowels):
        vocal += 1

# print the result
if vocal:
    print("Count of vocal words : ", vocal)
else:
    print("No vocal words found.")