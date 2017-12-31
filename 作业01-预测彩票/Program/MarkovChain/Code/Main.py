import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table('data2.TXT')
df.head(10)

DT = df.get_values()
DT


X = np.linspace(1,33,33)
R = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6']
Count = np.zeros(max(df['R6'])+1)
len(Count)
for i in range(len(df)):
    for r in R:
        Count[df.iloc[i][r]] += 1
        
P_Count = Count[1:]/581
plt.figure(figsize=(10,6))
plt.plot(X, P_Count, '-o');


'''转移统计矩阵'''
n = len(DT)
P = np.zeros(34*34).reshape((34,34))

for i in range(1,len(DT)):
    L = DT[i, 2:8]
    L_pre = DT[i-1, 2:8]
    for j in range(2,8):
        x = DT[i-1,j]
        for k in range(2,8):
            y = DT[i,k]
            P[x,y] += 1
P


'''马尔可夫转移概率矩阵'''
PP = np.zeros(34*34).reshape((34,34))
for i in range(1,34):
    S = np.sum(P[i])
    #for j in range(1,34):
    PP[i,:] = P[i,:]/S
    
PP


'''根据最后一期进行预测'''
# 最近一期红球号
L_now = DT[-1, 2:8]
L_now

# 根据马尔科夫转移概率最大化预测
L_predict = []
for i in range(6):
    x = L_now[i]
    y = np.argmax(PP[x])
    while y in L_predict:
        PP[x,y] = 0
        y = np.argmax(PP[x])
    L_predict.append(y)

L_predict

# 结果排序
L_predict.sort()
L_predict


'''结果数据导出函数'''
def Output(L, file):
    fout = open(file, 'w')
    
    for i in range(len(L)):
        fout.write(str(L[i]) + '\t')
    
    print("数据成功导出到文件中")
    fout.close()


file = './Output_MarkovChain.txt'
Output(L_predict, file)