import pandas as pd
import numpy as np

ruru = pd.read_csv("ruru.csv")

ruru = ruru.drop_duplicates().dropna()
ruru = ruru.reset_index(drop=True)
ruru.to_csv("ruru_fix.csv",index=False)