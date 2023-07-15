import numpy as np

tab = np.array([[15, 5, 1], [29, 12, 3], [43,33,5],[25,27,4]])
print(tab)

import pandas as pd

ligne_noms = ['ali', 'badr', 'cimon','rachid']
colonne_noms = ['age', 'score', 'bonus']

data = pd.DataFrame(tab, index=ligne_noms, columns=colonne_noms)
print(data)

sorted_data_ligne = data.sort_index()
print(sorted_data_ligne)

sorted_data_colonne = data.sort_index(axis=1)
print(sorted_data_colonne)

#groupedData = data.groupby('age')
#print(groupedData)

#groupedDatas = data.groupby('age', 'score')
#print(groupedDatas)

#groupedData.groups

df = pd.DataFrame({'Nom': ['Amin', 'Adil', 'Ahmed', 'Badr','Mohamed'], 
 'Diplome': ['Ingénieur', 'DESA', 'PHD', 
 'ingénieur', 'Phd'], 
 'Age': [22, 25, 35, 23, 30]})

print(df)
print(df.columns)
print(df.index)
print(df.head)
print(df.tail)
print(df.tail(2))
df[1 :3]
df.Nom
#df ['Nom']
#df.loc[ :10,[Nom,Diplome]]
df.iloc[:10,[0,1]]

df.describe()


from sklearn import datasets
iris=datasets.load_iris() 

print(iris.data)
print(iris.target)
print(iris.target_names)
print(iris.feature_names) 

data_df= pd.DataFrame(iris.data)

print(data_df)
print(data_df.columns)
print(data_df.index)

data_df.columns = ['Sepal_Length','Sepal_width','Petal_Length','Petal_width']

print(data_df)
print(data_df.size)

print(data_df.head())
print(data_df.head(3))
print(data_df.tail())
print(data_df.tail(2))

print(data_df[1 :3])
print(data_df.Sepal_Length)
print(data_df['Sepal_width'])
print(data_df.loc[ :10,['Sepal_width','Petal_width']])
print(data_df.iloc[:10,[0,1]])
