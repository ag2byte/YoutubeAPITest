import googleapiclient.discovery
from pymongo import MongoClient

import dotenv
import time
import os
import threading
import datetime
import json

dotenv.read_dotenv()
# getting environment variables
mongo_client = MongoClient(os.environ.get('MONGO_DB_HOST'),int(os.environ.get('MONGO_DB_PORT')))
api_key = os.environ.get('YOUTUBE_API_KEY')
youtube_query = os.environ.get('YOTUUBE_QUERY_TERM')


youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey = api_key) # building the youtube API with the api_key 
afterdate = (datetime.datetime.now()- datetime.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")

# connecting to the mongodb database
db = mongo_client.ytapi
db.VideoData.create_index('id',unique = True)

def main():
    while True:
        time.sleep(int(os.environ.get('SLEEP_INTERVAL')))
        run_in_background()

def run_in_background():
    """Runs in background refreshing the content in the database every fixed interval of time"""
    message = youtube.search().list(
        part="snippet",
        maxResults=20,
        q=youtube_query,
		type='video',
		order='date',
		publishedAfter=afterdate) # youtube search Query

    response = message.execute()

    for item in response['items']:
        video_data ={}
		
        video_data['id'] = item['id']
        video_data['title'] = item['snippet']['title']
        video_data['description'] =item['snippet']['description']
        video_data['thumbnails'] = item['snippet']['thumbnails']
        video_data['publishedAt'] = item['snippet']['publishedAt']
        video_data['channel'] = item['snippet']['channelTitle']
        json_data = json.dumps(video_data)
        try:
            newrecord = db.VideoData.insert_one(json.loads(json_data)) # inserting data in mongodb database
            print("INSERTED"+str(newrecord.inserted_id))
        except Exception as e:
            pass
    
t1 = threading.Thread(target=main) # background process runs in a seperate thread
t1.start()


