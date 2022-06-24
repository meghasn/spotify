# spotify
Analysing my spotify data to understand more about my music preferences. This project is for education purpose.

First install the neccessary packages using
! pip install spotipy
! pip install requests
! pip install pandas

##DESCRIPTION OF FILES

#spotify.py
To access the spotify API

To access the spotify API, first you have to log in to the developer dashboard and click on 'create an app'.
An app can access the Spotify API, but only if it gets permission from at least one user. So we’ll use the app to ask ourselves permission to access our user data.
Go to edit settings and under the redirect uri add the 'redirect link' that we’ll use to collect the user’s permission. Here, I am using "http://localhost:7777/callback/" as the link
In the app panel you will also find client id and client secret.

Using these parameters, you can access the spotify API



Referals:
Data scrapping:
https://towardsdatascience.com/get-your-spotify-streaming-history-with-python-d5a208bbcbd3

