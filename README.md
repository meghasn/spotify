# spotify
Analysing my spotify data to understand more about my music preferences. This project is for education purpose.

First install the neccessary packages using
! pip install spotipy
! pip install requests
! pip install pandas

## DESCRIPTION OF FILES

# spotify.py

To access the spotify API

To access the spotify API, first you have to log in to the developer dashboard and click on 'create an app'.
An app can access the Spotify API, but only if it gets permission from at least one user. So we’ll use the app to ask ourselves permission to access our user data.
Go to edit settings and under the redirect uri add the 'redirect link' that we’ll use to collect the user’s permission. Here, I am using "http://localhost:7777/callback/" as the link
In the app panel you will also find client id and client secret.

Using these parameters, you can access the spotify API


# spotify_data_scrapping.py

Data scrapping is the process of importing information from a website into a spreadsheet or local file saved on your computer. Using the API's you can generate track is for the song and get the respective track features. In this file we have generated the track id and features of a single song.

# spotify_create_dataset

Now using the information we have from the previous 2 files we are going to create a dataset that contains all the songs in your steaming history along with their different features like danceability, energy, loudness, sound etc.

# mymusicpatterns.py

Convert StreamingHistory json file to csv

# spotify_popularity_artist_genre.py

created a dataset having the song name and popularity..Was not able to get the song genre. If anyone find out how to do it, feel free to add

Suggest various recommendations using the obtained datasets

# additional dataset folder

contains code to generate some additional datasets using your spotify data

# data folder 

contains all the datasets created

Various ideas:
Genre classification
Automatic playlist creation
Automatic song addittion to playlist
Combined playlist based on tow or more users' data
Andhakshari player :)

Referals:
Data scrapping:
https://towardsdatascience.com/get-your-spotify-streaming-history-with-python-d5a208bbcbd3

Additonal Dataset:
https://towardsdatascience.com/machine-learning-and-recommender-systems-using-your-own-spotify-data-4918d80632e3

