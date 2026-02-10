### Folder : SRC
- this folder contains all the resusuable functions in form of the python files, that were used in the jupyter notebook files. Further there are many subfolder inside of it, follow this file to find out more about those subfolders and individual purpose they serve.


### ----------- subfolder : basic ----------------

- this folder has only one python file : (load_check_data.py), this file conatins 

1. load_data(file_path) : this function is used to load the particular data file, given the path of that file
2. get_nan_duplicates_shape(df) : get the shape of the dataset, nan and dupliactes value inside the dataset
3. get_info(df) : check for the type of columns
4. drop_cols(df, col) : drop the given column from the data frame
5. save_data(df, path) : save the final data


### ---------- subfolder : featured_engineering -------------------
- one of the core folder in the entire project. it has many python files, each one with it's own uniwue purpose.


=====> file : handling_duplicates.py
- get_duplicates(df) : get the duplicates in the dataset
- drop_duplicates(df) : drop the duplicates from the dataset


=====> file : handling_nan.py
- get_nan_location(df, col) : get the location of the nan
- drop_nan_record(df, record_index) : drop the particular nan value at the certain index


=====> file : process_categoricals.py
- get_nunique_value_counts(df, cols) : gets the unique values inside the column(s)
- apply_one_hot(df, cols) : applies one hot encoding to the column(s)
- apply_label_encode(df, col, labels) : apply label encoding to the column, based on the labels given


=====> file : process_numericals.py
- get_format(df, col, patterns) : get the different record patterns in the column
- split_numericals(df, col, sep, new_cols) : split the numerical columns based on the given seperator and make the new columns
- check_value_counts_numericals(df, cols) : check the value counts (at feature engineering stage)
- drop_cols_numerical(df, col) : drop the columns(newly formed/ old numerical columns)
- change_dtype_numericals(df, cols, target_type) : change the data type for the columns(numericals in this case)


=====> file : scale_transform.py
- apply_transform_boxcox(df, cols) : apply the boxcox transformation to a column(s)
- drop_pre_post_transformation(df, cols) : drops the column(s) after apllying the transformation
- scale_train(df, cols_to_scale, scaler_path) : scale the train data only, save the scaler to the given path
- scale_valid(df, cols_to_scale, scaler_path) : scale the valid data by loading the trained scaler from the training data


=====> file : plot_features.py
- plot_graphs(df, cols) : plot the graphs (hist, qq and boxplot) for the numerical columns
- plot_graphs_post_scaling(df, df_copy, cols) : plot the boxplot for the numerical features(pre and post scaling for the comparison)


### ----------- subfolder : predictions ------------------------------


- this folder has all the files that were used once the preprocessing part was done. has the models and prediction part in it


=====> file : split_data.py

1. data_split(df, price = None) : split the data into the train/test data or eval data, depending on the input given.


=====> file : pred_plot_trees.py

1. metrices(y_test, y_pred) : has the different metrices that compare the predicted ones to the actual ones. (called implicitly, never explicitly)

2. plot(y_test, y_pred) : plot the scatter plot and best fit line to compare the predictions. (called implicitly, never explicitly)

3. plot_and_pred_train(X_train, X_test, y_train, y_test, model, model_path) : train the model and predict on the test data, then save the model to the given path. calls the metrices() and plot() functions to compare the results to the actual one

4. best_model_pred(X_eval, best_model_path) : after finding the best model with best results from plot_and_pred_train() function, it is given the best model to predict on the eval data and then it returns those predictions that are being saved later.

5. other_model_pred(X_eval, y_pred_best, other_model_path) : other model predicts on the eval data, then results are compared with the best model predictions on the eval data


=====> file : pred_plot_distance.py

- this file is very similar to the pred_plot_trees.py file, with same function name and same sequence with the only difference being with the scaler.
1. metrices(y_test, y_pred) : has the different metrices that compare the predicted ones to the actual ones. (called implicitly, never explicitly)

2. plot(y_test, y_pred) : plot the scatter plot and best fit line to compare the predictions. (called implicitly, never explicitly)

3. plot_and_pred_train(X_train, X_test, y_train, y_test, model, model_path, scaler) : train the model and predict on the test data, then save the model to the given path. calls the metrices() and plot() functions to compare the results to the actual one, but after training and predictions the price scaler object is called to inverse scale and then the metrices() and plot() functions are being called.

4. best_model_pred(X_eval, best_model_path, scaler) : after finding the best model with best results from plot_and_pred_train() function, it is given the best model to predict on the eval data and then using the same price scaler object, inverse transformation is being used then the predictions are returned.

5. other_model_pred(X_eval, y_pred_best, other_model_path, scaler) : other model predicts on the eval data, then inverse transformation applied, then the results are compared with the best model predictions on the eval data.