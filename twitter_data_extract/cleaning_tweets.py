import pandas as pd
import re
df = pd.read_csv('tweetData.csv', encoding = 'unicode_escape')
df_copy = df
print(len(df_copy))
for i in range(len(df_copy)):
    txt = df_copy.loc[i]["full_text"]
    txt=re.sub(r'@[A-Z0-9a-z_:]+','',txt)#replace username-tags
    txt=re.sub(r'^[RT]+','',txt)#replace RT-tags
    txt = re.sub('https?://[A-Za-z0-9./]+','',txt)#replace URLs
    txt=re.sub("[^a-zA-Z]", " ",txt)#replace hashtags
    df_copy.at[i,"full_text"]=txt