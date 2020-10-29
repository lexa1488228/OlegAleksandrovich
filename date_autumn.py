def date_autumn(dates):
    x = []
    l = []
    p = []
    b = []
    for i in dates:
        p = i.split("-")
        if p[0] == "09" or p[0] == "10" or p[0] == "11":
            x.append(p)
    max = int(x[-1][2])
    for i in x:
        if max <= int(i[2]):
            l.append(i)
            max = int(i[2])
    data = int(i[-1][1])
    for i in l:
        if data <= int(i[1]):
            p.append(i)
            data = int(i[1])
    for i in range(len(p)):
        for j in range(len(p[i])):
            b.append(p[i][j])
    return "-".join(b)