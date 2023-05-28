# Average height of a bunch of students-

students_height = input("Please enter the height of the students \n").split()
for n in range(0, len(students_height)):
     students_height[n]= int(students_height[n])

total_height = sum(students_height)
num_students = len(students_height)

avg_height = (total_height/num_students)

print(type(avg_height))

print(f"The average height of the students is {avg_height}")
