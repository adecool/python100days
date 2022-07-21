# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_low = name1.lower()
name2_low = name2.lower()
lovers_name = name1_low + name2_low
T = lovers_name.count('t')
R= lovers_name.count('r')
U = lovers_name.count('u')
E = lovers_name.count('e')
L = lovers_name.count('l')
O = lovers_name.count('o')
V = lovers_name.count('v')
E = lovers_name.count('e')

TRUE = T+R+U+E
LOVE = L+O+V+E

love_score = int(str(TRUE) + str(LOVE))
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together."
)
else:
    print(f"your score is {love_score}, you two don't match.")