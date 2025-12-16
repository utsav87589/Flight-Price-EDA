#---------------predicting and then plotting

import joblib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, root_mean_squared_error, mean_absolute_error, mean_squared_error, roc_curve

#-------------metrices
def metrices(y_test, y_pred) : 
    print(f"r2 score : {r2_score(y_test, y_pred)}")
    print(f"MAE : {mean_absolute_error(y_test, y_pred)}")
    print(f"RMSE : {root_mean_squared_error(y_test, y_pred)}")
    print(f"MSE : {mean_squared_error(y_test, y_pred)}")

#----------function to plot
def plot(y_test, y_pred) : 
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.scatter(y_test, y_pred, color='blue', alpha=0.5, label='Predicted')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
             color='red', linewidth=2, label='Perfect Prediction Line')
    plt.xlabel('Actual Values (y_test)')
    plt.ylabel('Predicted Values (y_pred)')
    plt.legend()
    plt.grid(True)
   
    plt.subplot(1, 2, 2)
    plt.plot(y_test, label='Actual', color='blue', marker='o')
    plt.plot(y_pred, label='Predicted', color='red', marker='x')
    plt.xlabel('Index')
    plt.ylabel('Target Value')
    plt.legend()
    plt.grid(True)
    plt.show()

#---------------function to predict and plot on the trees
def plot_and_pred_train(X_train, X_test, y_train, y_test, model, model_path, scaler) : 

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        y_test = scaler.inverse_transform(np.array(y_test).reshape(-1, 1))
        y_pred = scaler.inverse_transform(np.array(y_pred).reshape(-1, 1))
        #-------------temporarily saving at other location
        joblib.dump(model, model_path)
        metrices(y_test, y_pred)
        plot(y_test, y_pred)


#----------------function to predict using the best model

def best_model_pred(X_eval, best_model_path, scaler) : 
     model = joblib.load(best_model_path)
     y_pred = model.predict(X_eval)

     y_pred = scaler.inverse_transform(np.array(y_pred).reshape(-1, 1))

     return y_pred

#---------------function to predict using the other models and then comparing it
def other_model_pred(X_eval, y_pred_best, other_model_path, scaler) : 
     
     model = joblib.load(other_model_path)
     y_pred_other = model.predict(X_eval)
     y_pred_other = scaler.inverse_transform(np.array(y_pred_other).reshape(-1, 1))

     metrices(y_pred_best, y_pred_other)
     plot(y_pred_best, y_pred_other)
