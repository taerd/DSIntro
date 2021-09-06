import pandas as pd
import numpy as np

student_perfomrance=pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')
#print(student_perfomrance)
#print(student_perfomrance.head(5))
#print(student_perfomrance.tail(5))
#print(student_perfomrance.describe())
#print(student_perfomrance.dtypes)
#print(student_perfomrance.shape)
#take means of writing score by gender
#print(student_perfomrance.groupby('gender').aggregate({'writing score': 'mean'}))

#Took from table first 5 records and their first 3 columns (iloc)
print(student_perfomrance.head(5))
print(student_perfomrance.iloc[0:5,0:3])
print(student_perfomrance.iloc[[1,3,5],[0,1,-1]])
#another way using labels columns  (loc)
print(student_perfomrance.iloc[[0,3,4,7,8]])
student_perfomrance_with_names=student_perfomrance.iloc[[0,3,4,7,8]]
student_perfomrance_with_names.index = ["a1","a2","a3","a4","a5"]
print(student_perfomrance_with_names)
print(student_perfomrance_with_names.loc[["a1","a4"],["gender","writing score"]])

#dataframe ,  series - array
print(" . . . . . . . . . . ")
print(student_perfomrance_with_names.iloc[:,0])
print(type(student_perfomrance_with_names.iloc[:,0]))
print(type(student_perfomrance_with_names))
print(pd.Series([1,2,3]))

#"vacya","misha","anatolyi"
my_series_1=pd.Series([1,2,3],index = ["cergey","macya","grisha"])
my_series_2=pd.Series([4,5,6], index = ["cergey","macya","grisha"])
#dictianary where key - col name  and value - my_series_
print(pd.DataFrame({'col_name_1': my_series_1, 'col_name_2':my_series_2}))

#Series
print(" this is series, tooks only records at columb 'gender'")
print(student_perfomrance_with_names['gender'])
print(student_perfomrance_with_names['gender'].shape)
print(" this is dataframe, tooks dataframe with column 'gender'")
print(student_perfomrance_with_names[['gender']])
print(student_perfomrance_with_names[['gender']].shape)




#task
print("task")
task_df=pd.read_csv('https://stepik.org/media/attachments/course/4852/titanic.csv')
print(task_df.tail(5))
print("count columns is ", task_df.columns.size)
print("count rows is ", task_df.size/task_df.columns.size)
print("dtypes \n", task_df.dtypes)
