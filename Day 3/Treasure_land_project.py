print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
occupation = input("welcome to the one piece world, the one piece treasure is now in your hand; so what occupation do you choose P for pirate or M for marine? P or M ")


if occupation == 'P':
    equipment = input('what do you choose either magic tools or  ship for your adventure, type ship or tools? T or S ')
    if equipment == 'S':
        direction= input('you arrived at the sea unharmed. you have to choice for sea talents; instict or storm sense. which talent do you choose? I OR S')
        if direction == 'S':
            test = input('you have arrived at the island of raftel do you want to see for yourself even though you might loose your life or still continue to roam? enter either see or roam')

            if test == 'see':
                print('Your courage has been rewarded, hurray the wealth of the one piece world belongs to you now!!!!! ')
            else:
                print('Oops you lost the tresure because of your cowardise. Game over!!')
        else:
            print('Game Over!!')
    else:
        print('Game Over')
else:
    print('Game Over!!!')
