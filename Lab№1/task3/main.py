in_file = open('m.txt').read().splitlines()
map = [line.split() for line in in_file]

duple_row = []
for i in range (len(map)):
        if len(set(map[i])) < len(map[i]):
            duple_row.append(i)

if duple_row:
    print("Duplications:", *duple_row)
else:
    print("None")
