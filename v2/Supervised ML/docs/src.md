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
- split_data(df, target_feature) : split the data around the target feature (train-test split), only for the train data
- verify_split(X_train, X_test, y_train, y_test) : verify the split of the data, by checking out their shape


=====> file : pred_and_plot.py
- plot_metrices(y_test, y_pred) : find out the comparison metrices for the model performance during the training phase (always used internally, never called off externally in notebooks)

- plot_graphs(y_test, y_pred) : plot the graphs for the true vs test data during the model training phase (used internally inside the file, never called off exlicitly in the notebook files)

- pred_train_model(X_train, X_test, y_train, y_test, model, model_path, scaler_price_path = None) : train the models(tree and distance based) on the train data and then save those models for the inference part (predictions on the valid data), in this function we called 'plot_metrices()' and 'plot_graphs()' functions, if scaler path is provided then it's for the distance based models else for the trees

- best_model_predict(df, best_model_path, scaler_price_path = None) : after finding the best model (for distance and trees) we load that trained model and predict on the valid data as a benchmark (scaler logic is same as for the pred_train_model())

- other_model_predict(df, y_pred_best_model, other_model_path, scaler_price_path = None) : other pretrained and saved models predict on the valid data and then being compared with the best model (logic for scaler is same as 'pred_train_model' and 'best_model_predict')