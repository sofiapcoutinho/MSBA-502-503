#Sofia Pereira Coutinho
#Company XYZ Consulting Project
#Data Cleaning and Transforming

#This program will clean and transform a dataset from Company XYZ, a zoo that specializes in desert preservation.
#The dataset contains data about attendance in the zoo from August 2017 to October 2022. Each row in the data represents an attendance point.
#The goal of the program is to group attendance by day; remove any unnecessary columns, and create any necessary columns for this analysis; and transform any categorical data into numerical data, for ease of analysis.
#The final clean dataset will be used to create regression models to predict and explain attendance.

#The program will have the following steps:
#1. IMPORTS & VARIABLE SETUP
#2. CLEANING
#3. CREATE CATEGORICAL COLUMNS
#4. GROUPING
#5. FIX DUMMY VARIABLES
#6. CREATE MONTH COLUMN
#7. CREATE COVID COLUMN


########## 1. IMPORTS & VARIABLE SETUP ##########

#import necessary packages
import os, pandas as pd

#setting up input/output variables
directory = 'C:/Users/Profile/downloads'

INPUT_DATA_FILE = 'Sample_Data.csv'

OUTPUT_DATA_FILE = 'Final_Data.csv'

#set directory
os.chdir(directory)

#import csv file as dataframe
df = pd.read_csv(INPUT_DATA_FILE)


########## 2. CLEANING ##########

def transform_type(df_number, attribute, datatype):
    '''Transforms specified column to specified datatype'''
    df_number[attribute] = df_number[attribute].astype(datatype)
    
#include data only for attendance points
df = df[df['Attend or Attract'] == 'Attend']

#store attend type and event columns in arrays 
attend = df['Attend Type']
events = df['Report Group']

#delete unnecessary columns
df_1 = df.drop(columns = ['Access Type', 'Attend Type', 'Attend or Attract', 'Descr', 'Membership Type', 'Report Group', 'Sales Node', 'Ticket Count'])

#convert date column to date datatype
df_1['Date Open'] = pd.to_datetime(df_1['Date Open'])

#convert ticket quantities to int datatype
transform_type(df_1, 'Adult Qty', int)
transform_type(df_1, 'Child Qty', int)
transform_type(df_1, 'Total Qty', int)


########## 3. CREATE CATEGORICAL COLUMNS ##########

#create the categorical columns for attend type
df_1.insert(1, 'Unscanned', attend, True)
df_1.insert(2, 'Regular', attend, True)
df_1.insert(3, 'Member', attend, True)

#replace data with 1s and 0s to convert categorical into numerical variables
df_2 = df_1.replace({'Unscanned': {'Unscanned Ticket':'1', 'Regular Ticket':'0', 'Member Ticket':'0', 'Member Pass':'0'},
                     'Regular': {'Unscanned Ticket':'0', 'Regular Ticket':'1', 'Member Ticket':'0', 'Member Pass':'0'},
                     'Member':{'Unscanned Ticket':'0', 'Regular Ticket':'0', 'Member Ticket':'1', 'Member Pass':'1'}
                     })

#convert datatype to int
transform_type(df_2, 'Unscanned', int)
transform_type(df_2, 'Regular', int)
transform_type(df_2, 'Member', int)

#create the categorial columns for events (report group)
df_2.insert(8, 'Brew', events, True)
df_2.insert(9, 'Howloween', events, True)
df_2.insert(10, 'Lanterns', events, True)
df_2.insert(11, 'Wildlights', events, True)
df_2.insert(12, 'Other', events, True)

