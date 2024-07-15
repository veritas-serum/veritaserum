import json
import pandas as pd
 
# json File has been downloaded from
# https://huggingface.co/datasets/felixludos/babel-briefings
# into ./downloaded_data
# TODO: Lazy-download this file directly inside the script
with open('./downloaded_data/babel-briefings-v1-fr.json') as f:
    data = json.load(f)
 
articles_df = pd.json_normalize(data)
articles_df = articles_df[['ID', 'url', 'title', 'description']]

articles_df = articles_df.sample(n=500, random_state=1)

articles_df.to_csv("./data_generated/french_evaluation_sample.csv")
