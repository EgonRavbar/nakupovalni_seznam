seznam = []
x = 1
while x != "1":
    a= raw_input("Zdravo, zelis nadaljevati?(da/ne)")
    if a == "da":
        print("Super! Naj ti pomagam.")
        x = raw_input("Vpisi zivilo:")
        seznam.append(x)
    elif a == "ne":
        print seznam
        break
