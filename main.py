from src.data_generator import generate_network_data
from src.preprocess import preprocess_data
from src.model import train_and_evaluate
from src.visualize import plot_confusion_matrix, plot_feature_importance

def run_pipeline():
    print("=== AI Cybersecurity Threat Detection System ===")
    
    # Phase 1: Simulate Network Environment
    data_path = generate_network_data(num_samples=10000)
    
    # Phase 2: Preprocess Traffic
    X_train, X_test, y_train, y_test, feature_names = preprocess_data(data_path)
    
    # Phase 3: Train AI and Detect Threats
    model, predictions = train_and_evaluate(X_train, X_test, y_train, y_test)
    
    # Phase 4: Generate SOC Visualizations
    plot_confusion_matrix(y_test, predictions)
    plot_feature_importance(model, feature_names)
    
    print("\n[INFO] Pipeline execution finished successfully.")
    print("[INFO] Check the 'outputs' folder for threat graphs.")

if __name__ == "__main__":
    run_pipeline()