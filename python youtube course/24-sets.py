# a set is a collection that is unordered and unindexed. No duplicate values.

utensils = {"fork","spoon","knife"}
dishes = {"bowl", "plate", "cup","knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()

utensils.update(dishes) # this puts all the values of dishes into the utensils set.

dinner_table = utensils.union(dishes) # this makes a new set with both the utensils and dishes sets in it.

print(utensils.difference(dishes)) # gives a set of what utensils has that dishes doesn't

print(utensils.intersection(dishes)) # gives a set of what utensils and dishes has in common.

for x in utensils:
  print(x)      # if we were to print this, the order will not be the same everytime. A set is faster than a list.


countries = {"America", "America"} # when printed, America will only show up once.