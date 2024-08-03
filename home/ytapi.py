
from django.http import JsonResponse
from googleapiclient.discovery import build
from django.conf import settings


def get_subscriber_count(channel_id):
    api_key = settings.YOUTUBE_API_KEY
    youtube = build('youtube', 'v3', developerKey=api_key)
    res = youtube.channels().list(id=channel_id, part='statistics').execute()

    if 'items' in res and len(res['items']) > 0:
        subscriber_count = res['items'][0]['statistics']['subscriberCount']
        return subscriber_count
    else:
        return {'error': 'Channel not found'}
    

# print(('UC0bG20RykiBFmCBqabR_5pg')) 