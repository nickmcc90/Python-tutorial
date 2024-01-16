# tuples - collections which are ordered and unchangeable

student = ("Bro",21,"male") # uses parenthesis

print(student.count("Bro")) # counts how many instances of Bro there are
print(student.index("male")) # returns the index of the certain value.

for x in student:
  print(x)

if "Bro" in student:
  print("Bro is here!")