import os
import sys 

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'client_id'
secret = 'client_secret'

auth_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=auth_manager)

print("Please input the playlist id: ")
id = input()
id = id.split('/')[-1].split('?')[0]
len = 0
total_dur = 0
alltracks = sp.playlist_tracks(id, None, 100)
while True:
    for track in alltracks['items']:
        total_dur += track['track']['duration_ms']
        len += 1
    
    if alltracks['next'] == None:
        break
    
    alltracks = sp.next(alltracks)

print('The average length is - ' + str(total_dur/len / 1000 / 60) + ' minutes')


    


