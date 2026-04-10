import pandas as pd
import numpy as np
import os

def generate_network_data(num_samples=5000):
    """Simulates realistic network traffic data for cybersecurity training."""
    np.random.seed(42)
    
    # Normal traffic patterns
    normal_data = {
        'duration': np.random.normal(5, 2, num_samples),
        'src_bytes': np.random.normal(200, 50, num_samples),
        'dst_bytes': np.random.normal(3000, 500, num_samples),
        'failed_logins': np.zeros(num_samples),
        'protocol': np.random.choice(['TCP', 'UDP', 'ICMP'], num_samples, p=[0.7, 0.2, 0.1]),
        'label': ['Normal'] * num_samples
    }
    
    # Attack traffic patterns (e.g., DoS, Brute Force)
    attack_samples = int(num_samples * 0.3) # 30% of traffic is malicious
    attack_data = {
        'duration': np.random.normal(100, 20, attack_samples), # Long connections
        'src_bytes': np.random.normal(5000, 1000, attack_samples), # High data upload
        'dst_bytes': np.random.normal(50, 10, attack_samples),
        'failed_logins': np.random.randint(5, 50, attack_samples), # Brute force
        'protocol': np.random.choice(['TCP', 'UDP', 'ICMP'], attack_samples, p=[0.5, 0.4, 0.1]),
        'label': ['Attack'] * attack_samples
    }
    
    # Combine and shuffle
    df_normal = pd.DataFrame(normal_data)
    df_attack = pd.DataFrame(attack_data)
    df = pd.concat([df_normal, df_attack]).sample(frac=1).reset_index(drop=True)
    
    # Save to data folder
    os.makedirs('data', exist_ok=True)
    file_path = 'data/network_traffic.csv'
    df.to_csv(file_path, index=False)
    print(f"[INFO] Simulated network dataset created at {file_path}")
    return file_path