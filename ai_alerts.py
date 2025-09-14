import pandas as pd

data = pd.read_csv('data/network_logs_analyzed.csv')

def generate_alerts(row):
    if row['anomaly'] == 'Anomalous':
        return f"⚠️ ALERT: Suspicious activity! Packet Size: {row['packet_size']}, Duration: {row['duration']:.2f}s, Protocol: {row['protocol']}"
    return None

data['alert'] = data.apply(generate_alerts, axis=1)
alerts = data.dropna(subset=['alert'])
alerts.to_csv('data/ai_alerts.csv', index=False)
print(f"{len(alerts)} alerts generated and saved to ai_alerts.csv")
