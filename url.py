import requests
import pandas as pd

# Function to get Spotify access token
def get_spotify_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
    
    if auth_response.status_code == 200:
        auth_data = auth_response.json()
        return auth_data['access_token']
    else:
        print(f"Error: Unable to get token, Status Code: {auth_response.status_code}")
        print(f"Response: {auth_response.text}")
        return None

# Function to search for a track and get its ID
def search_track(track_name, artist_name, token):
    query = f"{track_name} artist:{artist_name}"
    url = f"https://api.spotify.com/v1/search?q={query}&type=track"
    response = requests.get(url, headers={
        'Authorization': f'Bearer {token}'
    })
    json_data = response.json()
    
    try:
        first_result = json_data['tracks']['items'][0]
        track_id = first_result['id']
        return track_id
    except (KeyError, IndexError):
        return None

# Function to get track details
def get_track_details(track_id, token):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    response = requests.get(url, headers={
        'Authorization': f'Bearer {token}'
    })
    json_data = response.json()
    try:
        image_url = json_data['album']['images'][0]['url']
        return image_url
    except (KeyError, IndexError):
        return None

# Your Spotify API Credentials
client_id = '426570b13cda421e88ba807feba56e41'
client_secret = 'fe59ad496327442cb047dcaf6cf98360'

# Get Access Token
access_token = get_spotify_token(client_id, client_secret)

if access_token is None:
    print("Error: Unable to proceed without access token.")
else:
    # Read your DataFrame (replace with the correct path to your CSV file)
    df_spotify = pd.read_csv(r'C:\Users\akars\OneDrive\Desktop\spotify dashboard\spotify-2023.csv', encoding='ISO-8859-1')

    # Loop through each row to get track details and add to DataFrame
    for i, row in df_spotify.iterrows():
        track_id = search_track(row['track_name'], row['artist(s)_name'], access_token)
        if track_id:
            image_url = get_track_details(track_id, access_token)
            if image_url:
                df_spotify.at[i, 'image_url'] = image_url

    # Save the updated DataFrame (replace 'updated_file.csv' with your desired output file name)
    df_spotify.to_csv(r'C:\Users\akars\OneDrive\Desktop\spotify dashboard\updated_file.csv', index=False)

