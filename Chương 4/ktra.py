with open("input.txt", "r") as f_in:
    data = f_in.read().split()

chu = []
so = []

for item in data:
    if item.isdigit():
        so.append(item)
    else:
        chu.append(item)

with open("outchu.txt", "w") as f_chu:
    for x in chu:
        f_chu.write(x + "\n")

with open("outso.txt", "w") as f_so:
    for x in so:
        f_so.write(x + "\n")