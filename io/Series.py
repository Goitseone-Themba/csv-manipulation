import pandas as pd

data = [1, 5, 4, 8]

twoD = pd.Series(data, index=["a", "b", "c", "d"])

print(twoD)