# sort() method = used with lists
# sorted() function = used with iterables

students = ["apples","oranges","bananas","turnips"]

students.sort()

for i in students:
  print(i)

#this should output the list in alphabetical order
# or we could do this to put it in reverse:
students.sort(reverse=True)

#this only works on lists "[]". With tuples however.... ()

students = ("apples","oranges","bananas","turnips")
sorted_students = sorted(students)
#we can do...
sorted_students = sorted(students,reverse=True)

# what if we had a list of tuples that we wanted to sort by a specific column?

students = [("Nick","A",60),
            ("Sandy","B",80),
            ("Albert","C",70)]

grade = lambda grades:grades[1]
students.sort(key=grade,reverse=True)

for i in students:
  print(i)

# if it was a tuple of tuples, then we use the sorted function

sorted_students = sorted(students,key=grade)