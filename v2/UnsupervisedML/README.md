# Flight-Price-EDA : Unsupervised ML
- Here is all about the unsupervised ml part for the Flight price EDA project. In the unsupervised ML part, I took the same data that I had for the tree and distance based models (i.e, scaled and non scaled data) and then proceeded with it.
- although some functions that are in the src file are exact same, but instead of importing from the supervised ml file, I prefered to make new ones for the unsupervsied ml files to avoid the confusion and the problematic part for the furture.


### ---------- brief summary : folder structure -------------
- Below is a brief discription about what each folder might contain inside, and what can you actually expect. for more detailed information, I have secific readme file for the each folder, within the folder named (docs)

1. Data : This folder contains all the data used for the unsupervised ML in both form (intermidiate)
2. docs : Has all the readme files
3. notebooks : contains all the notebook files (jupyter files)
4. reports : Reports done at the end of the project
5. src : has all the reusable code and functions that were called in the notebooks


### function common in both (supervised and unsupervised ml files) : 

- the common functions in the both of the files are : 

1. load_data(df_path) : load the data based on the path provided
- reason : (Do I have to explain this one lol haha), loading data is the first step of data science engineering.

2. get_nan(df) : used to get the nan values
- reason : used as a checkpoint at various stages of the data processing phase

3. get_shape(df) : used to get the shape of the dataset
- reason : used as a checkpoint at various stages of data  processing phase

4. def save_data(df, path) : save the dataset to the certain location
- reason : saving the data after preprocessing is important to begin working on it for the next stages

5. def drop_col(df, col) : drop the certain column(s) from the dataset
- reason : sometimes the column(s) important in the supervised ml are not much of a big deal in unsupervised ml (eg : price column)
