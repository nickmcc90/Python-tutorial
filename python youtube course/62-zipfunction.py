# zip(*iterables) = aggregate elements from two or more iterables (lists, tuples, sets, etc.)

usernames = ["Dude","Bro","Mister"]
passwords = ("p@ssword","abc123","guest")

users = zip(usernames,passwords)

for i in users:
  print(i)

# or in a dictionary
  
users = dict(zip(usernames,passwords))

for key,value in users.items():
  print(key+" : "+value)

# not limited to two iterables.
  
usernames = ["Dude","Bro","Mister"]
passwords = ("p@ssword","abc123","guest")
login_date = ["1/1/2021","2/2/2022","3/3/2023"]

users_dated = zip(usernames,passwords,login_date)

for i in users_dated:
  print(i)