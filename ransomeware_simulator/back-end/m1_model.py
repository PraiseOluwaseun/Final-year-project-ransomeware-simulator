import numpy as np
import shap
from lime.lime_tabular import LimeTabularExplainer
from sklearn.ensemble import RandomForestClassifier

class RansomwareML:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
        self._train_dummy_model()

    def _train_dummy_model(self):
        self.X = np.random.rand(200, 6)
        y = np.random.randint(0, 2, 200)
        self.model.fit(self.X, y)

    def predict(self, features):
        # Convert list to numpy array and reshape for prediction
        feat_array = np.array(features).reshape(1, -1)
        prediction = self.model.predict(feat_array)[0]
        return int(prediction)

    def explain_lime(self, features):
        explainer = LimeTabularExplainer(
            self.X,
            feature_names=["CPU", "Memory", "Disk", "Processes", "Network", "Flag"],
            class_names=["Benign", "Ransomware"],
            mode="classification"
        )
        # Convert list to numpy array
        feat_array = np.array(features)
        explanation = explainer.explain_instance(
            feat_array, 
            self.model.predict_proba
        )
        return explanation.as_list()

    def explain_shap(self, features):
        explainer = shap.TreeExplainer(self.model)
        # Convert list to numpy array
        feat_array = np.array(features).reshape(1, -1)
        shap_values = explainer.shap_values(feat_array)
        
        # Handle SHAP output format (differs by library version)
        if isinstance(shap_values, list):
            return shap_values[1][0].tolist()
        return shap_values[0].tolist()