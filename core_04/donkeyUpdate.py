word = "donkey"
with open("c:/python_lect/core_04/donkey.txt") as f:
   data = f.read()

newData = data.replace(word, "#####")

with open("c:/python_lect/core_04/donkey.txt", "w") as f:
   f.write(newData)
   

   
      

