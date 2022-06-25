import ast
from typing import List
from os import listdir
import spotipy.util as util
import spotipy
import pandas as pd
import requests
"""
input: My Data-> file in which all the downloaded json files are stored
get all the files from StreamingHistory.json
return the streamings
take the unique track names from these streamings and use it to get respective track id and features
"""
def get_streamings(path: str = 'MyData') -> List[dict]:
    
    files = ['MyData/' + x for x in listdir(path)
             if x.split('.')[0][:-1] == 'StreamingHistory']
    
    all_streamings = []
    
    for file in files: 
        with open(file, 'r', encoding='UTF-8') as f:
            new_streamings = ast.literal_eval(f.read())
            all_streamings += [streaming for streaming 
                               in new_streamings]
    return all_streamings


"""
get_id and get_features are the same fns from spotify_data_scraping
"""

token='BQD-R2eW3tgXyKCbhBto49qmXiQhnt7IZzTUH_5uSpAVn11B-0EjaePyrkagMo6bLGDR91cObBo4HFTYi92jPNOMlKbmJ5CILmBMjeQ3zWKLq29t8ud5WCI55GL1k2yTe5_82C3il7N0PZdK1CojLkyN2JQneQK6aSYzKx6cu03nKyMVtJVqKCcEwkLVpApyhTBpgkY'
def get_id(track_name: str, token: str) -> str:
    # print(track_name,token)
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer ' + token,
    }
    params = [('q', track_name),('type', 'track')]
    try:
        print("x")
        response = requests.get('https://api.spotify.com/v1/search', 
                    headers = headers, params = params, timeout = 5)
        print(response)
        json = response.json()
        first_result = json['tracks']['items'][0]
        track_id = first_result['id']
        return track_id
    except:
        return None

def get_features(track_id: str, token: str) -> dict:
    sp = spotipy.Spotify(auth=token)
    try:
        features = sp.audio_features([track_id])
        return features[0]
    except:
        return None
streamings = get_streamings()
# print(streamings)
unique_tracks = list(set([streaming['trackName'] 
                for streaming in streamings]))
# print(unique_tracks)
all_features = {}
for track in unique_tracks:
    track_id = get_id(track, token)
    features = get_features(track_id, token)
    print(track_id)
    if features:
        all_features[track] = features
with_features = []
print(all_features)
for track_name, features in all_features.items():
    with_features.append({'name': track_name, **features})
print(with_features)
df = pd.DataFrame(with_features)
df.to_csv('streaming_history.csv')