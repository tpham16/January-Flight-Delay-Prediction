# January-Flight-Delay-Prediction

A Python/PostgreSQL script that analyzes the historial data of airlines and calculates the delays of flights in January 2020. The data can be accessed from the following Kaggle page: https://www.kaggle.com/datasets/divyansh22/flight-delay-prediction?select=Jan_2020_ontime.csv 

In get_delays.py, I pulled the table from the Kaggle dataset and I saved the rows for flights that were not diverted nor cancelled into a pandas dataframe using PostgreSQL. I used 'Psycop2', a Python module called which is used for PostgresSQL, to load the data into the Python file for analysis. 

Using pandas, I created a new dataframe that groups of each unique airline and airports and caculate the ratio of the respective delays. 


