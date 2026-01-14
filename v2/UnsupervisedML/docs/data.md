### ------------ Folder name : Data --------------------

- here is all the information about the data folder, the way folder is structured and the stuff inside each one of them
- Inside the folder we have two subfolders, each one contaning different set of files for different purposes
- 2 subfolders : 1. Intermidiate, 2. model ready
- further the subfolders have more folders inside, at first glance it might look very confusing, but once you get through this readme file, everything will make sense.



##### Subfolder  : intermidiate
- in the intermidiate folder basically, we have the data that we had for the trees and distance based models, during the supervised ML but stored at two different places in 2 different subfolders. ignore the naming convention please, this is like the most suited name I could find.

1. non-scaled : the data which was non-scaled i.e, the data for the tree based models after all the preprocessing was done.
2. scaled : the data which was scaled using the scaler object. i.e, the data for the distance based models after preprocessing



##### Subfolder : model_ready
- this folder has the model ready data, which technically is nothing but the 'price' column being splitted and then the 2 parts which were separated (one with 'price' only and one 'without price' and has the 'rest'), alongside the 'test' saved as it is in 2 different subfolders, scaled and non-scaled. 
- in the test data, we never had the 'price' column and for the unsupervised ml, we had to split the 'price' column, because we never use it in the unsupervised ml.

1. non-scaled : has test_non_scaled, price_non_scaled and X_non_scaled
2. scaled : it contains, test_scaled, price_scaled and X_scaled

- the purpose of having the 'price', 'test' and 'non scaled data' is entirely for the research and curiosity to see how models will treat them in contrast to unsupervised ml, where our aim in always to find the patterns not the predictions or anything similar.