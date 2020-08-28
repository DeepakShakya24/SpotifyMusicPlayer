from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# Create your views here.
def index(request):
    if request.method=='POST':
        artist_uri=request.POST.get('uri')
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='a338296a311d420d80e7ee79b1a85ced',client_secret='68d45066f0064f84b8b44769b0e7db66'))
        results = spotify.search(q=artist_uri,limit=20)
        final_results=results['tracks']['items']
        return render(request,'index.html',{'results':final_results})
    else:
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='a338296a311d420d80e7ee79b1a85ced',client_secret='68d45066f0064f84b8b44769b0e7db66'))
        result = spotify.search(q='Ed Sheeran', limit=10)
        final_results2=result['tracks']['items']
        return render(request,'index.html',{'result':final_results2})