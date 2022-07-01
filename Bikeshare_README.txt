In this project, I used Python to explore data related to bike share systems for three major cities in the
United States: Chicago, New York City, and Washington. 
I wrote code to import the data from csv files (I could not upload them to github because of the size restriction) 
and answered some questions about it by computing descriptive statistics. 
I also provided an interactive experience in the terminal.

Information about the datasets:

Randomly selected data for the first six months of 2017 are provided for all three cities. 
All three of the data files contain the same core six (6) columns:

Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

Gender
Birth Year

Statistics Computed:

#1 Popular times of travel (i.e., occurs most often in the start time)

most common month
most common day of week
most common hour of day

#2 Popular stations and trip:

most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)

#3 Trip duration:

total travel time
average travel time

#4 User info:

counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)
The option to view data based on gender or age