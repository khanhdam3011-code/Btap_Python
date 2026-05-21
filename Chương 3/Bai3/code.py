with open("input.txt", "r") as f_in:
    lines = f_in.readlines()

ket_qua = []

for line in lines:
    line = line.strip()
    if line == "":
        continue

    k = int(line)
    uoc = []
    d = 2
    temp = k

    while temp > 1:
        if temp % d == 0:
            uoc.append(d)
            while temp % d == 0:
                temp = temp // d
        d = d + 1

    chuoi_uoc = ""
    for x in uoc:
        chuoi_uoc = chuoi_uoc + str(x) + " "

    ket_qua.append(chuoi_uoc.strip())

with open("output.txt", "w") as f_out:
    for dong in ket_qua:
        f_out.write(dong + "\n")