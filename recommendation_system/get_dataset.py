import spotipy
import yaml
from spotipy.oauth2 import SpotifyOAuth
from data_functions import offset_api_limit, get_artists_df, get_tracks_df, get_track_audio_df,\
    get_all_playlist_tracks_df, get_recommendations


# with open("spotify/spotify_details.yml", 'r') as stream:
    # spotify_details = yaml.safe_load(stream)

# https://developer.spotify.com/web-api/using-scopes/
scope = "user-library-read user-follow-read user-top-read playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='a9baa9ef73234a53baa6f03b5fd7c8d3',
    client_secret='58cd19810ee54b62b1fc4cf6ccd2d0b3',
    redirect_uri='http://localhost:7777/callback/',
    scope=scope,
))

# Spotify API calls and data manipulation
# Save for later to be quickly read by multiple workflows
print("Getting, transforming, and saving top artist data...")
# print(sp)
# print(sp.current_user_top_artists())
top_artists = offset_api_limit(sp, sp.current_user_top_artists())
top_artists_df = get_artists_df(top_artists)
top_artists_df.to_pickle("top_artists.pkl")

# print("Getting, transforming, and saving followed artist data...")
# followed_artists = offset_api_limit(sp, sp.current_user_followed_artists())
# print(followed_artists)
# followed_artists_df = get_artists_df(followed_artists)
# followed_artists_df.to_pickle("followed_artists.pkl")

print("Getting, transforming, and saving top track data...")
top_tracks = offset_api_limit(sp, sp.current_user_top_tracks())
top_tracks_df = get_tracks_df(top_tracks)
top_tracks_df = get_track_audio_df(sp, top_tracks_df)
top_tracks_df.to_pickle("top_tracks.pkl")

print("Getting, transforming, and saving saved track data...")
saved_tracks = offset_api_limit(sp, sp.current_user_saved_tracks())
saved_tracks_df = get_tracks_df(saved_tracks)
saved_tracks_df = get_track_audio_df(sp, saved_tracks_df)
saved_tracks_df.to_pickle("saved_tracks.pkl")

print("Getting, transforming, and saving playlist track data...")
"""
has to run and check from here onwards..both the pkl files below this not generated

"""
playlist_tracks_df = get_all_playlist_tracks_df(sp, sp.current_user_playlists())  # limit of 50 playlists by default
print(playlist_tracks_df.columns.tolist())
playlist_tracks_df = get_track_audio_df(sp, playlist_tracks_df)
print(playlist_tracks_df.columns.tolist())
# playlist_tracks_df.to_pickle("playlist_tracks.pkl")
# # Create yaml dump
# playlist_dict = dict(zip(playlist_tracks_df['playlist_name'], playlist_tracks_df['playlist_id']))
# print(playlist_dict)
# with open('playlists.yml', 'w') as outfile:
#     print("x")
#     yaml.dump(playlist_dict, outfile, default_flow_style=False)

# print("Getting, transforming, and saving tracks recommendations...")
# # Define a sample playlists to yield tracks to get recommendations for, 20 recommendations per track
# recommendation_tracks = get_recommendations(sp, top_tracks_df[top_tracks_df['playlist_name'].isin(
#     ["Chill", "Chill '20", "Chill '19", "Chill '18", "Your Top Songs 2020", "Your Top Songs 2019", "Your Top Songs 2018"
#      ])].drop_duplicates(subset='id', keep="first")['id'].tolist())
# recommendation_tracks_df = get_tracks_df(recommendation_tracks)
# recommendation_tracks_df = get_track_audio_df(sp, recommendation_tracks_df)
# recommendation_tracks_df.to_pickle("recommendation_tracks.pkl")