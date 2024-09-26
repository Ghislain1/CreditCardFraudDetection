import pandas as pd

# read
data_df = pd.read_csv("creditcard.csv")
#print("Credit Card Fraud rows:", data_df.shape[0], "Colomns:", data_df.shape[1])

#darstellung der 5te erste Zeile
d_head = data_df.head()
#print(d_head)

#darstellung der 5te letzte Zeile
d_tail = data_df.tail()
#print(d_tail)

#look into more details to the data.
d_descrip = data_df.describe()
#print(d_descrip)

# check if there is any missing data
sum = data_df.isnull().sum()
count = data_df.isnull().count()
percent = sum / count*100
join = pd.concat(objs=[sum, percent], axis = 1, keys= ['sum', 'percet'])
print(join)
transp = join.transpose()
print(transp)
