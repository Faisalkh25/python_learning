
with open("c:/python_lect/core_04/file.txt") as f:
   content = f.read()

with open("c:/python_lect/core_04/newFile.txt", "w") as f: 
   f.write(content)