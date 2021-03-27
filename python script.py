a_file = open("frame11.txt", encoding="utf-8-sig")

a = []
for position, line in enumerate(a_file):
    a.append(line.split(","))
    
for i in range(len(a)):
    del a[i][1], a[i][2],a[i][3], a[i][4], a[i][5]

with open('listfile1.txt', 'w', encoding='utf-8-sig') as filehandle:
    filehandle.writelines("%s\n" % place for place in a)

with open('listfile1.txt', 'r', encoding='utf-8-sig') as f, open('frame11.txt', 'w', encoding='utf-8-sig') as fo:
    for line in f:
        fo.write(line.replace("'", "").replace("[", "").replace("]", "").replace('"', '').replace("\\n", "").replace(" ", ""))
