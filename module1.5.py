import pandas as pd
import numpy as np

student_performance = pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')
print(student_performance.head(5))
# takes records where gender='female' using .loc (indexeed)
print(student_performance.loc[student_performance.gender == 'female', ['gender', 'writing score']])
# takes records where writing score(-1 column) >70
print(student_performance.loc[student_performance.iloc[:, -1] > 70])
# biggest than mean of writing score
mean = student_performance['writing score'].mean()
print(student_performance.loc[student_performance['writing score'] > mean])
# student_performance.loc[student_performance.loc['writing score']]

# task 1, better use len() then size/columns.size
print((student_performance.loc[student_performance['lunch'] == 'free/reduced'].size / (
    student_performance.columns.size)) / (student_performance.size / (student_performance.columns.size)))
# task 2
print(student_performance.loc[student_performance['lunch'] == 'free/reduced'].describe())
print(student_performance.loc[student_performance['lunch'] != 'free/reduced'].describe())

# rename columns
student_performance.columns = [x.replace(" ","_") for x in student_performance.columns]
print(student_performance)
# or
#students_performance = student_performance \
#    .rename(columns=
#            {'parental level of education': 'parental_level_of_education',
#             'test preparation course': 'test_preparation_course',
#             'math score': 'math_score',
#             'reading score': 'reading_score',
#             'writing score': 'writing_score'}
#            )
#print(student_performance)

print(student_performance.query("writing_score > 74"))
print(student_performance.query("gender=='female' & writing_score >78"))
#Экранирование в query
writing_score_query=78
print(student_performance.query("writing_score > @writing_score_query"))

#finding columns where score in name of column
score_columns=[i for i in list(student_performance) if 'score' in i]
print(student_performance[score_columns])
#or
print(student_performance.filter(like='score'))
#if u need to take records from df which some filter u must add at filter axis=0
#to do the like="smtng" on records