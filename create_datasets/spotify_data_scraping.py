import requests
import spotipy
token='BQD-R2eW3tgXyKCbhBto49qmXiQhnt7IZzTUH_5uSpAVn11B-0EjaePyrkagMo6bLGDR91cObBo4HFTYi92jPNOMlKbmJ5CILmBMjeQ3zWKLq29t8ud5WCI55GL1k2yTe5_82C3il7N0PZdK1CojLkyN2JQneQK6aSYzKx6cu03nKyMVtJVqKCcEwkLVpApyhTBpgkY'
"""
input: track_name, access token generated earlier
output: track id

request.get() -> return the response
response.json() -> returns a json object of the response
"""
def get_id(track_name: str, token: str, artist:str) -> str:

    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer ' + token,
    }
    params = [('q', track_name),('type', 'track')]
    try:
        response = requests.get('https://api.spotify.com/v1/search', 
                    headers = headers, params = params, timeout = 5)
        json = response.json()
        first_result = json['tracks']['items'][0]
        track_id = first_result['id']
        return track_id
    except:
        return None

    

Runaway_id = get_id('Runaway', token, artist = 'AURORA')
print(Runaway_id)
#1v1oIWf2Xgh54kIWuKsDf6
"""
input: track_id, token
output=features
using the object sp extracting the required features
"""
def get_features(track_id: str, token: str) -> dict:
    sp = spotipy.Spotify(auth=token)
    try:
        features = sp.audio_features([track_id])
        return features[0]
    except:
        return None
Runaway_features = get_features(Runaway_id, token)
print(Runaway_features)
"""
{'danceability': 0.422, 'energy': 0.302, 'key': 11, 'loudness': -9.214, 'mode': 1, 'speechiness': 0.0372, 'acousticness': 0.629, 'instrumentalness': 7.83e-05, 'liveness': 0.104, 'valence': 0.123, 'tempo': 114.089, 'type': 'audio_features', 'id': '1v1oIWf2Xgh54kIWuKsDf6', 'uri': 'spotify:track:1v1oIWf2Xgh54kIWuKsDf6', 'track_href': 'https://api.spotify.com/v1/tracks/1v1oIWf2Xgh54kIWuKsDf6', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/1v1oIWf2Xgh54kIWuKsDf6', 'duration_ms': 248827, 'time_signature': 4}

"""
