# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:28:35 2024

@author: CLEMENT H MALULEKE
"""

import pandas as pd
import matplotlib.pyplot as plt



df= pd.read_csv("C:/Users/CLEMENT H MALULEKE/Documents/Python Scripts/Summer_Coding_School/Project/Project/.spyproject/movie_dataset.csv")

print(df.info())

#Rename the two columns with spaces
df=df.rename(columns={'Runtime (Minutes)': 'Runtime_(Mins)', 'Revenue (Millions)': 'Revenue_(Millions)'})


##Dropind the ranking column.
df.drop(columns=['Rank'], inplace = True)

print(df.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 11 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Title               1000 non-null   object 
 1   Genre               1000 non-null   object 
 2   Description         1000 non-null   object 
 3   Director            1000 non-null   object 
 4   Actors              1000 non-null   object 
 5   Year                1000 non-null   int64  
 6   Runtime_(Mins)      1000 non-null   int64  
 7   Rating              1000 non-null   float64
 8   Votes               1000 non-null   int64  
 9   Revenue_(Millions)  872 non-null    float64
 10  Metascore           936 non-null    float64
dtypes: float64(3), int64(3), object(5)
memory usage: 86.1+ KB
None

"""
#remove diplicates in the dataset
df.drop_duplicates(inplace=True)

#calculate the avarage metascore and use it to fill the banks
avg_metascore= round(df['Metascore'].mean())
#fill the blanks witht the avarage

df['Metascore'].fillna(avg_metascore, inplace = True)

"""
instead of removing all the rows with nan on the  Revenue_millions lets just fill the values with the avarage revenue

"""

#calculate the avarage Revenue and use it to fill the banks
avg_revenue= round(df['Revenue_(Millions)'].mean(),2)

    
#fill the blanks witht the avarage
df['Revenue_(Millions)'].fillna(avg_revenue, inplace = True)


# df.dropna( inplace= True)
print(df.info())


print(df['Rating'].describe())

"""
Data cleaning is now done and the data is tidy and ready for the first steps of analysis.

"""

"""
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1000 entries, 0 to 999
Data columns (total 11 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Title               1000 non-null   object 
 1   Genre               1000 non-null   object 
 2   Description         1000 non-null   object 
 3   Director            1000 non-null   object 
 4   Actors              1000 non-null   object 
 5   Year                1000 non-null   int64  
 6   Runtime_(Mins)      1000 non-null   int64  
 7   Rating              1000 non-null   float64
 8   Votes               1000 non-null   int64  
 9   Revenue_(Millions)  1000 non-null   float64
 10  Metascore           1000 non-null   float64
dtypes: float64(3), int64(3), object(5)
memory usage: 93.8+ KB
None

"""


print(df.info())

"""
QUESTION 1

What is the highest rated movie in the dataset?
"""

highest_rated_movie= df[df['Rating']==9.000000]

"""
***************************ANSWER**************************
Title	Genre	Description	Director	Actors	Year	Runtime_(Mins)	Rating	Votes	Revenue_(Millions)
The Dark Knight	Action, Crime, Drama	When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the Dark Knight must come to terms with one of the greatest psychological tests of his ability to fight injustice.	Christopher Nolan	Christian Bale, Heath Ledger, Aaron Eckhart,Michael Caine	2008	152	9.0	1791916	533.32

"""
"""
***********************ANSWER********************
The Dark Knight

"""

"""
*****************QUESTION_2**********************************

What is the average revenue of all movies in the dataset? 
Note, since the answer will be effected by how you dealt with missing values a
range has been provided. 

"""

avg_revenue = df['Revenue_(Millions)'].mean()
print(avg_revenue)

"""
**********************ANSWER***************

82.9568400000002

SO THE INTERVAL IS Between 70 and 100 Million


"""


"""
**************************QUESTION_3***********************



What is the average revenue of movies from 2015 to 2017 in the dataset?

Note, since the answer will be effected by how you dealt with missing values a range has been provided. 

"""
# df.columns=df.columns.str.replace(" ","")
# avg_reveue = df['Revenue_(Millions)'].mean()
# temp=df[df['Year']>=2015] & (df['Year']<= 2017)
# Mean_revenue=temp['Revenue_(Millions)'].mean()


