### Folder : SRC
- this folder contains all the resusuable functions in form of the python files, that were used in the jupyter notebook files. Further there are many subfolder inside of it, follow this file to find out more about those subfolders and individual purpose they serve.


### ----------- subfolder : data ----------------

- this folder has only one python file : (load_data.py), this file conatins 
1. load_data(file_path) : this function is used to load the particular data file, given the path of that file
2. get_shape(df) : get the shape of the dataset
3. get_nan(df) : get the null value count in the dataset
4. get_info(df) : check for the type of columns
5. save_data(df, path) : save the final data


### ---------- subfolder : featured_engineering -------------------
- one of the core folder in the entire project. it has many python files, each one with it's own uniwue purpose.


=====> file : processing_cols.py
1. unique_values(df, col) : gets the unique values present inside a particular column
2. value_counts(df, col) : gets the value count for each individual categories in a column
3. one_hot(df, col) : applies the one hot encoding to the categorical column
4. label_encoding(df, col, mapping) : applies the label encoding to the feature based on the mapping given
5. split_numerical(df, col) : splits the numerical column based on the operators(inside of the function is if-else condition)
6. split_numerical_further(df, col) : further splits the some numerical columns, that needs the more processing, even after first split
7. columns_to_drop(df, cols) : drop the columns


=====> file : plot_features.py
1. plot_graphs(df, feature) : plots hist, qq and box plot for the numerical features.
2. plot_graphs_post_scaling(df, df_copy, feature) : plots the box plots for the numerical feature of df and df_copy, after the sacler is applied on the main dataframe (df), (mainly for the distance based models)


=====> file : outliers.py
