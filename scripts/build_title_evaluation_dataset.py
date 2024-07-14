import json
import pandas as pd
 
with open('./data/babel-briefings-v1-fr.json') as f:
    data = json.load(f)
 
df = pd.json_normalize(data)
df = df[['ID', 'url', 'title', 'description']]

df = df.sample(n=500, random_state=1)

df.to_csv("./data_generated/french_evaluation_sample.csv")
