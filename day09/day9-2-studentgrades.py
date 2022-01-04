student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
for stud in student_scores:
  if student_scores[stud] > 90:
    student_grades[stud] = "Outstanding"
  elif student_scores[stud] > 80:
    student_grades[stud] = "Exceeds Expectations"
  elif student_scores[stud] > 70:
    student_grades[stud] = "Acceptable"
  else :
    student_grades[stud] = "Fail"

#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
print(student_grades)
