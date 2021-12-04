import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('graf.csv', delimiter=',', header=None, names=['Date UTC', 'how many unique addresses are generated by transactions on the network'])

Date_UTC = df['Date UTC'].values.tolist()
Nums_of_transact = df['how many unique addresses are generated by transactions on the network'].values.tolist()
Date_UTC_new = []
Nums_of_transact_new = []
sum = 0
for i in range(len(Date_UTC)-1):
    if Date_UTC[i] == Date_UTC[i+1]:
        sum += Nums_of_transact[i]
    else:
        Date_UTC_new.append(Date_UTC[i])
        Nums_of_transact_new.append(sum)
        sum = 0
Date_UTC_new_series = pd.Series(Date_UTC_new)
Nums_of_transact_new_series = pd.Series(Nums_of_transact_new)
df_last = pd.DataFrame(columns = ['Date UTC', 'how many unique addresses are generated by transactions on the network'])
df_last['Date UTC'] = Date_UTC_new_series
df_last['how many unique addresses are generated by transactions on the network'] = Nums_of_transact_new_series

df_last.plot()