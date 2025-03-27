import pandas as pd
import numpy as np
import time

n = 10000000
df = pd.DataFrame({
    "id": np.arange(n),
    "value": np.random.rand(n),
    "category": np.random.choice(["A", "B", "C", "D"], n)
})

def countTime(file_format, write_func):
    start_time = time.time()
    write_func()
    end_time = time.time()
    print(f"{file_format}: {end_time - start_time:.2f} сек")

countTime("CSV", lambda: df.to_csv("data.csv", index=False))

countTime("Parquet", lambda: df.to_parquet("data.parquet", index=False))

countTime("HDF5", lambda: df.to_hdf("data.h5", key="df", mode="w", format="table"))
