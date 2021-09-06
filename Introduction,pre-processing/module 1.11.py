import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.max_columns = None

events_data=pd.read_csv("../data/event_data_train.csv")
submissions_data=pd.read_csv("../data/submissions_data_train.csv")

#добавление столбца с понятной датой
events_data['date']=pd.to_datetime(events_data.timestamp,unit='s')
events_data['day']=events_data.date.dt.date
print(events_data.head())

submissions_data['date']=pd.to_datetime(submissions_data.timestamp,unit='s')
print(submissions_data.head())

#посчет выполненных степов для каждого пользователя
users_scores=submissions_data.pivot_table(index='user_id',
                                    columns='submission_status',
                                    values='step_id',
                                    aggfunc='count',
                                    fill_value=0).reset_index()
print(users_scores.head())

#уникальные timestamp для каждого user
print(events_data[['user_id','day','timestamp']].drop_duplicates(subset=['user_id','day'])\
      .groupby('user_id')['timestamp'].apply(list))
users_timestamps=events_data[['user_id','day','timestamp']].drop_duplicates(subset=['user_id','day'])\
      .groupby('user_id')['timestamp'].apply(list)

#np.diff([1,2,5]) out- array([1,3])
#узнаем сколько времени прошло между заходами user
print(users_timestamps.apply(np.diff))

#распределение перерывов у пользователей
gap_data=users_timestamps.apply(np.diff).values
print(gap_data)

#перевод array arrayev в один array
gap_data=pd.Series(np.concatenate(gap_data,axis=0))
#делим разницу между заходами в timestamp на дни
gap_data=gap_data/(24*60*60)
print(gap_data)

#визуализация перерывов
# gap_data[gap_data<200].hist()
# plt.show()

#квантиль 95 процентов
print(gap_data.quantile(0.95))

#квантиль 90 процентов
print(gap_data.quantile(0.90))

#hacker time trying to find userd_id anatoliy karpov
user_action=events_data[['user_id','day','action']].drop_duplicates(subset=['user_id','day'])
print(user_action.user_id.mode())
#user_action.pivot_table(index='user_id',columns='action',aggfunc='count')

#классификация отвалившихся пользователей
print(events_data.tail())

print(events_data.groupby('user_id',as_index=False)\
    .agg({'timestamp' : 'max'}).head())



users_data = events_data.groupby('user_id',as_index=False)\
    .agg({'timestamp' : 'max'}).rename(columns={'timestamp': 'last_timestamp'})

drop_out_threshold=30*24*60*60
now = users_data.last_timestamp.max()

users_data['is_gone_user']= (now - users_data.last_timestamp)>drop_out_threshold
print(users_data.head(10))

#merge 2 tables by user_id, default=inner join , outer- пересечение без выкинутых
users_data=users_data.merge(users_scores,on='user_id',how='outer')
users_data=users_data.fillna(0)
print(users_data.head())

#подчет событий пользователя
users_events_data=events_data.pivot_table(index='user_id',
                        columns='action',
                        values='step_id',
                        aggfunc='count',
                        fill_value=0).reset_index()

users_data=users_data.merge(users_events_data,on='user_id',how='outer')
print(users_data.head())

#users activity
users_days=events_data.groupby('user_id').day.nunique().to_frame().reset_index()
print(users_days.head())

userds_data=users_data.merge(users_days,on='user_id',how='outer')
print(users_data.head())

#проверка на потерю даных
print(events_data.user_id.nunique()==userds_data.user_id.nunique())

# успешно закончил курс (больше 181 баллов с
# учетом распределения количества passed результатов)
print(users_data.passed.quantile(0.93))
users_data['passed_corse']=users_data.passed> 170
print(users_data.head())

#соотношение пройденных с дропнувшимися
print(users_data.groupby('passed_corse').count())

