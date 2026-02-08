### ------------ Folder name : Data --------------------

- here is all the information about the data folder, the way folder is structured and the stuff inside each one of them

- inside we have 3 subfolder, with each one having data from the different stages and for different purpose

1. raw
2. basic_processed
3. model_ready


### ************** subfolder : raw *********************

- here, we have 2 files : (Data_Train.xlsx) and (Test_set.xlsx). 

- (Data_Trasin.xlsx) has the raw data, but it also have the target feature ('Price'), later we called this data as (train.csv) in the (basic_processed) folder

- (Test_set.xlsx) doesn't have the target feature, but it was split already as it is while downloaded from the Kaggle, later it is called (valid.csv) in the (basic_processed) folder and the rest of the project also, we have similar naming reference.


### ************** subfolder : basic_processed *********************

- we have 2 files here : (train.csv) and (valid.csv), the both of the files are just identical to the files (Data_Train.xlsx) and (Test_set.xlsx) from the (raw) folder, respectively,

- after loading the data, the basic checks were performed, like checking (.head()) of the data frame, checking the info, nan and duplicates to make the strategy for the processing before making the data model ready. as the one final thing the extensions of the files were changed from (.xlsx) to (.csv)


### ************** subfolder : model_ready *********************

- it has 4 files inside, the files after processing from the (basic_processed) subfolders were later saved over there.

- (train_tree.csv) : has the target feature, non scaled data, used for model training purpose (for the tree based models)
- (train_distance.csv) : has the target feature, scaled data, used for model training purpose (for the distance based models)

- (valid_tree.csv) : does not have the target feature, non scaled data, used for validation purpose (for the tree based models)
- (valid_distance.csv) : does not have the target feature, non scaled data, used for validation purpose (for the distance based models)