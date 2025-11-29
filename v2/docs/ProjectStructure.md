### Project file and folder structure

- The project is borken into various Folder and subfolder, each one serving a different and unique purpose.


### ======= folder : Docs ==========

- This folder contains all the necessary documentation regarding the project, that include everything from README.md to feature_selection to all the way till reports. 
- Use it as a reference point to get know about the project from the scratch


### ============ Folder : data ===========

- The Data folder has 3 subfolders : intermidiate, raw and preprocessed, with each one having data from different stages in different form

### subfolders
- (raw) : contians raw data as excel file, Data_Train. xlsx(with price feature), Test_set.xlsx(without price feature). Data_Train is our main dataset, on which the wholem logic of featured engineering of the project is based.

- (intermidiate) : conatins data after featured engineering, but without transformation and scaling with same naming convention as in (raw)

- (preprocessed) : it has further 2 folders in it (distance, trees), for (distance) after the intermidiate step, transformations, outlier removal and scaling was applied, as those models are prone to outliers. Whereas, for the (trees) after the intermidiate step only, the check was done, no outlier was removed, no scaling or transformation was done on any column


### ============ Folder : notebooks ============
