from sklearn.metrics import f1_score, accuracy_score, recall_score, precision_score, confusion_matrix, roc_auc_score, roc_curve
import mlflow
import matplotlib.pyplot as plt
import seaborn as sns

def push_metrics(y_predicted, y_true):
  """
    Get metrics and track them to mlflow
  """
  f1 = f1_score(y_true,y_predicted)
  accuracy = accuracy_score(y_true,y_predicted)
  recall = recall_score(y_true,y_predicted)
  precision = precision_score(y_true,y_predicted)
  roc_auc = roc_auc_score(y_true, y_predicted)

  mlflow.log_metric("f1 score", f1)
  mlflow.log_metric("accuracy", accuracy)
  mlflow.log_metric("recall",recall)
  mlflow.log_metric("precision", precision)
  mlflow.log_metric("roc_auc", roc_auc)

  print("Metric tracking success")

def push_confusion_matrix(y_predicted, y_true, mlflow_run = True):
  """
    Save and track confusion matrix
  """
  matrix = confusion_matrix(y_true,y_predicted)

  class_labels = ['Negative','Positive']

  plt.figure(figsize = (8,6))
  sns.heatmap(
    matrix,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=class_labels,
    yticklabels=class_labels
  )

  plt.title('Matrix confusion heatmap')
  plt.xlabel('Predicted labels')
  plt.ylabel('True labels')

  plt.savefig('/content/confusion_matrix')

  print('confusion_matrix generated')

  if mlflow_run:
    mlflow.log_artifact('/content/confusion_matrix.png')
  else:
      plt.show()

def push_roc_curve(y_pred_proba, y_true, mlflow_run = True):
  """
    Save and track roc curve
  """
  roc_auc = roc_auc_score(y_true, y_pred_proba)
  fpr, tpr, thresholds = roc_curve(y_true, y_pred_proba)

  plt.figure(figsize=(8, 6))
  plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC-curve (area = {roc_auc:.4f})')
  plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--', label='Random based classification')
  plt.xlabel('False Positive Rate (FPR)')
  plt.ylabel('True Positive Rate (TPR)')
  plt.title('ROC-curve')
  plt.legend(loc='lower right')
  plt.grid(True)

  plt.savefig('/content/roc_curve')

  print("roc_curve generated")

  if mlflow_run:
    mlflow.log_artifact('/content/roc_curve.png')
  else:
    plt.show()
