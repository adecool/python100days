#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('Welcome to the tip calculator.')
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
tip_percent +=1
num_of_persons = int(input("How many peple to split the bill? "))
pay_per_person = round((total_bill/num_of_persons) * tip_percent, 2)
# or "{:.2f}".format(pay_per_person)

print(f'Each person should pay: ${pay_per_person}')