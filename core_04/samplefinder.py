
# print line number where python is written
with open("c:/python_lect/core_04/sample.html") as f:
    lines = f.readlines()
    
lineno = 1
for line in lines:
    if("python" in line):
        print(f"python found: line number is - {lineno}") 
        break
    lineno += 1

else:
    print("no python is present")

