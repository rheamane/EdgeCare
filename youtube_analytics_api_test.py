import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
import csv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']

API_SERVICE_NAME = 'youtubeAnalytics'
API_VERSION = 'v2'
CLIENT_SECRETS_FILE = "client_secret_716368587013-doic4i0c3el73k2fbabaniqt6k5q9vqj.apps.googleusercontent.com.json"
def get_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_local_server()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def execute_api_request(client_library_function, **kwargs):
    response = client_library_function(
        **kwargs
    ).execute()

    with open('yt_analytics_data.csv', 'w', newline='') as csvfile:
        fieldnames = response['columnHeaders'][0]['name'], response['columnHeaders'][1]['name'], response['columnHeaders'][2]['name'], response['columnHeaders'][3]['name'], response['columnHeaders'][4]['name']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        for row in response['rows']:
            writer.writerow(row)

    print("Data saved")
    print(response)

if __name__ == '__main__':
      # Disable OAuthlib's HTTPs verification when running locally.
      # *DO NOT* leave this option enabled when running in production.
      os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

      youtubeAnalytics = get_service()
      execute_api_request(
          youtubeAnalytics.reports().query,
          ids='channel==MINE',
          startDate='2023-01-01',
          endDate='2023-12-31',
          metrics='estimatedMinutesWatched,views,likes,subscribersGained',
          dimensions='day',
          sort='day',
          maxResults=5
      )