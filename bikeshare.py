"""
This script was written by Davian Nadarajah (davian.nadarajah@hotmail.com) to analyse
the Chicago, New York and Washington datasets for the Term 1 DAND US Bikeshare Data Project.
Please see accompanying readme.txt file for resource references.
"""

## import all necessary packages and functions
import time
import pandas as pd
import numpy as np
import datetime

## Filenames
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(city_file, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(city_file)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

       # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare dataset.
    '''
    # Use a loop to determine if the city input is valid
    while True:
        input_city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                    'Would you like to see data for Chicago, New York, or Washington?\n')
        city = input_city.lower()
        if city not in ("chicago", "new york", "washington"):
            print(input_city + ' is not a valid city, please try again.')
        else:
            break

    # Allocate a filename based on valid city input
    if city == "chicago":
        city_file = CITY_DATA['chicago']
    elif city == "new york":
        city_file = CITY_DATA['new york city']
    elif city == "washington":
        city_file = CITY_DATA['washington']
    return city_file

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) time period to filter the city's bikeshare dataset
    '''
    # Use a loop to determine if the time period input is valid.
    while True:
        input_time_period = input('\nWould you like to filter the data by month, day, both or not at'
                        ' all? Type "none" for no time filter.\n')
        time_period = input_time_period.lower()
        if time_period not in ("month", "day", "both", "none"):
            print(input_time_period + ' is not a valid time period, please try again.')
        else:
            break
    return time_period

def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        (str) specified month to filter the city's bikeshare dataset
    '''
    # Use a loop to determine if the month specified is valid.
    while True:
        input_month = input('\nWhich month? January, February, March, April, May, or June?\n')
        month = input_month.lower()
        months = ["january", "february", "march", "april", "may", "june"]
        if month not in months:
            print(input_month + ' is not a valid month, please try again.')
        else:
            break
    return month.title()

def get_day():
    '''Asks the user for a day and returns the specified day to filter the city's bikeshare dataset.

    Args:
        none.
    Returns:
        (str) specified day to filter the city's bikeshare dataset
    '''
    # Use a loop to determine if the day specified is valid.
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    while True:
        input_day = input('\nWhich day? Please enter a day of the week (eg. Sunday).\n')
        day = input_day.lower()
        if day not in days_of_week:
            print(input_day + ' is not a valid day, please try again.')
        else:
            break
    return day.title()

def popular_month(df):
    '''Calculates and prints the most popular start month of travel and count of trips
    from the filtered dataset. Uses "Start Time" column.

    Args:
        df - filtered city dataset containing formatted (int) month numbers
    Returns:
        none.
    '''
    # The dataframe (df) has the month data returning as a number (eg. Jan = 1, Feb = 2).
    # This converts the number index into the relevant month.
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    months = pd.Series(months, index=np.arange(1,7,1))

    # Calculates the most frequently occurring start month and returns it as a number
    popular_month = df['month'].mode()[0]

    # Takes the month number and looks it up in the months pandas array so that
    # it returns the month name.
    popular_month = months[popular_month]

    # Determines how many times the most popular start month has occurred.
    # .value_counts() sorts the count by descending order by default for each
    # unique occurance and then .max() will return the maximum count. this
    # equates to the count of the mode.
    popular_month_trips = df['month'].value_counts().max()

    # print the above statistics and format the count using the thousands
    # comma separator using {:,}.
    print('Most common start month:                         {} (Trip count: {:,})'
         .format(popular_month, popular_month_trips)
         )
    return None

def popular_day(df):
    '''Calculates and prints the most popular start day of travel and count
    of trips from the filtered dataset. Uses "Start Time" column.

    Args:
        df - filtered city dataset containing formatted (str) day names
    Returns:
        none.
    '''
    # determines the most common/popular start day has occurred.
    popular_day = df['day_of_week'].mode()[0]

    # .value_counts() sorts the count by descending order by default for
    # each unique occurance. Then .max() will return the maximum count.
    # This equtes to the count of the mode.
    popular_day_trips = df['day_of_week'].value_counts().max()

    # print the above statistics and format the count using the thousands
    # comma separator using {:,}.
    print('Most common start day:                           {} (Trip count: {:,})'
         .format(popular_day, popular_day_trips)
         )

    return None

def popular_hour(df):
    '''Calculates and prints the most popular start hour of the day travelled
    and count of trips from the filtered dataset. Uses "Start Time" column.

    Args:
        df - filtered city dataset containing formatted time data, (int) as hour
        number
    Returns:
        none.
    '''

    # The dataset contains the hour of day as a number and refers to each
    # in 24 hour time (eg.23 = 11pm). The below creates a pandas array to convert
    # the integer times into AM / PM strings.
    hours = ['1 AM', '2 AM', '3 AM', '4 AM', '5 AM', '6 AM', '7 AM', '8 AM', '9 AM', '10 AM', '11 AM', '12 PM',
            '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM', '9 PM', '10 PM', '11 PM', '12 AM']
    hour_list = pd.Series(hours, index=np.arange(1,25,1))

    # determines the most common/popular start hour.
    popular_start_hour = df['start_hour'].mode()[0]

    # .value_counts() sorts the count by descending order by default
    # .max() will return the maximum count (ie. which equates to the mode).
    popular_start_hour = hour_list[popular_start_hour]
    popular_start_hour_trips = df['start_hour'].value_counts().max()

    # print the above statistics and format the count using the thousands
    # comma separator using {:,}.
    print('Most common start hour:                          {} (Trip count: {:,})'
         .format(popular_start_hour, popular_start_hour_trips)
         )
    return None

def trip_info(df):
    '''Calculates and prints the following from the filtered dataset:
    - Total trip duration and total count of trips (in days, HH: MM: SS)
    - Average trip duration (in HH:MM:SS)
    - Most popular start station and count
    - Most popular end station and count
    - Most popular combination of start and end stations and count

    Args:
        df - filtered city dataset containing formatted time data (duration
        in seconds).
    Returns:
        none.
    '''
    # Display total travel time in seconds
    total_duration = df['Trip Duration'].sum()

    #need to convert to int(seconds) to avoid typeerror when using datetime.timedelta.
    #This will make it "days, HH:MM:SS.
    total_duration = datetime.timedelta(seconds=int(total_duration))

    # Display mean travel times and convert to HH:MM:SS
    trip_avg = df['Trip Duration'].mean()
    trip_avg = datetime.timedelta(seconds=int(trip_avg))

    # Total number of trips
    total_trips = len(df['Trip Duration'])

    # Calcualte most common/popular start station
    pop_start_station = df['Start Station'].mode()[0]

    # Calculate the count of trips for the most popular station
    count_pop_start_station = df['Start Station'].value_counts().max()

    # Most common/popular end station and count
    pop_end_station = df['End Station'].mode()[0]
    count_pop_end_station = df['End Station'].value_counts().max()

    # Most common/popular trip combination and count. Need to first
    # concatenate start and end station columns.
    df['Combined'] = df['Start Station'] + ' to ' + df['End Station']
    pop_trip = df['Combined'].mode()[0]
    count_pop_trip = df['Combined'].value_counts().max()

    # print the above statistics and format the count using the thousands
    # comma separator using {:,}.
    print('Total trip duration (days, HH:MM:SS):            {} (Total trip count: {:,})\n'
        'Average trip duration (HH:MM:SS):                {}\n'
        'Most common start station:                       {} (Trip count: {:,})\n'
        'Most common end station:                         {} (Trip count: {:,})\n'
        'Most common trip from start to end:              {} (Trip count: {:,})'
     .format(
          total_duration, total_trips, trip_avg,
          pop_start_station, count_pop_start_station,
          pop_end_station, count_pop_end_station,
          pop_trip, count_pop_trip
          )
     )
    return None

def usertype_info(df):
    '''Calculates and prints the following from the filtered dataset:
    - Number of "Customer" type users and percentage against total users.
    - Number of "Dependent" type users and percentage against total users.
    - Number of "Subscriber" type users and percentage against total users.
    - Number of "Unknown/Unspecified" type users and percentage against total users.
    All data is sourced from the "User Type" column.

    Args:
        df - filtered city dataset containing User Type data.

    Returns:
        none.
    '''
    # There are null values in the Yser Type column so need to replace the NaN
    # entries with "Unknown".
    df['User Type'] = df['User Type'].fillna(value = 'Unknown')

    # Get total types and counts of each user_type and store in a dictionary
    total_users = df['User Type'].value_counts().to_dict()

    # Store counts against a variable for each valid column.
    unique_values = df['User Type'].unique()

    # Set zero as default value in case not in dictionary.
    total_customers, total_subscribers, total_unknown = 0, 0, 0

    # Take on the counts in the dictionary if they exist.
    if 'Customer' in unique_values:
        total_customers = total_users['Customer']

    if 'Subscriber' in unique_values:
        total_subscribers = total_users['Subscriber']

    if 'Unknown' in unique_values:
        total_unknown = total_users['Unknown']

    # Note that not all datasets have the "Dependent" user type. So need to
    # check this specifically with an if statement otherwise will get errors.
    if 'Dependent' in unique_values:
        total_dependents = total_users['Dependent']
    else:
        total_dependents = 0

    # Calculate the percantages of each type against the total
    total_usertypes = total_customers + total_subscribers + total_dependents + total_unknown
    perc_customers = total_customers / total_usertypes
    perc_subscribers = total_subscribers / total_usertypes
    perc_dependents = total_dependents / total_usertypes
    perc_unknown = total_unknown / total_usertypes

    # This should equal to 100%. If not, then there is data that needs
    # to be added.
    perc_total = perc_customers + perc_subscribers + perc_dependents + perc_unknown

    # print the above statistics and format the count using the thousands
    # comma separator using {:,}. Also format the percentages.
    print('Number of "Customer" type users:                 {:,} ({:%} of total recorded users)\n'
          'Number of "Subscriber" type users:               {:,} ({:%} of total recorded users)\n'
          'Number of "Dependent" type users:                {:,} ({:%} of total recorded users)\n'
          'Number of "Unknown" type users:                  {:,} ({:%} of total recorded users)\n'
          'Total number of all user types:                  {:,} ({:%} of total recorded users)'
         .format(
              total_customers, perc_customers, total_subscribers, perc_subscribers,
              total_dependents, perc_dependents, total_unknown, perc_unknown,
              total_usertypes, perc_total
              )
         )
    return None

def gender_info(df):
    '''Calculates and prints the following from the filtered dataset:
    - Number of Male users and percentage against total users
    - Number of Female users and percentage against against total users
    - Number of Unknown gender users and percentage against total users
    - Total number of all gender types and percentage against total users
    All data is sourced from the "Gender" column.

    Args:
        df - filtered city dataset containing Gender data.

    Returns:
        none.
    '''

    # The Washington dataset does not have the Gender column. So need to check
    # this first before doing any calculations.
    if 'Gender' not in df.columns:
        print('No gender information is available in this dataset.')
    else:
        # There are null values in the Gender column so need to replace the NaN
        # entries with "Unknown".
        df['Gender'] = df['Gender'].fillna(value = 'Unknown')

        # Store counts for each type in a dictionary for easy reporting
        total_genders = df['Gender'].value_counts().to_dict()

        # Store counts against a variable for each valid column.
        unique_values = df['Gender'].unique()

        # Set zero as default value in case not in dictionary.
        total_males, total_females, total_unknown = 0, 0, 0

        # Take on the counts in the dictionary if they exist.
        if 'Male' in unique_values:
            total_males = total_genders['Male']

        if 'Female' in unique_values:
            total_females = total_genders['Female']

        if 'Unknown' in unique_values:
            total_unknown = total_genders['Unknown']

        # Calculate the percantages of each type against the total
        total_genders = total_males + total_females + total_unknown
        perc_males = total_males / total_genders
        perc_females = total_females / total_genders
        perc_unknown = total_unknown / total_genders

        # This should equal to 100%. If not, then there is data that needs
        # to be added.
        perc_total = perc_males + perc_females + perc_unknown

        # print the above statistics and format the count using the thousands
        # comma separator using {:,}. Also format the percentages.
        print('\nNumber of Male users:                            {:,} ({:%} of total recorded users)\n'
              'Number of Female users:                          {:,} ({:%} of total recorded users)\n'
              'Number of Unknown gender users:                  {:,} ({:%} of total recorded users)\n'
              'Total number of all gender types:                {:,} ({:%} of total recorded users)'
              .format(
                  total_males, perc_males,
                  total_females, perc_females,
                  total_unknown, perc_unknown,
                  total_genders, perc_total
                  )
             )
        return None

def birthyear_info(df):
    '''Calculates and prints the following from the filtered dataset:
    - Youngest user based on birth year
    - Oldest user based on birth year
    - User with the most common birth year and count
    All data is sourced from the "Birth Year" column.

    Args:
        df - filtered city dataset containing Birth Year data.

    Returns:
        none.
    '''
    # The Washington dataset does not have the Bith Year column. So need
    # to check this first before doing any calculations.

    if 'Birth Year' not in df.columns:
        print('No birth year information is available in this dataset.')
    else:
        # Note that there are null values in Birth Year but its
        # consideration is not required for the below calculations

        #youngest user
        max_birthyear = int(df['Birth Year'].max())

        #oldest user
        min_birthyear = int(df['Birth Year'].min())

        #most common user
        frequent_birthyear = int(df['Birth Year'].mode()[0])
        count_frequent_birthyear = df['Birth Year'].value_counts().max()

        # print the above statistics and format the count using the thousands
        # comma separator using {:,}.
        print('\nYoungest user was born in:                       {}\n'
              'Oldest user was born in:                         {}\n'
              'Most frequent user was born in:                  {} (Total count: {:,})'
             .format(
                  max_birthyear, min_birthyear, frequent_birthyear, count_frequent_birthyear
                  )
             )

    return None

def display_data(df):
    '''Provides the user the option of viewing five lines of data, repeating this upon request
       until the user responds with 'no'.
    Args:
        csv city data file.
    Returns:
        none.
    '''
    # remove the columns I created so that only raw data appears
    df = df.drop(['month','day_of_week', 'start_hour', 'Combined'], axis=1)

    i = 0

    # ask user to see 5 lines of data
    show_data = input("\nWould you like to see five lines of code? Type 'yes' to view.\n")

    # this will keep asking the user to see the next five lines of code until
    # they do not respond with 'yes'
    while show_data.lower() == 'yes':
        print(df.iloc[i:i + 5])
        i += 5
        show_data = input(
                    "\nWould you like to see five more lines of data? Type \'yes\' to view.\n"
                    )

def main():
    '''Calculates and prints out the descriptive statistics based on the city and
    time period specified by the user. Also includes runtime information.

    Args:
        none.
    Returns:
        none.
    '''

    while True:
        # Determine which city file (ie. the .csv dataset) should be analysed.
        city_file = get_city()

        # Get the time period (day, month or all), from the user
        time_period = get_time_period()

        # Analyse city data with just a month filter (ie. no day filter)
        if time_period == 'month':
            month = get_month()
            day = 'all'

            # This creates the dataframe based on the user input city and time parameters
            df = load_data(city_file, month, day)

            # Compiling the report and adding run time information
            print('\nPARAMETERS:  CITY DATA = ' + city_file + ', MONTH = ' + month + ' , DAY = ' + day)
            start_time = time.time()
            print('\n----- Popular times of travel -----')
            popular_day(df)
            popular_hour(df)
            runtime_pop_travel = time.time() - start_time

            start_time = time.time()
            print('\n----- Popular stations and trip duration -----')
            trip_info(df)
            runtime_stations_duration = time.time() - start_time

            start_time = time.time()
            print('\n----- User Info -----')
            usertype_info(df)
            gender_info(df)
            birthyear_info(df)
            runtime_userinfo = time.time() - start_time

            print('\n----- Runtime Info -----')
            print('The Popular times of travel statistics took ' + str(runtime_pop_travel)
             + ' seconds to run.')
            print('The Popular statiosn and trip duration statistics took ' + str(runtime_stations_duration)
             + ' seconds to run.')
            print('The User info statistics took ' + str(runtime_userinfo) + ' seconds to run.' )
            print('-'*100)

            # Ask the user if they want to see 5 lines of code, repeating the request until they say no.
            display_data(df)

        # Analyse city data with just a day filter (ie. no month filter)
        elif time_period == 'day':
            month = 'all'
            day = get_day()

            # This creates the dataframe based on the user input city and
            # time parameters
            df = load_data(city_file, month, day)

            # Compiling the report and adding run time information
            print('\nPARAMETERS:  CITY DATA = ' + city_file + ', MONTH = ' + month + ' , DAY = ' + day)
            start_time = time.time()
            print('\n----- Popular times of travel -----')
            popular_month(df)
            popular_hour(df)
            runtime_pop_travel = time.time() - start_time

            start_time = time.time()
            print('\n----- Popular stations and trip duration -----')
            trip_info(df)
            runtime_stations_duration = time.time() - start_time

            start_time = time.time()
            print('\n----- User info -----')
            usertype_info(df)
            gender_info(df)
            birthyear_info(df)
            runtime_userinfo = time.time() - start_time

            print('\n----- Runtime Info -----')
            print('The Popular times of travel statistics took ' + str(runtime_pop_travel)
            + ' seconds to run.')
            print('The Popular statiosn and trip duration statistics took ' + str(runtime_stations_duration)
             + ' seconds to run.')
            print('The User info statistics took ' + str(runtime_userinfo) + ' seconds to run.' )
            print('-'*100)

            # Ask the user if they want to see 5 lines of code, repeating the request until they say no.
            display_data(df)


        # Analyse city data with month and day filters applied
        elif time_period == 'both':
            month = get_month()
            day = get_day()

            # This creates the dataframe based on the user input city and
            # time parameters
            df = load_data(city_file, month, day)

            # Compiling the report and adding run time information
            print('\nPARAMETERS:  CITY DATA = ' + city_file + ', MONTH = ' + month + ' , DAY = ' + day)
            start_time = time.time()
            print('\n----- Popular times of travel -----')
            popular_hour(df)
            runtime_pop_travel = time.time() - start_time

            start_time = time.time()
            print('\n----- Popular stations and trip duration -----')
            trip_info(df)
            runtime_stations_duration = time.time() - start_time

            start_time = time.time()
            print('\n----- User info -----')
            usertype_info(df)
            gender_info(df)
            birthyear_info(df)
            runtime_userinfo = time.time() - start_time

            print('\n----- Runtime Info -----')
            print('The Popular times of travel statistics took ' + str(runtime_pop_travel)
            + ' seconds to run.')
            print('The Popular statiosn and trip duration statistics took ' + str(runtime_stations_duration)
            + ' seconds to run.')
            print('The User info statistics took ' + str(runtime_userinfo) + ' seconds to run.' )
            print('-'*100)

            # Ask the user if they want to see 5 lines of code, repeating the request until they say no.
            display_data(df)

        else:
            # Analyse city data with no time filters
            time_period = 'none'
            month = 'all'
            day = 'all'

            # This creates the dataframe based on the user input city and
            # time parameters
            df = load_data(city_file, month, day)

            # Compiling the report and adding run time information
            print('\nPARAMETERS:  CITY DATA = ' + city_file + ', MONTH = ' + month + ' , DAY = ' + day)
            start_time = time.time()
            print('\n----- Popular times of travel -----')
            popular_month(df)
            popular_day(df)
            popular_hour(df)
            runtime_pop_travel = time.time() - start_time

            start_time = time.time()
            print('\n----- Popular stations and trip -----')
            trip_info(df)
            runtime_stations_duration = time.time() - start_time

            start_time = time.time()
            print('\n----- User info -----')
            usertype_info(df)
            gender_info(df)
            birthyear_info(df)
            runtime_userinfo = time.time() - start_time

            print('\n----- Runtime Info -----')
            print('The Popular times of travel statistics took ' + str(runtime_pop_travel) +
            ' seconds to run.')
            print('The Popular statiosn and trip duration statistics took ' +
            str(runtime_stations_duration) + ' seconds to run.')
            print('The User info statistics took ' + str(runtime_userinfo) + ' seconds to run.' )
            print('-'*100)

            # Ask the user if they want to see 5 lines of code, repeating the request until they say no.
            display_data(df)

        #Ask if the user wants to continue with another data query
        restart = input('\nWould you like to restart? Type \'yes\' to proceed.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
