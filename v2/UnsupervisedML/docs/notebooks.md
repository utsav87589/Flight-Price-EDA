### ------------ Folder name : Notebooks --------------------

- here is all the information about the notebooks folder, the stuff inside and how basically they are operating.
- in this folder is basically the notebooks file that were used while the data was processed or during the phases of applying the unsupervised ml logic with the datasets.
- these notebooks files have the exact process alongside giving the hint, how the operations were being carried out combined with the files in the src folder.


##### File : process_data.ipynb
- in this file conatins the code, logic and implementation of how the data went from intermidiate to the model ready, obvisouly, you can refer to the exact file to find the more information about it, the comments are out there in the file, you can also refer to the flowchart for the project to get the hint, as it is not possible to put the exact line by line logic here, but still I am adding the flow of the file which explains the enough to know about the file.

- flow : 
- loading the functions --> then scaled train data (with setting up paths) --> performed initial checks --> separated the price coloumn --> dropped the price feature then from the original data --> then loaded the test data --> performed inital checks(only check nan in that case) --> then setup the paths to save them at different locations --> saved the data in the model ready under the scaled.

- the above workflow was exceuted the exact same way for the non scaled data (which is tree based data technically).