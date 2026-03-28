
 

def tableGenerator(n):

    table = ""
    for i in range(1, 11):
        table += f"{n} * {i} = {n*i}\n"

    with open(f"c:/python_lect/core_04/tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2,21):
    tableGenerator(i)

