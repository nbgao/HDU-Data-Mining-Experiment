import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table('data2.TXT')
DT = df.get_values()
DT

# 红球各数字概率分布图
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

# 计算累计概率
C_Count = np.cumsum(P_Count)
print(C_Count)

plt.figure(figsize=(10,6))
plt.plot(X, C_Count, '-o');


# 概率分布饼图
X = np.arange(1,34)
plt.figure(figsize=(8,8))
plt.pie(P_Count, labels=X, startangle = 90,autopct='%1.2f%%', pctdistance=0.90);


'''轮盘赌预测'''
Result = []
for i in range(20):
    print("%d: " %(i+1), end='')
    Result.append(Predict())


file = './Output_RandomPredict.txt'
Output(Result, file)