import os
import shutil


try:
  os.remove("file path") # deletes a file
except FileNotFoundError:
  print("That file was not found")

# also, 
  
os.rmdir('folder') #deletes a directory



shutil.rmtree(path) # this deletes a folder full of files.