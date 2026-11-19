import numpy as np
import pandas as pd

np.random.seed(123)
production = np.random.normal(5, 1.2, 100)
df = pd.DataFrame({"Maize_Production": production})
print(df.describe())
