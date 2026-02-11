import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import r2_score, roc_curve, mean_absolute_error, mean_squared_error, root_mean_squared_error


### function to print the metrices
def plot_metrices(y_test, y_pred) :

    print(f"r2 score : {r2_score(y_test, y_pred)}")
    print(f"MAE : {mean_absolute_error(y_test, y_pred)}")
    print(f"RMSE : {root_mean_squared_error(y_test, y_pred)}")
    print(f"MSE : {mean_squared_error(y_test, y_pred)}") 


### function to plot the results
def plot_graphs(y_test, y_pred) : 

    plt.figure(figsize = (8, 4))

    #----------line plot with respect to the scatter plot (best fit line)
    plt.subplot(1, 2, 1)
    plt.scatter(y_test, y_pred, color = 'blue', alpha = 0.5, label = 'Predicted')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
             color = 'red', linewidth = 2, label = 'Best fit line')
    plt.xlabel('Actual Values (y_test)')
    plt.ylabel('Predicted Values (y_pred)')
    plt.legend()
    plt.grid(True)

   #------------------- predicted vs true points
    plt.subplot(1, 2, 2)
    plt.plot(y_test, label='Actual', color='blue', marker='o')
    plt.plot(y_pred, label='Predicted', color='red', marker='x')
    plt.xlabel('Index')
    plt.ylabel('Target Value')
    plt.legend()
    plt.grid(True)
    plt.show()


### function to predict on the train/test data, save the model (training model part)
def pred_train_model(X_train, X_test, y_train, y_test, model, model_path, scaler_price_path = None) : 

    if scaler_price_path is not None : 

        scaler_price = joblib.load(scaler_price_path)

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        #------------inverse scaler
        y_test = scaler_price.inverse_transform(np.array(y_test).reshape(-1, 1))
        y_pred = scaler_price.inverse_transform(np.array(y_pred).reshape(-1, 1))

        #-------------saving the model
        joblib.dump(model, model_path)

        #---------plotting
        plot_metrices(y_pred, y_test)
        plot_graphs(y_test, y_pred)

    else : 
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        #-------------saving the model
        joblib.dump(model, model_path)

        #---------plotting
        plot_metrices(y_test, y_pred)
        plot_graphs(y_test, y_pred)


### function to predict on the valid for the best model from tree and distance based models
def best_model_predict(df, best_model_path, scaler_price_path = None) : 

    # -------------for the distance based models

    if scaler_price_path is not None : 

        scaler_price = joblib.load(scaler_price_path)
        model = joblib.load(best_model_path)

        y_pred_best_model = model.predict(df)
        y_pred_best_model = scaler_price.inverse_transform(np.array(y_pred_best_model).reshape(-1, 1))

        return y_pred_best_model
    
    else : 
        # ----------this part is exclusively for the tree

        model = joblib.load(best_model_path)

        y_pred_best_model = model.predict(df)

        return y_pred_best_model


### function to let the other models predict on the valid data and then compare the results with best model
def other_model_predict(df, y_pred_best_model, other_model_path, scaler_price_path = None) : 

    # -------------for the distance based models

    if scaler_price_path is not None : 

        scaler_price = joblib.load(scaler_price_path)
        model = joblib.load(other_model_path)

        y_pred_other_model = model.predict(df)
        y_pred_other_model = scaler_price.inverse_transform(np.array(y_pred_other_model).reshape(-1, 1))

        #---------plotting
        plot_metrices(y_pred_best_model, y_pred_other_model)
        plot_graphs(y_pred_best_model, y_pred_other_model)

    else : 
        
        # ----------this part is exclusively for the tree

        model = joblib.load(other_model_path)

        y_pred_other_model = model.predict(df)

        #---------plotting
        plot_metrices(y_pred_best_model, y_pred_other_model)
        plot_graphs(y_pred_best_model, y_pred_other_model)

