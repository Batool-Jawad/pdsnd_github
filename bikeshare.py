import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        #getting the city name from the user
        city = input('Enter city name (chicago, new york city, washington): ').lower()
        #checking whether the user's input is a valid city name
        if city in CITY_DATA:
            break
        else:
            print('Incorrect city name')
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        #getting the month name from the user
        month = input('Enter month name (all, january, february, ... , june): ').lower()
        #checking whether the user's input is a valid month name
        if (month in months) or (month == 'all'):
            break
        else:
            print('Incorrect month name')
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        #creating a list of days of week
        day_of_week_list = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        #getting the day of week from the user
        day = input('Enter day of week (all, monday, tuesday, ... sunday): ').lower()
        #checking whether the user's input is a valid day of week
        if day in day_of_week_list:
            break
        else:
            print('Incorrect day of week')
            continue

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data file into data frame
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month,day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel.

       Args:
           (DataFrame) df - name of the dataframe to analyze
           (str) month - name of the month to filter by, or "all" to apply no month filter
           (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #if data is not filtred by a single month
    if month == 'all':
        #getting the common month using mode method
        common_month_num = df['month'].mode()[0]
        #getting the month name from the months list
        common_month_name = months[common_month_num-1].title()
        print('The most common month is: {}'.format(common_month_name))

    # TO DO: display the most common day of week
    #if data is not filtred by a single day of week
    if day == 'all':
        #getting the common day of week using mode method
        common_day_of_week = df['day_of_week'].mode()[0]
        print('The most common day of week is: {}'.format(common_day_of_week))

    # TO DO: display the most common start hour
    #adding new column to the date frame called hour which contains the number of hours in start time
    df['hour'] = df['Start Time'].dt.hour
    #getting the common hour using mode method
    common_hour = df['hour'].mode()[0]
    print('The most common hour is: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #getting the most commonly used start station using mode method
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}'.format(common_start_station))

    # TO DO: display most commonly used end station
    #getting the most commonly used end station using mode method
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: {}'.format(common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    #getting the most frequent combination of start station and end station trip
    common_start_end_combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most frequent combination of start station and end station trip is: {}'.format(common_start_end_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #calcuating the total travel time using numpy function sum
    total_travel_time = np.sum(df['Trip Duration'])
    print('Total travel time is: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    #calcuating the mean travel time using numpy function mean
    mean_travel_time = np.mean(df['Trip Duration'])
    print('Average travel time is: {}'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #counting the number of users in each type
    user_types_count = df['User Type'].value_counts()
    print('Counts of user types: \n{}\n'.format(user_types_count))

    # TO DO: Display counts of gender
    #for only chicage and new york city
    if 'Gender' in df:
        #counting the number of users in each gender
        gender_counts = df['Gender'].value_counts()
        print('Counts of gender: \n{}\n'.format(gender_counts))

    # TO DO: Display earliest, most recent, and most common year of birth
    #for only chicage and new york city
    if 'Birth Year' in df:
        #calcuating the earist birth year using numpy min function
        earliest_year = np.min(df['Birth Year'])
        #calcuating the most recent birth year using numpy max function
        most_recent_year = np.max(df['Birth Year'])
        #getting the most common birth year using mode method
        most_common_year = df['Birth Year'].mode()[0]
        print('Earilest year of birth is: {}'.format(earliest_year))
        print('Most recent year of birth is: {}'.format(most_recent_year))
        print('Most common year of birth is: {}'.format(most_common_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data based on the user's request."""
    #intilize row_counter with zero
    row_count = 0
    while True:
        #check whether the user wants to see the raw data
        display = input('Disply 5 rows of data ? Enter yes or no ')
        #if the user wants to see the data
        if display.lower() == 'yes':
            #increment row_count by 5
            row_count += 5
            #display raw data
            print(df.head(row_count))
        #if the user does not want to see raw data anymore, exit while loop
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
