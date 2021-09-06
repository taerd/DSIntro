import pandas as pd
import numpy as np
#task 1
d={'type' : ['A','A','B','B'],'value' : [10,14,12,23]}
my_data=pd.DataFrame(data=d)
print(my_data)

#task 2
df= pd.read_csv('https://stepik.org/media/attachments/course/4852/my_stat.csv')
print(df)
subset_1=df.iloc[0:9,[0,2]]
print(subset_1)
subset_2=df.iloc[:,[1,3]].drop([0,4],axis=0)
print(subset_2)

#task 3
#subset_1 = df.loc[[x for x in list(df.V1) if x>0]]
subset_1=df.query("V3=='A' & V1>0")
subset_2=df.query("V2!=10 or V4>=1")

#subset_1 = df[(df['V1'] > 0) & (df['V3'] == 'A')]
#subset_2 = df[(df['V2'] != 10) | (df['V4'] >= 1)]
print(subset_1)
print(subset_2)

#task 4
df['V5']=df.V1+df.V4
df=df.assign(V6=np.log(df.V2))
print(df)

#task 5
#df=df.rename(columns={"V1":"session_value","V2":"group","V3":"time","V4":"n_users"})

#another way , but you need to write all namecolumns
df=df.drop(['V5','V6'],axis=1)
df.columns = ['session_value','group','time','n_users']
print(df)

#task 6
df=pd.read_csv('https://stepik.org/media/attachments/course/4852/my_stat_1.csv')
df=df.fillna(value={"session_value":0})
med=pd.DataFrame([x for x in list(df.n_users) if x>=0]).median(axis=0)
df.loc[df.n_users<0.0,'n_users']=med[0]

#task 7
mean_session_value_data=df.groupby('group',as_index=False).aggregate({"session_value":'mean'}).rename(columns={"session_value":"mean_session_value"})
print(mean_session_value_data)