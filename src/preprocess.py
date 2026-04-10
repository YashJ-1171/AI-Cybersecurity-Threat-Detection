import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import os

def preprocess_data(file_path):
    print("[INFO] Preprocessing data...")
    df = pd.read_csv(file_path)
    
    # Convert categorical text (Protocol, Label) to numbers
    le_proto = LabelEncoder()
    df['protocol'] = le_proto.fit_transform(df['protocol'])
    
    # Target variable (0 = Normal, 1 = Attack)
    df['label'] = df['label'].apply(lambda x: 1 if x == 'Attack' else 0)
    
    X = df.drop('label', axis=1)
    y = df['label']
    
    # Train/Test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Scale numerical features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Save scaler for future predictions
    os.makedirs('models', exist_ok=True)
    joblib.dump(scaler, 'models/scaler.pkl')
    
    return X_train_scaled, X_test_scaled, y_train, y_test, X.columns