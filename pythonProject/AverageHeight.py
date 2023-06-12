# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
print(student_heights)

sum_of_heights = 0
number_of_heights = 0


for height in student_heights:
   sum_of_heights += int(height)
   number_of_heights += 1

average_height = round(sum_of_heights/ number_of_heights)

print(f"The sum is {sum_of_heights}, and there are {number_of_heights} numbers to be added.")
print(f"That being said, the average height is {average_height}.")


