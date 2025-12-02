### Logic behind the Featured engineering done on the dataset

- Here, I am sharing the core reasoning and the logic behind the featured engineering done on the Train dataset, 
- To read more detailed about the data, please refer to the data folder and look for each individual subfolder, for which you want to find information about.


### ----------short summary for the dataset-----------

- The dataset is fairly big, around 10k rows and 11 individual columns
- There were only 2 missing nan values in the dataset, (1 in Route and 1 in Total stops column)
- target feature is 'Price' column


### -----------------Featured engineering logic---------------

1. Handling nan values : 
- Since there were only 2 nan values, I substitute the each one with the mode of the column to make it efficient

2. Categorical Features : there were 2 kind of categorical features that I separated into 2 categories : Onehot encoding based and Label encoding based. 
- Onehot encoding based features : ['Airline', 'Additional_Info']
- Label encoding based features : ['Source', 'Destination', 'Total_Stops']

3. Numerical features : ['Date_of_Journey', 'Arrival_Time', 'Dep_Time', 'Duration']

4. Dropped columns : 'Route' column was not a useful column, since the dataset already had the 'Source', 'Destination' and 'Total_Stops' features, which provided more accurate and useful information, furthermore, in this same folder in another radme file 'columns_drop.md', where I covered about the columns that I dropped at the certain stages of the featured engineering.


### ----------------basic workflow for each column-------------

- for the each column, I followed almost the same blueprint to handle it, only with a few slight changes, which you can find as you follow the rest of the documentation in this folder.

- Blueprint : (unique values in the column --> value counts in the column --> encoding/mapping/splitting(depending on the type) --> check the value counts again (if necessary and very column specific) --> drop the old column (again column specific).

### ----------------Column : 'Airline'

- Type : Categorical(one hot based)

- steps involved : 
(unique value check --> value count --> reduced the categories to 4 --> check the value count again --> applied one hot(dropped the first) --> drop the column in the end)

- categories before mapping

Jet Airways                          3849
IndiGo                               2053
Air India                            1752
Multiple carriers                    1196
SpiceJet                              818
Vistara                               479
Air Asia                              319
GoAir                                 194
Multiple carriers Premium economy      13
Jet Airways Business                    6
Vistara Premium economy                 3
Trujet                                  1

- categories after mapping

Jet Airways    3849
other          3029
IndiGo         2053
Air India      1752

### --------------Column  : Additional_info

- Type : Categorical(one hot based)

- steps involved : 
(unique value check --> value count --> reduced the categories to 2 --> check the value count again --> applied one hot(dropped the first) --> drop the column in the end)

- categories before mapping

No info                         8345
In-flight meal not included     1982
No check-in baggage included     320
1 Long layover                    19
Change airports                    7
Business class                     4
No Info                            3
1 Short layover                    1
Red-eye flight                     1
2 Long layover                     1

- categories after mapping

No info      8345
Some info    2338


### --------------Drop_cols_v1(applied)


### --------------Column : Source

- Type : Categorical(label based)

- steps involved : 
(unique value check --> value count --> mapping --> applied label encoding --> kept the column as it is)

- mapping logic : 
{'Delhi': 0, 'Kolkata': 1, 'Banglore': 2, 'Mumbai': 3, 'Chennai': 4}

- value counts : 
Delhi       4537
Kolkata     2871
Banglore    2197
Mumbai       697
Chennai      381

### ---------------Column : Destination

- Type : Categorical(label based)

- steps involved : 
(unique value check --> value count --> Combined New Delhi and Delhi as the same value --> Value check again --> mapping --> applied label encoding --> kept the column as it is)

- mapping logic : 
{'Cochin': 0, 'Banglore': 1, 'Delhi': 2, 'Hyderabad': 3, 'Kolkata': 4}

- value counts v1 : 
Cochin       4537
Banglore     2871
Delhi        1265
New Delhi     932
Hyderabad     697
Kolkata       381

- value counts v2 : 
Cochin       4537
Banglore     2871
Delhi        2197
Hyderabad     697
Kolkata       381

### -----------Column : Total_Stops

- Type : Categorical(label based)

- steps involved : 
(unique value check --> value count --> mapping(same rank assigned to 2 stops, 3 stops and 4 stops to reduce the noise) --> applied label encoding --> value count agin --> kept the column as it is)

- mapping logic : 
{'non-stop': 0, '1 stop': 1, '2 stops': 2, '3 stops': 2, '4 stops': 2}

-value counts v1: 
1 stop      5626
non-stop    3491
2 stops     1520
3 stops       45
4 stops        1

-value counts v2 : 
1    5626
0    3491
2    1566

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
 0   Source                     10683 non-null  int64 
 1   Destination                10683 non-null  int64 
 2   Total_Stops                10683 non-null  int64 
 3   Price                      10683 non-null  int64 
 4   Airline_IndiGo             10683 non-null  int32 
 5   Airline_Jet Airways        10683 non-null  int32 
 6   Airline_other              10683 non-null  int32 
 7   Additional_Info_Some info  10683 non-null  int32 
 8   Date_of_Journey_day        10683 non-null  object
 9   Date_of_Journey_month      10683 non-null  object
 10  Dep_Time_hour              10683 non-null  object
 11  Dep_Time_minute            10683 non-null  object
 12  Arrival_Time_hour          10683 non-null  object
 13  Arrival_Time_minute        10683 non-null  object
 14  Duration_in_hours          10683 non-null  object

 - 2. After I saved the dataset (data -> intermidiate -> train.csv)
 - 3. for reference the path of this file is (notebooks -> FE&EDA -> basic -> train -> (then this folder))
 - 4. notebooks and data both are in the same hierarchy of the folders.