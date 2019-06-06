import pandas as pd

tab1 = pd.read_csv('tab1.csv', delimiter=';')
tab2= pd.read_csv('tab2.csv', delimiter=';')

df = pd.merge(tab2, tab1, on='patNum')

df['amountAllowed'] = df['amountAllowed'].str.replace('$', '')
df['amountAllowed'] = df['amountAllowed'].str.replace(',', '.')
df['amountAllowed'] = df['amountAllowed'].str.replace(' ', '')

df['difference'] = df['difference'].str.replace('$', '')
df['difference'] = df['difference'].str.replace(',', '.')
df['difference'] = df['difference'].str.replace(' ', '')

df['amountPaid'] = df['amountPaid'].str.replace('$', '')
df['amountPaid'] = df['amountPaid'].str.replace(',', '.')
df['amountPaid'] = df['amountPaid'].str.replace(' ', '')

df['amountAllowed'] = df['amountAllowed'].astype(float)
df['difference'] = df['difference'].astype(float)
df['amountPaid'] = df['amountPaid'].astype(float)

df = df[['DOS', 'patNum']].groupby('patNum').count().merge(df, left_on='patNum', right_index=True)
df = df.drop(['DOS_y'], axis=1)
df.rename(columns={'DOS_x': 'count'}, inplace=True)

sample = df.sample(n=15, replace=True)

sample['weight'] = df['count'].count() / sample['count']

swdbc = sample['weight'].sum() * sample['count'].count()

print('MU HAT: Total Amount Paid Estimate:', ((sample.amountPaid * sample.weight).sum() / swdbc))

print('MU HAT: Total Amount Allowed Estimate:', (((sample.amountAllowed * sample.weight).sum()) / swdbc))

print('MU HAT: Total Difference Estimate:', (((sample.difference * sample.weight).sum()) / swdbc ))

print('------', (((sample.difference * sample.weight).sum()) / (sample.weight.sum() * sample.weight.count())))




