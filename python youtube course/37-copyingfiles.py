# copyfile() = copies contents of file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)



import shutil

shutil.copyfile("file path","new copy name") # first = the file location, second = the new file name

# copy and copy 2 take the same arguments.