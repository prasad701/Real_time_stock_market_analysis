# Databricks Notebook 12: MLflow tracking template
import mlflow
from sklearn.ensemble import IsolationForest

mlflow.set_experiment("/Shared/stock-market-anomaly-detection")

with mlflow.start_run(run_name="isolation_forest_baseline"):
    contamination = 0.02
    n_estimators = 200

    mlflow.log_param("model", "IsolationForest")
    mlflow.log_param("contamination", contamination)
    mlflow.log_param("n_estimators", n_estimators)

    # Log metrics here after model evaluation:
    # mlflow.log_metric("precision", precision)
    # mlflow.log_metric("recall", recall)
    # mlflow.sklearn.log_model(model, "model")

print("MLflow tracking template ready.")
