# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f'The highest score in the class is: {max}')       
 # learning never ends
max = student_scores[0]

for x in student_scores:
    if x > max:
        max = x
print(f'The highest score in the class is: {max}')