import pandas as pd

raw_df = pd.read_csv('squirrel.csv')

df = \
    (raw_df
        .groupby('Primary Fur Color', as_index=False).agg(
            count = pd.NamedAgg(column='Unique Squirrel ID', aggfunc='count')
        )
        .to_csv('final.csv')
        
    )
