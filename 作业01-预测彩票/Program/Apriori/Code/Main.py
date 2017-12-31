import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table('data2.TXT')
df.head(10)

DT = df.get_values()
DT

X = np.linspace(1,33,33)
P_Count = CalProbability(DT)

plt.figure(figsize=(10,6))
plt.plot(X, P_Count, '-o');


'''频繁项集算法求解'''
# 最小支持度
minSup = 0.193

P_Count = CalProbability(DT)
print("频繁1项集中集合个数:", np.count_nonzero(P_Count>minSup))

# Apriori算法
F = Apriori(DT[:,2:8], minSup)
F

Sum, Result = CountN(F, n=6)
print("频繁6项集总共%d个" %Sum)

# 列出所有的频繁6项集
Result


file = './Output_Apriori.txt'
Output(Result, file)