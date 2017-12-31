def CalProbability(Data):
    R = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6']
    Count = np.zeros(np.max(Data[:,2:8])+1)
    
    for i in range(len(Data)):
        for r in range(2,8):
            Count[Data[i,r]] += 1
            
    P_Count = Count[1:]/581

    return P_Count