# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:19:40 2021

@author: kimje
"""
import requests
import pandas as pd
url = 'https://raw.githubusercontent.com/PlayingNumbers/ds_salary_proj/master/glassdoor_jobs.csv'
res = requests.get(url, allow_redirects=True)
with open('glassdoor_jobs.csv','wb') as file:
    file.write(res.content)
df = pd.read_csv('glassdoor_jobs.csv')



#salary parsing
#company name text only
#state field
#age of company
#parsing of job description (python, etc.)


df['hourly']= df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

df['employer_provided']= df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)



df= df[df['Salary Estimate'] != '-1']

salary= df['Salary Estimate'].apply(lambda x: x.split('(')[0])

minus_Kd= salary.apply(lambda x: x.replace('K', '').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))


df['min_salary']= min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary']= min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary']= (df.min_salary + df.max_salary)/2


#df['min_salary'].dtype

