
from django.core import paginator
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, response
from django.core.paginator import Paginator

import pymongo


from ytapi import mongo_client,youtube,afterdate,db

def getRecords(request):
	"""
	Returns a GET Response of the records stored in the database in a paginated form
	"""

	page = request.GET.get('page','')
	# print(page)
	res = db.VideoData.find().sort('publishedAt',pymongo.DESCENDING) # fetch data from the database in reverse chronological manner

	records_list = list(res)
	for r in records_list:
		del r['_id']
	
	paginator = Paginator(records_list,10) # paginating the response
	paged_data = paginator.get_page(page) 

	return HttpResponse(paged_data)
 
	
def clearRecords(request):
	"""
	Clears the database 
	"""
	db.VideoData.drop()
	return JsonResponse({"status":"deleted"})
