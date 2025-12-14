### About the folder and the structure

- In the scaler folder, we have the scaler objects that were saved after the scaler object was formed and then saved in this folder and again called for the inverse scaling while doing the prediction part.
- It's usage is only specific to the distance based models.
- It has only two different scaler objects : 
1. scaler_for_price : scaler object for the price column, because that was fitted for only one column and was called later on.
2. scaler_for_rest : scaler object for the rest of the numerical columns, it was first trained and done on the train data, then loaded again for the test data. never called afterwards.