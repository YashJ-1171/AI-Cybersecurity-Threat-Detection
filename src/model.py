from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
import os

def train_and_evaluate(X_train, X_test, y_train, y_test):
    print("[INFO] Training Random Forest Threat Detection Model...")
    
    # Initialize and train
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Predict
    predictions = model.predict(X_test)
    
    # Evaluation Metrics
    accuracy = accuracy_score(y_test, predictions)
    print(f"\n[SUCCESS] Model Training Complete!")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions, target_names=['Normal', 'Attack']))
    
    # Save model
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/rf_model.pkl')
    
    return model, predictions