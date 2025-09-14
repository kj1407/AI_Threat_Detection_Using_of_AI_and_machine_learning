import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv('data/network_logs.csv')
features = ['packet_size', 'duration']
X = data[features]

model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
data['anomaly'] = model.fit_predict(X)
data['anomaly'] = data['anomaly'].apply(lambda x: 'Anomalous' if x == -1 else 'Normal')

data.to_csv('data/network_logs_analyzed.csv', index=False)
print("Threat detection completed. Results saved to network_logs_analyzed.csv")
