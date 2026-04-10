import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import os

def plot_confusion_matrix(y_true, y_pred):
    print("[INFO] Generating visual reports...")
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8,6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Normal', 'Attack'], yticklabels=['Normal', 'Attack'])
    plt.title('Threat Detection Confusion Matrix')
    plt.ylabel('Actual Traffic')
    plt.xlabel('AI Predicted Traffic')
    
    os.makedirs('outputs', exist_ok=True)
    plt.savefig('outputs/confusion_matrix.png')
    plt.close()

def plot_feature_importance(model, feature_names):
    importances = model.feature_importances_
    plt.figure(figsize=(10,6))
    sns.barplot(x=importances, y=feature_names, palette='viridis')
    plt.title('Which Network Features Indicate an Attack?')
    plt.xlabel('Importance Score')
    plt.ylabel('Network Feature')
    plt.savefig('outputs/feature_importance.png')
    plt.close()
    print("[INFO] Visualizations saved in 'outputs/' folder.")