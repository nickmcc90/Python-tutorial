# list comprehension = a way to create a new list with less syntax

# list = [expression for item in iterable if conditional]
#     --or--
# list = [expression (if/else) for item in iterable]     this is if there is an else statement, move it to before the 'for'

# this way is without list comprehensions.
squares = []
for i in range(1,11):
  squares.append(i * i)
print(squares)                # this should print out a list of squares from 1 to 11.


squares = [i * i for i in range(1,11)]
print(squares)                            # this way is list comprehensions.



# ANOTHER EXAMPLE

students = [100,90,80,70,60,50,40,30,20,10]

passed_students = list(filter(lambda x:x >=60, students))
print(passed_students)                      # without comprehensions

#with comprehensions
passed_students = [i for i in students if i >= 60]
print(passed_students)

#with max complexity

passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)