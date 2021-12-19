# from json.decoder import JSONDecodeError
from django.core import paginator
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, response
from django.core.paginator import Paginator

import pymongo


from ytapi import mongo_client,youtube,afterdate,db


# def index(request):

# 	message = youtube.search().list(
#         part="snippet",
#         maxResults=20,
#         q="no way home",
# 		type='video',
# 		order='date',
# 		publishedAfter=afterdate


#     )
# 	response = message.execute()

# 	for item in response['items']:
# 		video_data ={}
		
# 		video_data['id'] = item['id']
# 		video_data['title'] = item['snippet']['title']
# 		video_data['description'] =item['snippet']['description']
# 		video_data['thumbnails'] = item['snippet']['thumbnails']
# 		video_data['publishedAt'] = item['snippet']['publishedAt']
# 		video_data['channel'] = item['snippet']['channelTitle']
# 		json_data = json.dumps(video_data)
# 		try:
# 			newrecord = db.VideoData.insert_one(json.loads(json_data))
# 			print("INSERTED"+str(newrecord.inserted_id))
# 		except Exception as e:
# 			pass

	
# 	return JsonResponse({'ok':'ok'})


def getRecords(request):

	page = request.GET.get('page','')
	print(page)
	res = db.VideoData.find().sort('publishedAt',pymongo.DESCENDING)

	records_list = list(res)
	for r in records_list:
		del r['_id']
	
	paginator = Paginator(records_list,10)
	paged_data = paginator.get_page(page)

	return HttpResponse(paged_data)
 
	
def clearRecords(request):
	db.VideoData.drop()
	return JsonResponse({"status":"deleted"})
