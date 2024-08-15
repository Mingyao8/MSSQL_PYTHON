import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\user\\Desktop\\HW_0809.csv", usecols=['DateTime', 'Point', 'vFloat', 'vInt', 'vBool'], index_col=0, nrows=900)
data = pd.DataFrame(data)

data.to_csv("C:\\Users\\user\\Desktop\\test.csv")

data['SUM'] = data.iloc[:, 1:4].sum(axis=1)
data['SUM'] = data.apply(
    lambda row: row['vFloat'] + row['vInt'] if row['vBool'] == 0 else 1,
    axis=1
)

res = data.pivot_table(values='SUM', index='DateTime', columns='Point')

res2 = res['A10  ']

# temp = res.index.tolist()
# arr_lb = [temp[i] for i in range(0, len(temp), 400)]
# arr_tk = [i for i in range(0, len(temp), 400)]

# plt.figure(figsize=(15, 5))
# res2.plot()
# plt.xticks(ticks=arr_tk, labels=arr_lb, rotation = 30)
# plt.axhline(y = 442 , color = 'gray' , linestyle = "--")
# plt.axvline(x = 6000 , color = 'gray' , linestyle = "--")
# plt.show()