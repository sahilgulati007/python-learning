# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sum_height = 0
total_stud = 0
for student_height in student_heights :
  sum_height += student_height
  total_stud += 1
print(round(sum_height/total_stud))


