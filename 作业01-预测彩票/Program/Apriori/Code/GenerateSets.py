def GenerateSets(Set1):
    Set2 = []
    for s1 in Set1:
        for s2 in Set1:
            if s1 != s2:
                Set = []
                for s in s1:
                    if s not in Set:
                        Set.append(s)

                for s in s2:
                    if s not in Set:
                        Set.append(s)

                Set.sort()
                if Set not in Set2:
                    Set2.append(Set)

    return Set2