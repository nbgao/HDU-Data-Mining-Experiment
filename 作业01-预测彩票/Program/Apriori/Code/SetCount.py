def SetCount(Data, Sets):
    C = []
    for Set in Sets:
        c = 0
        for L in Data:
            flag = True
            for s in Set:
                if s not in L:
                    flag = False

            if flag==True:
                c += 1
        C.append(c)

    return C