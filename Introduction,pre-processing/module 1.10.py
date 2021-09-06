import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

events_data=pd.read_csv("../data/event_data_train.csv")
submissions_data=pd.read_csv("../data/submissions_data_train.csv")

print(events_data.head(10))
print(events_data.action.unique())
#добавление столбца с понятной датой
events_data['date']=pd.to_datetime(events_data.timestamp,unit='s')
print(events_data.head())

print(events_data.date.max())

#vizualization
#mark date as index df
events_data.index=events_data['date']
print(events_data)

vie=events_data[events_data['action']=='viewed']['action'].resample('M').count()
pas=events_data[events_data['action']=='passed']['action'].resample('M').count()
dis=events_data[events_data['action']=='discovered']['action'].resample('M').count()
star=events_data[events_data['action']=='started_attempt']['action'].resample('M').count()

for column in [vie,pas,dis,star]:
    column.plot(figsize=(8,6),legend=True)
    plt.legend(['viewed', 'passed', 'discovered', 'started_attempt'])
plt.show()

events_data['day']=events_data.date.dt.date
print(events_data)

#количество уникальных пользователей в день
events_data.groupby('day')\
    .user_id.nunique().plot()
plt.show()

#баллы пользовательй теряем пользовтелей которые не прошли не один контекст

print(events_data[events_data.action=='passed'].groupby('user_id',as_index=False)\
    .agg({'step_id' : 'count'})\
    .rename(columns={'step_id': 'passed_steps'}).passed_steps.hist())
plt.show()

print(events_data[events_data.action=='passed'].groupby('user_id',as_index=False)\
      .step_id.nunique().head())

#с учетом ошибки (ctrl+ / для быстрого снятия коментов)
print(events_data.pivot_table(index='user_id',columns='action',values='step_id',aggfunc='count',
                              fill_value=0).reset_index().head(10))







