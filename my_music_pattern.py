import pandas as pd
"""
convert the downloaded json file to csv
"""
with open('StreamingHistory0.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('my_musicpattern.csv', encoding='utf-8', index=False)