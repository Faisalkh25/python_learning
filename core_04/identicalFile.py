
with open("c:/python_lect/core_04/file.txt") as f:
  content =  f.read().strip()

with open("c:/python_lect/core_04/file2.txt") as f:
 content2 =  f.read().strip()

if(content == content2):
  print("file is same")
else:
  print("file is not same")
