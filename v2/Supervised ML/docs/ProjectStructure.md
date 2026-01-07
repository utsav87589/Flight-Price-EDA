### Project file and folder structure

- The project is split into various Folder and subfolder, each one with a different and unique purpose. Each folder has a readme inside it, providing the more details about it.


### ======= folder : Docs ==========

- This folder contains all the necessary documentation regarding the project, that include everything from README.md to feature_selection to all the way till reports. 
- Use it as a reference point to get know about the project from the scratch


### ============ Folder : data ===========

- The Data folder has 3 subfolders : intermidiate, raw and preprocessed, with each one having data from different stages in different form

### subfolders
- (raw) : contains raw data as excel file, Data_Train.xlsx (with price feature), Test_set.xlsx(without price feature). Data_Train is our main dataset, on which the whole logic of featured engineering of the project is based.

- (intermidiate) : contains data after featured engineering, but without transformations and scaling with same naming convention as in (raw)

- (preprocessed) : it has further 2 folders in it (distance, trees), for (distance) after the intermidiate step, transformations, outlier removal and scaling was applied, as those models are prone to outliers. Whereas, for the (trees) after the intermidiate step only, the check was done, no outlier was removed, no scaling or transformation was done on any column


### ============ Folder : notebooks ============

- Notebooks folder contains many subfolders, inside those subfolders are the jupyter notebooks with the code and logic behind the preprocessing of the data.

### subfolders
 - (basic) : this folder has the core preprocessing logic for the raw train and test data, for more information, please refer to the readme files inside that folder

 - (trees) : data from the intermidiate folder, which after checking for the plots and some final checks was model ready

 - (distance) : data from the intermidiate folder, after scalers and removing outliers was model ready for all distance based models.


 ### ================ Folder : Reports ==============

 - Contains the reports for the comparison after the final model testing in a pdf file.


 ### =============== Folder : src ===============

- has all the repetitive python code (in form of functions) that was used over and over again in the program, in the jupyter notebooks
- has a seperate radme file as well


### ================= Folder : scalers ==============

- scaler objects for distance based models
- one scaler only for 'price' column in the 'test' dataset 
- another scaler for the rest of the columns.

### ================= Folder : models ==============

- it has all the models saved in it, that were used for the testing like tree based and distance based models.
- the idea for this folder was that, if the model is trained once, it should be saved to avoid additional training each time the notebook(jupyter file is open), also to test the performance of the models on the test data.
- without saving the models, we train the model again and again while testing on new data. (models after saving serves as inference models)
