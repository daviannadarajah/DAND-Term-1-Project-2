This file contains the resources used in the bikeshare.py file created by Davian Nadarajah (davian.nadarajah@hotmail.com) to analyse the Chicago, 
New York and Washington datasets for the Term 1 DAND US Bikeshare Data Project. 

1. 	Title: Find empty or NAN entry in Pandas Dataframe
	Purpose: Help understand the dataset by locating columns with missing or null values in a dataframe using np.where(pd.isnull(df)).
	Relevant functions: Not applicable. Used for exploration.
	URL: https://stackoverflow.com/questions/27159189/find-empty-or-nan-entry-in-pandas-dataframe

2.	Title: How to count the NaN values in a column in Pandas DataFrame 	
	Purpose: Help understand the dataset by counting the number of missing or null values in a dataframe column using .isnull().sum()
	Relevant functions: Not applicable. Used for exploration.
	URL: https://stackoverflow.com/questions/26266362/how-to-count-the-nan-values-in-a-column-in-pandas-dataframe
	
3. 	Title: Python for Data Analysis - Data Wrangling with Pandas, Numpy and IPython by Wes McKinney
	Purpose: Learning to use a Dataframe (p.128) and arange (p.139) to create an index for a pandas dataseries so I can ascribe an index number to a calendar month.
	Relevant functions: popular_month(df), popular_hour(df)
	Resource: pdf book

4. 	Title: numpy.arange
	Purpose: Explanation of the arguments associated with the numpy.arange. Connected with Resource 3.
	Relevant functions: popular_month(df), popular_hour(df) 
	URL: https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html

5. 	Title: pandas.Series.value_counts
	Purpose: Determine the default parameters for this function.
	Relevant Functions: popular_month(df), popular_day(df), popular_hour(df), trip_info(df), usertype_info(df), gender_info(df), birthyear_info(df)
	URL: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html
	
6. 	Title: pandas.DataFrame.max
	Purpose: Determine the default parameters for this function.
	Relevant Functions: popular_month(df), popular_day(df), popular_hour(df), trip_info(df), birthyear_info(df)
	URL: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.max.html

7. 	Title: Pandas Value_Counts Selection
	Purpose: Determine how to extract the maximum count after using the pandas.series.value_counts()
	Relevant Functions: popular_month(df), popular_day(df), popular_hour(df), trip_info(df), birthyear_info(df)
	URL: https://stackoverflow.com/questions/46702755/pandas-value-counts-selection
	
8. 	Title: Format a number to include commas
	Purpose: Need to format trip counts over 1000. Easier to read with the thousands comma separator.
	Relevant Functions: popular_month(df), popular_day(df), popular_hour(df), trip_info(df), usertype_info(df), gender_info(df), birthyear_info(df)
	URL: https://codereview.stackexchange.com/questions/63398/format-a-number-to-include-commas

9. 	Title: Convert Seconds to datetime timedelta
	Purpose: How to convert a duration expressed in seconds to days, hh:mm:ss
	Relevant Functions: trip_info(df)
	URL: https://stackoverflow.com/questions/25193464/convert-seconds-to-datetime-timedelta

10.	Title: How to convert seconds to hours, minutes and seconds?
	Purpose: How to convert a duration expressed in seconds to days, hh:mm:ss
	Relevant Functions: trip_info(df)
	URL: https://stackoverflow.com/questions/775049/how-to-convert-seconds-to-hours-minutes-and-seconds 	

11. 	Title: Python function to convert seconds into minutes, hours, and days
	Purpose: This covered typeerror problem I was having. Needed to ensure things are converted to integer when using datetime.timedelta.
	Relevant Functions: trip_info(df)
	URL: https://stackoverflow.com/questions/4048651/python-function-to-convert-seconds-into-minutes-hours-and-days

12. 	Title: Count frequency of values in pandas DataFrame column
	Purpose: Store the counts of each user type in a dictionary for easy reporting
	Relevant Functions: usertype_info(df), gender_info(df)
	URL: https://stackoverflow.com/questions/36004976/count-frequency-of-values-in-pandas-dataframe-column

13. 	Title: How to turn input number into a percentage in python
	Purpose: Learning to express and format decimal numbers as percentages
	Relevant Functions: usertype_info(df), gender_info(df)
	URL: https://stackoverflow.com/questions/28142688/how-to-turn-input-number-into-a-percentage-in-python

14. 	Title: How to check if a column exists in Pandas
	Purpose: Check if there is the Gender column in the data set as Washington dataset does not have this.
	Relevant Functions: gender_info(df), bithyear_info(df)
	URL: https://stackoverflow.com/questions/24870306/how-to-check-if-a-column-exists-in-pandas
	
15. 	Title: Pandas dataframe fillna() only some columns in place
	Purpose: Learn to replace NaN values with "unknown" in Gender column 
	Relevant Functions: usertype_info(df), gender_info(df)
	URL: https://stackoverflow.com/questions/38134012/pandas-dataframe-fillna-only-some-columns-in-place

16.	Title: pandas.DataFrame.drop
	Purpose: Learn to remove created columns in a dataframe so only raw data is shown.
	Relevant Functions: display_data(df)
	URL: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop.html
 



