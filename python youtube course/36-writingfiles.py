text = "YOOOOOOOO\n get tf outta here"

with open('test.txt','w') as file: # the default second argument in open() is 'r' for read, but changing to 'w' makes it so that we can write a file.
  file.write(text)


with open('test.txt','a') as file: # 'a' means append, and since each new write overwrites the file, 'a' appends new text.
  file.write(text)