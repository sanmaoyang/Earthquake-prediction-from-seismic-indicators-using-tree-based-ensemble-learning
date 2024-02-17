import numpy as np
import pandas as pd
from sklearn.model_selection import PredefinedSplit, GridSearchCV,TimeSeriesSplit
from sklearn.metrics import f1_score, roc_auc_score, matthews_corrcoef
class ModelTuner:

    def __init__(self, model, train_data, validation_data, test_data ,scorefunction):
        self.model = model
        self.train_data = train_data
        self.validation_data = validation_data
        self.test_data = test_data
        self.best_parameters = None
        self.mcc_index = 1
        self.y_pred = None
        self.y_pro = None
        self.scorefunction = scorefunction

    def tune(self,fixed_params,param_grid):
        # Combine the train and validation data
        train = pd.concat([self.train_data, self.validation_data])

        # Create a predefined split
        pds = TimeSeriesSplit(test_size=len(self.validation_data),n_splits=2)

        # Set the fixed parameters in the model
        self.model.set_params(**fixed_params)

        # Create a grid search CV object
        clf = GridSearchCV(estimator=self.model, cv=pds, param_grid=param_grid,scoring=self.scorefunction)

        # Fit the model to the training data
        clf.fit(train.iloc[:,:-1], train.iloc[:,-1])

        # Get the best parameters
        self.best_parameters = clf.best_params_
        self.model.set_params(**self.best_parameters)
        self.model.set_params(**fixed_params)

        return self.best_parameters , self.model

    def mcc_index(self):
        self.model.fit(self.train_data.iloc[:,:-1], self.train_data.iloc[:,-1])
        # Predict the labels on the validation data
        y_pred = self.model.predict(self.validation_data.iloc[:,:-1])
        # Calculate the MCC
        mcc_value = matthews_corrcoef(self.validation_data.iloc[:,-1], y_pred)
        if mcc_value < 0:
            self.mcc_index = 0
    
    def getpredict(self):
        train = pd.concat([self.train_data, self.validation_data])
        self.model.fit(train.iloc[:,:-1], train.iloc[:,-1])
        self.y_pred = self.model.predict(self.test_data.iloc[:,:-1])
        self.y_pro = self.model.predict_proba(self.test_data.iloc[:,:-1])[:,1]

    def evaluate(self,mccmax = False):
        self.getpredict()
        # Calculate F1 score
        f1 = f1_score(self.test_data.iloc[:,-1], self.y_pred)
        # Calculate AUC
        auc = roc_auc_score(self.test_data.iloc[:,-1], self.y_pro)
        # Calculate MCC
        mcc = matthews_corrcoef(self.test_data.iloc[:,-1], self.y_pred)
        # Calculate recall
        # Create a DataFrame
        results = pd.DataFrame({
            "F1": [f1],
            "AUC": [auc],
            "MCC": [mcc],
        })
        return results 
