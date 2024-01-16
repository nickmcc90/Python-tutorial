# unordered, changeable collection of unique key:value pairs

capitals = {"USA":"Washington DC",
          "India":"New Dehli",
          "China": "Beijing"
          }

print(capitals['China']) # this isn't too safe because if we type something that isn't in the dictionary, it interrupts flow.
print(capitals.get["Germany"]) # this just returns None and is safer
print(capitals.keys()) # prints all the keys
print(capitals.values()) # prints all the values
print(capitals.items()) # prints all the everything in it

capitals.update({"Germany":"Berlin"}) # this update brings in a whole new key and value
capitals.update({"USA":"Las Vegas"}) # this update changes an existing value of the key USA
capitals.pop("China") # this gets rid of a key and value pair given just the key
capitals.clear() # gets rid of everything


for key,value in capitals.items(): # this also prints the entire dictionary
    print(key,value)