#replace data with 1s and 0s for each of the three columns to make dummy variables
df_3 = df_2.replace({'Brew': {'BFAST EVENT':'0', 'BREW':'1', 'BUTTERFLY':'0', 'CAMEL':'0', 'CAMEL ADDON':'0', 'CAROUSEL':'0', 'CONSERVATION':'0', 'DEVELOPMENT':'0', 'DNU':'0', 'EDU ADDON':'0', 'EDUCATION':'0', 'GENERAL':'0', 'GIRAFFE':'0', 'GROUP SALES':'0', 'HOWL-O-WEEN':'0', 'LANTERNS':'0', 'LORIKEET':'0', 'LORIKEET ADD':'0', 'MEMBERSHIP':'0', 'PRIVATE EVNT':'0', 'PROMO ADDON':'0', 'PROMOTIONS':'0', 'SCHOOL TOURS':'0', 'SHUTTLE':'0', 'TOUR':'0', 'WILDLIGHTS':'0'},
                     'Howloween': {'BFAST EVENT': '0', 'BREW': '0', 'BUTTERFLY': '0', 'CAMEL': '0', 'CAMEL ADDON':'0', 'CAROUSEL': '0',
                              'CONSERVATION': '0', 'DEVELOPMENT': '0', 'DNU': '0', 'EDU ADDON': '0', 'EDUCATION': '0',
                              'GENERAL': '0', 'GIRAFFE': '0', 'GROUP SALES': '0', 'HOWL-O-WEEN': '1', 'LANTERNS': '0',
                              'LORIKEET': '0', 'LORIKEET ADD': '0', 'MEMBERSHIP': '0', 'PRIVATE EVNT': '0',
                              'PROMO ADDON': '0', 'PROMOTIONS': '0', 'SCHOOL TOURS': '0', 'SHUTTLE': '0', 'TOUR': '0',
                              'WILDLIGHTS': '0'},
                     'Lanterns': {'BFAST EVENT': '0', 'BREW': '0', 'BUTTERFLY': '0', 'CAMEL': '0', 'CAMEL ADDON':'0', 'CAROUSEL': '0',
                              'CONSERVATION': '0', 'DEVELOPMENT': '0', 'DNU': '0', 'EDU ADDON': '0', 'EDUCATION': '0',
                              'GENERAL': '0', 'GIRAFFE': '0', 'GROUP SALES': '0', 'HOWL-O-WEEN': '0', 'LANTERNS': '1',
                              'LORIKEET': '0', 'LORIKEET ADD': '0', 'MEMBERSHIP': '0', 'PRIVATE EVNT': '0',
                              'PROMO ADDON': '0', 'PROMOTIONS': '0', 'SCHOOL TOURS': '0', 'SHUTTLE': '0', 'TOUR': '0',
                              'WILDLIGHTS': '0'},
                     'Wildlights': {'BFAST EVENT': '0', 'BREW': '0', 'BUTTERFLY': '0', 'CAMEL': '0', 'CAMEL ADDON':'0', 'CAROUSEL': '0',
                              'CONSERVATION': '0', 'DEVELOPMENT': '0', 'DNU': '0', 'EDU ADDON': '0', 'EDUCATION': '0',
                              'GENERAL': '0', 'GIRAFFE': '0', 'GROUP SALES': '0', 'HOWL-O-WEEN': '0', 'LANTERNS': '0',
                              'LORIKEET': '0', 'LORIKEET ADD': '0', 'MEMBERSHIP': '0', 'PRIVATE EVNT': '0',
                              'PROMO ADDON': '0', 'PROMOTIONS': '0', 'SCHOOL TOURS': '0', 'SHUTTLE': '0', 'TOUR': '0',
                              'WILDLIGHTS': '1'},
                     'Other': {'BFAST EVENT': '1', 'BREW': '0', 'BUTTERFLY': '1', 'CAMEL': '1', 'CAMEL ADDON':'1', 'CAROUSEL': '1',
                              'CONSERVATION': '1', 'DEVELOPMENT': '1', 'DNU': '1', 'EDU ADDON': '1', 'EDUCATION': '1',
                              'GENERAL': '1', 'GIRAFFE': '1', 'GROUP SALES': '1', 'HOWL-O-WEEN': '0', 'LANTERNS': '0',
                              'LORIKEET': '1', 'LORIKEET ADD': '1', 'MEMBERSHIP': '1', 'PRIVATE EVNT': '1',
                              'PROMO ADDON': '1', 'PROMOTIONS': '1', 'SCHOOL TOURS': '1', 'SHUTTLE': '1', 'TOUR': '1',
                              'WILDLIGHTS': '0'}
                     })

#convert datatype to int
event_names = ['Brew', 'Howloween', 'Lanterns', 'Wildlights', 'Other']

for i in event_names:
    transform_type(df_3, i, int)


########## 4. GROUPING ##########

#group data by each day to have only one row per day
df_4 = df_3.groupby(['Date Open'], as_index=False).sum()
df_4.sort_values(by='Date Open', inplace = True)


########## 5. FIX DUMMY VARIABLES ##########

#after grouping, dummy variables were summed. convert back to 1 on days where the event occured
df_4.loc[df_4['Brew'] > 0, 'Brew'] = 1
df_4.loc[df_4['Howloween'] > 0, 'Howloween'] = 1
df_4.loc[df_4['Lanterns'] > 0, 'Lanterns'] = 1
df_4.loc[df_4['Wildlights'] > 0, 'Wildlights'] = 1
df_4.loc[df_4['Other'] > 0, 'Other'] = 1


########## 6. CREATE MONTH COLUMN ##########

#create month column with the full date
df_4.insert(1, 'Month', df_4['Date Open'], True)

#keep only the month number in the column
df_4['Month'] = pd.DatetimeIndex(df_4['Month']).month

month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def month_transform():
    '''Creates month name columns and inserts 1s in the corresponding month column for each row'''
    df_4.loc[df_4['Month'] == i + 1, month_names[i]] = 1

#loops through each month to call the month_transform function
for i in range(0, 12):
    month_transform()
    
#drop the original month column
df_5 = df_4.drop(columns = ['Month'])


########## 7. CREATE COVID COLUMN ##########

#create dummy variable column for Covid-19 dates
df_5.loc[df_5['Date Open'].between('2020-2-1', '2021-7-31'), 'Covid'] = 1

#transform all NA values in new month name columns to 0
df_6 = df_5.fillna(0)

#transform new month and covid columns to int
for i in month_names:
    transform_type(df_6, i, int)

transform_type(df_6, 'Covid', int)


########## EXPORT ##########

#export to csv file
df_6.to_csv(OUTPUT_DATA_FILE)


########## END OF CODE ##########