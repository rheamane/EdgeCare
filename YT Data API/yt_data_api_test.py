from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv

# Scopes for read-only access to the YouTube account
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

def main():
    # Set up the OAuth 2.0 flow
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
    credentials = flow.run_local_server()

    # Build the YouTube service
    youtube = build('youtube', 'v3', credentials=credentials)

    try:
        # Get the list of playlists for the authenticated user
        request = youtube.playlists().list(part='snippet', mine=True)
        response = request.execute()

        with open('playlists.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            writer.writerow(['Playlist Title', 'Playlist ID'])

        for item in response['items']:
            title = items['snippet']['title']
            playlistId = item['id']
            writer.writerow([title, playlistId])


    except HttpError as e:
        print(f"An error occurred: {e}")
        print(e)

if __name__ == '__main__':
    main()