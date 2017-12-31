import sys

def Apriori(Data, minSup):
    n = len(Data)
    C1 = {}
    for L in Data:
        for x in L:
            if x in C1:
                C1[x] += 1
            else:
                C1[x] = 1

    Keys = C1.keys()


    Set1 = []
    for i in Keys:
        Set1.append([i])

    cutSets = []

    for S in Set1[:]:
        if C1[S[0]]*1.0/n >= minSup:
            cutSets.append(S)

    cutSets.sort()

    allSets = []
    Sets = cutSets
    while Sets != []:
        C = SetCount(Data, Sets)
        cutSets = CutSets(Sets, C, minSup, n)
        for S in cutSets:
            if len(S) <= 6:
                allSets.append(S)
        Sets = GenerateSets(cutSets)

    return allSets

