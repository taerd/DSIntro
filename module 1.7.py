import inline as inline
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

#rename columns at csv
student_performance = pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')
student_performance.columns = [x.replace (" ","_") for x in student_performance.columns]

#view  histogram of math_score
#student_performance.math_score.hist()
#plt.show()

#scattered plot
#student_performance.plot.scatter(x='math_score',y='reading_score')
#plt.show()

#ax = sns.lmplot(x='math_score',y='reading_score',hue='gender',data=student_performance)
#ax.set_xlabels('Math score')
#ax.set_ylabels('Readng score')
#plt.show()

#task
#df=pd.read_csv('https://stepik.org/media/attachments/course/4852/income.csv')
#df.income.plot()
#sns.lineplot(data=df)
#plt.plot(df.index,df.income)
#sns.lineplot(x=df.index, y=df.income)
#df.plot()
#df.plot(kind='line')
#df['income'].plot()
#plt.show()

#task 2
#df2 = pd.read_csv("dataset_209770_6.txt", sep=" ")
#print(df2)
#df2.plot.scatter(x='x',y='y')
#plt.show()


#task 3

#df=pd.read_csv('https://stepik.org/media/attachments/course/4852/genome_matrix.csv',index_col=0)
#g=sns.heatmap(data=df,cmap="viridis")
#g.xaxis.set_ticks_position('top')
#g.xaxis.set_tick_params(rotation=90)
#plt.show()

#task 4
df=pd.read_csv("https://stepik.org/media/attachments/course/4852/dota_hero_stats.csv")
#
#hero_role=[]
#sum=0
#cnt=0
#for x in df['Unnamed: 0']:
#   sum+=df.iloc[x].roles.count(',')+1
#   cnt+=1
#print(sum/cnt)

#another way
#print(df.roles.str.split(',').apply(len).mode())

#way with histogram
#df.roles.agg(lambda x: len(x.split(','))).hist()
#plt.show()


#task 5
df=pd.read_csv('https://stepik.org/media/attachments/course/4852/iris.csv')
print(df)

#sns.distplot(df['sepal length'])
#plt.show()

#sns.distplot(df['sepal width'])
#plt.show()

#sns.distplot(df['petal length'])
#plt.show()

#sns.distplot(df['petal width'])
#plt.show()

#sns.distplot(df['species'])
#plt.show()


# распределения; Унимодальное,Бимодальное и видно размах
#sns.kdeplot(df.index,df['sepal length'])
#plt.show()

#sns.kdeplot(df.index,df['sepal width'])
#plt.show()

#sns.kdeplot(df.index,df['petal length'])
#plt.show()

#sns.kdeplot(df.index,df['petal width'])
#plt.show()

#sns.kdeplot(df.index,df['species'])
#plt.show()

# коробка с усами
#sns.violinplot(y=df['petal length'])
#plt.show()

#зависимость пар переменных
df.drop('Unnamed: 0',axis=1)
# hue - по species разделения по цветам
sns.pairplot(df,hue='species')
plt.show()






