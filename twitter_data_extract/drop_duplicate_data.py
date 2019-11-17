import pandas as pd

df = pd.read_csv('tweetData.csv', encoding = 'unicode_escape')
df_copy = df
print(len(df_copy))
serlis=df_copy.duplicated().tolist()
print(serlis.count(True)) 
serlis=df_copy.duplicated(['full_text']).tolist()
print(serlis.count(True))
df_copy=df_copy.drop_duplicates(['full_text'])
df_copy=df_copy.reset_index(drop=True)
df_copy=df_copy.drop(['place','coordinates','geo','id_str'],axis=1)


