#%%
import pandas as pd
import numpy as np


#%%
dfs = [pd.read_csv(f'vestco/article_scrapping/{article}_vestco_articles.csv')[['brand', 'prix']] for article in ['jeans','baskets','veste','tshirt']]
# %%
dfs[0]['brand']

# %%
pd.Series(list(set(l))).to_clipboard()
# %%
