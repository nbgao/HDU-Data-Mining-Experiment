def CutSets(Sets, C, minSup, length):
    for i,s in enumerate(Sets):
        if float(C[i]) /length < minSup:
            Sets.remove(s)

    return Sets