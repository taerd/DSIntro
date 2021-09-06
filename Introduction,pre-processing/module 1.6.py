import pandas as pd
import numpy as np

student_performance = pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')

#groupby
print(student_performance.groupby('gender').mean())
#aggregate and dictionary how to use aggregate
print(student_performance.groupby(['gender','race/ethnicity'])\
      .aggregate({'math score':'mean', 'reading score':'mean'})\
      .rename(columns= {'math score': "mean_math_score",'reading score': "mean_reading_score"})
      )
mean_scores=student_performance.groupby(['gender','race/ethnicity'])\
      .aggregate({'math score':'mean', 'reading score':'mean'})\
      .rename(columns= {'math score': "mean_math_score",'reading score': "mean_reading_score"})
print(mean_scores.index)
print(mean_scores.loc[[('female','group A'),('male','group A')]])


mean_scores=student_performance.groupby(['gender','race/ethnicity'],as_index = False)\
      .aggregate({'math score':'mean', 'reading score':'mean'})\
      .rename(columns= {'math score': "mean_math_score",'reading score': "mean_reading_score"})
#Print a unique values
print(student_performance['math score'].unique())
print(student_performance['math score'].nunique())

#number of unique values at each group
print(student_performance.groupby(['gender','race/ethnicity'])['math score'].nunique())
print(type(student_performance.groupby(['gender','race/ethnicity'])['math score'].nunique()))

#top 5 best female and male on math score
print(student_performance.sort_values(['gender','math score'],ascending=False)\
      .groupby('gender').head(5))

#adding column
student_performance['total_score']=student_performance['math score']+student_performance['reading score']+student_performance['writing score']
print(student_performance)

#another way to do something with columns
student_performance = student_performance.assign(total_score_log = np.log(student_performance.total_score))
print(student_performance)

#axis  = 1 override column drop
student_performance=student_performance.drop(['total_score','lunch'],axis=1)
print(student_performance)

#task 1
heroes = pd.read_csv('https://stepik.org/media/attachments/course/4852/dota_hero_stats.csv')
print(heroes.groupby('legs').nunique())

#task 2
workers = pd.read_csv('https://stepik.org/media/attachments/course/4852/accountancy.csv')

workers = workers.drop('Unnamed: 0',axis =1)
print(workers.head(5))
print(workers.groupby(['Executor','Type']).mean())

#task 3
print(heroes.columns)
print(heroes.groupby(['attack_type','primary_attr']).nunique())

#task 4
df = pd.read_csv('http://stepik.org/media/attachments/course/4852/algae.csv')
print(df.head(5))
pd.options.display.max_columns = None
print(df.groupby('genus')['alanin'].describe())
#best way to do the task is add aggregate
print('. . . . . . . . another way . . . . . . . . . .. ')
print(df.groupby('genus').aggregate(['min','mean','max']).loc['Fucus','alanin'].round(2))


#task 5
print(df.columns)
print(df.groupby('group')['citrate'].aggregate(['var']))
#to do all best way
print(df.groupby('group').aggregate({'citrate':'var','sucrose': lambda x : x.max()-x.min(), 'glucose': 'count'}))