"""
**************************QUESTION_4*************************
How many movies were released in the year 2016?

"""
#First make a subset of the data frame for this question so that you dont mess the original dataframe

dfq3= df[df['Year']==2016]

"""
**********ANSWER*****************
297 MOVIES

"""



"""
*********************************QUESTION_5******************************************
How many movies were directed by Christopher Nolan?


"""
Chris_directed= df[df['Director']=="Christopher Nolan"]


"""
*****************************ANSWER*********************************
5 MOVIES

"""



"""
*****************************Question_6********************
How many movies in the dataset have a rating of at least 8.0?


"""
ratings_ge_8= df[df['Rating']>= 8.00]
print(len(ratings_ge_8))

"""
*****************************ANSWER*********************************
78 MOVIES

"""



"""
*************************QUESTION_7*******************************
What is the median rating of movies directed by Christopher Nolan?


""" 
Chris_directed_Median= Chris_directed['Rating'].median()

"""
the median is rating is 8.6

"""



"""
**************************QUESTION_8****************************
Find the year with the highest average rating?

 
"""


grouped = df.groupby('Year')
average_rating_per_year = grouped['Rating'].mean()


"""
********************************************ANSWER********************************
2007
"""





"""
*************************QUESTION_9*******************************
What is the percentage increase in number of movies made between 2006 and
2016?

"""

movies_in_2006 = len(df[df['Year']== 2006])
movies_in_2016 = len(df[df['Year']== 2016])

diff_2006_and_2016= movies_in_2016 - movies_in_2006 
# percentage_diff = (diff_2006_and_2016/movies_in_2016)*100

# print("the percentage difference is : ", round(percentage_diff, 2))

"""
*******************************************ANSWER**************************************************
THE PERCENTAGE DIFFERENCE BETWEEN THE TWO YEARS IS 253
"""



"""
***********************************QUESTION_10************************************
Find the most common actor in all the movies?
Note, the "Actors" column has multiple actors names. You must find a way to
search for the most common actor in all the movies

"""
actors= df['Actors'].str.split(', ').explode()
actor_count= actors.value_counts()
most_common_actor = actor_count.idxmax()











"""
***********************************QUESTION_11***********************************


How many unique genres are there in the dataset?

Note, the "Genre" column has multiple genres per movie. You must find a way to identify them individually.

"""


Genres =df['Genre'].str.split(', ').explode()
unique_genres_count= Genres.nunique()




"""
now lets explore the relationship between few columns and this will help identify suspected outliers.

"""

plt.scatter(df['Votes'],df['Revenue_(Millions)'])
plt.xlabel('Votes')
plt.ylabel('Revenue in (millions)')
plt.title('Revenue against the Votes recieved')
plt.show()
print(df.info())

"""
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1000 entries, 0 to 999
Data columns (total 11 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Title               1000 non-null   object 
 1   Genre               1000 non-null   object 
 2   Description         1000 non-null   object 
 3   Director            1000 non-null   object 
 4   Actors              1000 non-null   object 
 5   Year                1000 non-null   int64  
 6   Runtime_(Mins)      1000 non-null   int64  
 7   Rating              1000 non-null   float64
 8   Votes               1000 non-null   int64  
 9   Revenue_(Millions)  1000 non-null   float64
 10  Metascore           1000 non-null   float64
dtypes: float64(3), int64(3), object(5)
memory usage: 126.0+ KB
None
"""

plt.scatter(df['Votes'],df['Rating'])
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('relationship between Votes and Ratings')
plt.show()


plt.scatter(df['Rating'],df['Revenue_(Millions)'])
plt.xlabel('Votes')
plt.ylabel('Revenue in millions')
plt.title('relationship between Votes and Ratings')
plt.show()

plt.scatter(df['Metascore'],df['Revenue_(Millions)'])
plt.xlabel('Metascore')
plt.ylabel('Revenue in millions')
plt.title('relationship between Votes and Ratings')
plt.show()




"""
Create a profiling report


"""

# from ydata_Profiling import ProfileReport

# profile= ProfileReport(df,title = "My Report")
# profile.to_file("My_Report.html")



import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(df,hue="Year")
plt.show()

# sns.heatmap(df)
# plt.show()
























































































































