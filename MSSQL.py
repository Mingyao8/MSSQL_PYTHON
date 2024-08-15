import pandas as pd

data = pd.read_csv("C:\\Users\\user\\Desktop\\HW_0809.csv", usecols=['DateTime', 'Point', 'vFloat', 'vInt', 'vBool'], index_col=0, nrows=1000)
data = pd.DataFrame(data)

data['SUM'] = data.apply(
    lambda row: row['vFloat'] + row['vInt'] if row['vBool'] == 0 else 1,
    axis=1
)

res = data.pivot_table(values='SUM', index='DateTime', columns='Point')
res = res.fillna(0)

res.to_csv("C:\\Users\\user\\Desktop\\test.csv")
print(res)
