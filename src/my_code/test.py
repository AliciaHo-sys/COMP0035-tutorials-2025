from collections.abc import Iterable
import pandas as pd

def is_atomic(val):
    return not isinstance(val, Iterable) or isinstance(val, str)

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, [3, 4]],
    'B': ['x', {'y': 1}, 'z'],
    'C': [True, False, (1, 2)]
})

# Apply atomic check
atomic_mask = df.map(is_atomic)

# Identify rows with any non-atomic values
non_atomic_rows = ~atomic_mask.all(axis=1)

# Extract those rows
df_non_atomic = df[non_atomic_rows]
print(df_non_atomic)
