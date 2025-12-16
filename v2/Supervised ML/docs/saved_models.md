### About the folder and the structure

- In this folder, we have the saved ML models in two different subfolders, each with different type of models, one contains the tree based models, while the another one has the distance based ml models.
- models were saved after the initial predictions and the later called while preidcting on the eval data, the whole idea was to use the same pr trained models rather than just training over and over again

=====> subfolder : distance
- contains the distance based models : Linear Regression (aka LR), Support vector regressor (aka SVR) and K nearest neighbour (aka KNN)


=====> subfolder : trees
- contains the tree based models : DTR (decisio tree regressor), abr (Adaboost regressor), gbr (Gradient boost regressor) and rfr (Random forest regressor).