import random

def Predict():
    L = []
    while len(L)<6:
        p = 6*random.random()
        for i in range(0,33):
            if p<C_Count[i]:
                if((i+1) not in L):
                    L.append(i+1)
                    break;

    L = np.sort(L)
    print(L)
    return L