# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# my own attempt long but neat
'''list = position.split()
num1 = int(list[0][1])
num2 = int(list[0][0])
map[num1-1][num2-1] = 'X'
'''
# more neater attempt, lesson learnt simplicity isthe way
vertical = int(position[0])
horizontal = int(position[1])

map[vertical-1][horizontal-1] = 'x'



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")