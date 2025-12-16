### Logic behind the Featured engineering done on the dataset

- Here, I am sharing the core reasoning and the logic behind the featured engineering done on the Train dataset, 
- To read more detailed about the data, please refer to the data folder and look for each individual subfolder, for which you want to find information about.


### ----------short summary for the dataset-----------

- This was a subset of the main dataset i.e. a test dataset, with 2671 rows and 10 individual columns (price column was not there since it is a test dataset)
- There was no missing value in the dataset

### -----------------Featured engineering logic---------------

1. Categorical Features : there were 2 kind of categorical features that I separated into 2 categories : Onehot encoding based and Label encoding based. 
- Onehot encoding based features : ['Airline', 'Additional_Info']
- Label encoding based features : ['Source', 'Destination', 'Total_Stops']

2. Numerical features : ['Date_of_Journey', 'Arrival_Time', 'Dep_Time', 'Duration']

3. Dropped columns : 'Route' column was not a useful column, since the dataset already had the 'Source', 'Destination' and 'Total_Stops' features, which provided more accurate and useful information, furthermore, below is a list of all other dropped columns with the reason to drop, that I dropped all at once at the end of the dataset, unlike I did in steps for the training dataset

dropped columns                    Reason
'Airline'                          Onehot encoded
'Addtional_Info'                   Onehot encoded
'Date_of_Journey'                  Splitted
'Date_of_Journey_year'             Contained only one value ('2019')
'Dep_Time'                         Splitted
'Arrival_Time'                     Splitted
'Duration'                         Splitted
'Duration_in_minutes'              'Duration_in_hours' provided the better information, it was more like a noise

### ----------------basic workflow for each column-------------

- for the each column, I followed almost the same blueprint to handle it, only with a few slight changes, which you can find as you follow the rest of the documentation in this folder.

- Blueprint : (unique values in the column --> value counts in the column --> encoding/mapping/splitting(depending on the type) --> check the value counts again (if necessary and very column specific) --> drop the old column (again column specific).

### ----------------Column : 'Airline'

- Type : Categorical(one hot based)

- steps involved : 
(unique value check --> value count --> reduced the categories to 4 --> check the value count again --> applied one hot(dropped the first) --> drop the column in the end)

- categories before mapping

Jet Airways                          897
IndiGo                               511
Air India                            440
Multiple carriers                    347
SpiceJet                             208
Vistara                              129
Air Asia                              86
GoAir                                 46
Multiple carriers Premium economy      3
Vistara Premium economy                2
Jet Airways Business                   2

- categories after mapping

Jet Airways    897
other          823
IndiGo         511
Air India      440

### --------------Column  : Additional_info

- Type : Categorical(one hot based)

- steps involved : 
(unique value check --> value count --> reduced the categories to 2 --> check the value count again --> applied one hot(dropped the first) --> drop the column in the end)

- categories before mapping

No info                         2148
In-flight meal not included      444
No check-in baggage included      76
1 Long layover                     1
Business class                     1
Change airports                    1

- categories after mapping

No info      2148
Some info     523


### --------------Column : Source

- Type : Categorical(label based)

- steps involved : 
(unique value check --> value count --> mapping --> applied label encoding --> kept the column as it is)

- mapping logic : 
{'Delhi': 0, 'Kolkata': 1, 'Banglore': 2, 'Mumbai': 3, 'Chennai': 4}

- value counts : 
Delhi       1145
Kolkata      710
Banglore     555
Mumbai       186
Chennai       75

### ---------------Column : Destination

- Type : Categorical(label based)

- steps involved : 
(unique value check --> value count --> Combined New Delhi and Delhi as the same value --> Value check again --> mapping --> applied label encoding --> kept the column as it is)

- mapping logic : 
{'Cochin': 0, 'Banglore': 1, 'Delhi': 2, 'Hyderabad': 3, 'Kolkata': 4}

- value counts v1 : 
Cochin       1145
Banglore      710
Delhi         317
New Delhi     238
Hyderabad     186
Kolkata        75

- value counts v2 : 
Cochin       1145
Banglore      710
Delhi         555
Hyderabad     186
Kolkata        75

### -----------Column : Total_Stops

- Type : Categorical(label based)

- steps involved : 
(unique value check --> value count --> mapping(same rank assigned to 2 stops, 3 stops and 4 stops to reduce the noise) --> applied label encoding --> value count agin --> kept the column as it is)

- mapping logic : 
{'non-stop': 0, '1 stop': 1, '2 stops': 2, '3 stops': 2, '4 stops': 2}

-value counts v1: 

1 stop      1431
non-stop     849
2 stops      379
3 stops       11
4 stops        1

-value counts v2 : 

1    1431
0     849
2     391

### -----------------Column : Date_of_Jounrey

- Type : Numerical

- steps involved : 
(unique value --> split --> check unique value for each individual new column, i.e day, month, year --> drop the date_of_journey and date_of_journey_year)

- split operator : 
split on the (/) operator and then make individual columns like day, month and year.


### Drop_cols_v2 applied


### ---------------Column : Dep_Time

- Type : Numerical

- steps involved : 
(unique value --> split --> drop the column)

- split operator : ':'


### Drop_cols_v3 applied


### ------------------Column : Arrival_time

- Type : Numerical

- steps involved : 
(unique value --> split --> drop the column)

- addtional : 
column Arrival_Time_minute had 2 different types of format ('25 10 Jun' and '15'), handled it separately

- split operator : ':'


### Drop_cols_v4 applied


### ------------------Column : Arrival_Time_minute

- Type : Numerical

- steps involved : 
(unique value --> split(keeping the first part of the string only))

- split operator : ' '(space bar)

### ------------------Column : Duration

- Type : Numerical

- steps involved : 
(unique value --> split --> Cols_drop_v5 --> unique_value_v2 --> substitute the anomly(5m))

- split operator : 'h'


### ---------------miscellaneous

- 1. After these steps, I checked the df.info() to make sure the processed dataset has every column in the int form : 
---  ------                     --------------  ----- 
0   Source                     2671 non-null   int64 
 1   Destination                2671 non-null   int64 
 2   Total_Stops                2671 non-null   int64 
 3   Airline_IndiGo             2671 non-null   int32 
 4   Airline_Jet Airways        2671 non-null   int32 
 5   Airline_other              2671 non-null   int32 
 6   Additional_Info_Some info  2671 non-null   int32 
 7   Date_of_Journey_day        2671 non-null   object
 8   Date_of_Journey_month      2671 non-null   object
 9   Dep_Time_hour              2671 non-null   object
 10  Dep_Time_minute            2671 non-null   object
 11  Arrival_Time_hour          2671 non-null   object
 12  Arrival_Time_minute        2671 non-null   object
 13  Duration_in_hours          2671 non-null   object

 - 2. After I saved the dataset (data -> intermidiate -> test.csv)
 - 3. for reference the path of this file is (notebooks -> FE&EDA -> basic -> test -> (then this folder))
 - 4. notebooks and data both are in the same hierarchy of the folders.


 *** Important : This is a test dataset, you won't find the 'price' column in it.