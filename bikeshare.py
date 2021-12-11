import time
import datetime
import pandas as pd
import numpy as np
from PIL import Image
import requests

#this line lets us see every column in the DataFrame
pd.set_option('display.width', 120)
pd.set_option('display.max_columns', 1000)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#list of cities
cities = ["chicago", "new york city", "washington"]
#list of months
months = ["january","february","march","april","may","june"]
#list of days
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')


    # while loop to get the city name
    while True:
        city = input("Enter the name of the city! choose either chicago, new york city, or washington:\n")
        # making the city name lowercase so we can verify the names without errors
        city = city.lower()
        if city in cities:
            break
        else:
            print("Wrong input, try chicago, new york city, or washington.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter a month to filter by (select months from january to june), or type 'all' if you do not want to filter by month: \n")
        # making the month name lowercase so we can verify the names without errors
        month = month.lower()
        if month in months or month == "all":
            break
        else:
            print("Wrong input, only type months from january to june.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter a day to filter by, or type 'all' if you do not want to filter by day: \n")
        # making the day name lowercase so we can verify the names without errors
        day = day.lower()
        if day in days or day == "all":
            break
        else:
            print("Wrong input, try again!")


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df,city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    city1 = city
    month1 = month
    day1 = day
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    month_count = (df['month'] == popular_month).sum()
    popular_month = months[popular_month-1].title()
    print("The most common month is: {}, count: {}".format(popular_month,month_count))


    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    day_count = (df['day_of_week'] == popular_day).sum()
    print("The most common day is: {}, count: {}".format(popular_day, day_count))


    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    hour_count = (df['hour'] == popular_hour).sum()
    print("The most common hour is: {}, count: {}".format(popular_hour,hour_count))
    print("used filters:\ncity: {}, month filter: {}, day filter: {}".format(city1, month1, day1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df,city, month, day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    # find the most popular start station
    popular_start_station = df['Start Station'].mode()[0]
    start_station_count = (df['Start Station'] == popular_start_station).sum()
    print("The most common start station is: {}, count{}".format(popular_start_station,start_station_count))


    # TO DO: display most commonly used end station
    # find the most popular end station
    popular_end_station = df['End Station'].mode()[0]
    end_station_count = (df['End Station'] == popular_end_station).sum()
    print("The most common end station is: {}, count{}".format(popular_end_station,end_station_count))


    # TO DO: display most frequent combination of start station and end station trip
    #create a column in the dataframe for the most popular travel route
    df['Travel Route'] = df['Start Station'] + " ------> " + df['End Station']
    # find the most popular travel route
    popular_travel_route = df['Travel Route'].mode()[0]
    route_count = (df['Travel Route'] == popular_travel_route).sum()
    print("The most common travel route is:\n{}, count{}".format(popular_travel_route,route_count))
    print("used filters:\ncity:{}, month filter: {}, day filter: {}".format(city, month, day))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df,city, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = str(datetime.timedelta(seconds=int(total_travel_time)))
    print("The total trip duration is:\n{} hours".format(total_travel_time))



    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    average_travel_time = str(datetime.timedelta(seconds=average_travel_time))
    print("The average trip duration is:\n{} hours".format(average_travel_time))
    print("used filters:\ncity:{}, month filter: {}, day filter: {}".format(city, month, day))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # get value counts for each user type
    user_types = df['User Type'].value_counts()
    #print the total number of subscribers and customers
    print('Number of different user types:\n{}'.format(user_types))


    # TO DO: Display counts of gender
    #find the gender count excluding NaN values
    if 'Gender' in df.columns:
        gender_count = df['Gender'].dropna(axis = 0).value_counts()

        #print the total male and female numbers
        print('Number of male and female subscribers:\n{}'.format(gender_count))

    else:
        print("Users gender cannot be displayed")

    # TO DO: Display earliest, most recent, and most common year of birth
    #find the earliest year of birth
    if 'Birth Year' in df.columns:
        oldest_user = df['Birth Year'].dropna(axis = 0).min()
        #print the earliest year of birth
        print('The earliest year of birth is: {}'.format(int(oldest_user)))


        #find the most recent year of birth
        youngest_user = df['Birth Year'].dropna(axis = 0).max()
        #print the most recent year of birth
        print('The most recent year of birth is: {}'.format(int(youngest_user)))


        #find the most common year of birth
        common_birth_year = df['Birth Year'].dropna(axis = 0).mode()[0]
        year_count = (df['Birth Year'] == common_birth_year).sum()
        #print the most common year of birth
        print('The most common year of birth is: {}, count: {}'.format(int(common_birth_year),year_count))
    else:
        print("Birth year data cannot be displayed")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def raw_data(df,city):
    """ Asks the user if he/she wants to view raw data and displays 5 rows
    of data accordingly
    args: DataFrame"""
    df = df.fillna("N/A")
    #counter to increase the index of the first row of data every time the user asks for more data
    j = 0
    row_count = len(df.index)
    #asking the user if he/she wants to view raw data
    answer = input("Do you want to view raw data?(Enter 'yes' to see the data or otherwise to skip this part )\n").lower()
    #checking the answer
    if answer.lower() == "yes":
        #while loop to keep displaying 5 rows of data
        while answer.lower() == "yes":
            #for loop to display the actual rows of data
            for i in range(5):
                #printing 5 rows of data
                print("{}\n".format(df.iloc[[i+j]]))
            #checking if the user wants to see more data
            answer = input("Do you want to view more raw data?\n").lower()
            #checking if there is 5 or more rows of data
            if j+5 <= row_count:
                #increase j by 5 (start row index)
                j+=5
            #checking if there is no more data
            elif j >= row_count:
                #telling the user that there is no data left and breaking the while loop
                print("There is no more data to show")
                break
            #checking if there is data left but there is less than 5 rows of data
            else:
                j = row_count - j
                #for loop to print the remaining rows of data
                for i in range(row_count - j):
                    #printing remainig rows of data
                    print("{}".format(df.iloc[[i+j]]))
                print("There is no more data to show")
                break


def more_data_gender(df):
    """ displays trip duration data using gender filters"""


    while True:
        answer = input("Do you want to see gender specific info? (Enter 'yes' to see the data or otherwise to skip this part )\n")
        if answer.lower() == 'yes':
            #loop to take input for the gender
            while True:
                gender = input("Which gender would you like to see more information on? 'type male, female'\n")
                if gender.lower() == 'male' or gender == 'female':
                    break
                else:
                    print("Wrong input, try again!")

            if ('Gender' in df.columns):
                #find overall trip duration for target audience
                total_trip = df.loc[df['Gender'] == gender.title(), 'Trip Duration'].sum()
                total_trip = str(datetime.timedelta(seconds=int(total_trip)))
                #find overall trip duration for target audience
                avg_trip = df.loc[df['Gender'] == gender.title(), 'Trip Duration'].dropna(axis = 0).mean()
                avg_trip = str(datetime.timedelta(seconds = avg_trip))
                #print the total male and female stats
                print('average trip duration for {}s:\n{} hours'.format(gender,avg_trip))
                print("The total trip duration for {}s is:\n{} hours".format(gender,total_trip))
            else:
                print("Users gender data is not available")
                break

        else:
            break


def more_data_age(df):
    """ displays trip duration data using age filters"""
    while True:
        answer = input("Do you want to see age specific info?(Enter 'yes' to see the data or otherwise to skip this part )\n")
        if answer.lower() == 'yes' and ('Birth Year' in df.columns):

            #loop to take input for the year
            while True:
                year = input("Type a birth year to filter by:\n")
                if int(year) in df['Birth Year'].values:
                    break
                else:
                    print("Wrong input, try again! 'try typing another year'")
            #number of users born in the selected year
            year_count = (df['Birth Year'] == int(year)).sum()
            #find overall trip duration for target audience
            age_total_trip = df.loc[df['Birth Year'] == int(year), 'Trip Duration'].sum()
            age_total_trip = str(datetime.timedelta(seconds=int(age_total_trip)))
            #find overall trip duration for target audience
            age_avg_trip = df.loc[df['Birth Year'] == int(year), 'Trip Duration'].dropna(axis = 0).mean()
            age_avg_trip = str(datetime.timedelta(seconds = age_avg_trip))
            #print the total male and female numbers
            print('Number of users born in {}:\n{}'.format(year,year_count))
            print('average trip duration for users born in {}:\n{} hours'.format(year,age_avg_trip))
            print("The total trip duration for users born in {} is:\n{} hours".format(year,age_total_trip))


        else:
            print("If no data was shown this means that Users age data is not available")
            break



def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #a new dataframe to show raw filtered data
        df1 = df
        time_stats(df,city, month, day)
        station_stats(df,city, month, day)
        trip_duration_stats(df,city, month, day)
        user_stats(df)
        more_data_gender(df)
        more_data_age(df)
        raw_data(df1,city)




        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() == 'no':
                break

    img = Image.open('image1.jpg')
    img.show()

if __name__ == "__main__":
	main()
