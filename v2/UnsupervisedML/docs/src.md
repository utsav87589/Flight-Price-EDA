### ------------ Folder name : src --------------------

- here is all the information about the src folder including the files and the operation each individual file/subfolder is responsible for, alongside the folder structure.

- src folder is the one containing the python code mostly in form of function that was later reused again and again in the notebook files, before completing the report part.

- this folder structure is bit more complex with many subfolders inside and functions inside of the files in those subfolders, but here I try to give the best explanantion I could give, to guide you through the folder.

- further this folder is divided into the 2* subfolders : 1. process_data, 2. unsupervised_ml
- (*)sign after the (2) in the above statment means that at the time of documentation we only have 2 folders, but for sure there are gonna be more as the project proceed ahead. to find out more you can always refer to the github to track those changes and what exactly was there.


##### Subfolder : process_data
- in this folder we have the src files that were being used to perform the basic processing actions of the data to convert it from intermidiate form to the model ready form, additionally it also has (__init__.py) file to export out those functions to be called in the notebooks.
- these functions from the src files were used in with the combination of notebook files (process_data.ipynb) only.
- in this particular subfolder we have only one (data.py) file with all functions inside it.

====> (file : data.py)
- this file has the following content : 
1. load_data(df_path) : loads the dataframe based on the path given to it
2. get_nan(df) : return the nan values in the dataset
3. get_info(df) : gives the info(the data type of the columns) of the dataset/dataframe
4. drop_col(df, col) : drop the column/columns from the dataset (along the vertical axis i.e. axis = 1)
5. save_data(df, path) : save the data to the particular location on the basis of the location(path) given to it
6. get_shape(df) : return the shape of the dataset



##### Subfolder : unsupervised_ml
