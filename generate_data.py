import pandas as pd
import numpy as np
import os

os.makedirs('data', exist_ok=True)

n = 500
np.random.seed(42)
data = pd.DataFrame({
    'packet_size': np.random.randint(40, 1500, n),
    'duration': np.random.uniform(0.01, 5.0, n),
    'protocol': np.random.choice(['TCP', 'UDP', 'ICMP'], n)
})

anomalies = np.random.choice(n, size=20, replace=False)
data.loc[anomalies, 'packet_size'] *= 5
data.loc[anomalies, 'duration'] *= 10

data.to_csv('data/network_logs.csv', index=False)
print("Synthetic network_logs.csv created with 500 records.")
