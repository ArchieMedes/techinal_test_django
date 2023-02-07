from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse
from activitie.serializer import ActivitySerializer, ActivityEditSerializer
from rest_framework.response import Response
from rest_framework import permissions, status
from activitie.models import ActivityModel
import requests

# Create your views here.
# generar actividad (create)
class CreateActivity(APIView):
    
    permission_classes = (permissions.IsAuthenticated,)

    # create activity
    def post(self, request):
        
        # pulling data (activities) from API:
        response = requests.get('https://www.boredapi.com/api/activity')
        
        # convert response data into json
        activitie = response.json()
        print('activitie:', activitie)

        link = activitie['link']
        print('link:', link)
        if( link == '' ):
            print('no viene link')
            activitie['link'] = 'no_link'

        print('self.request.user.is_authenticated:', self.request.user.is_authenticated)
        # almacenar en la base de datos()
        serializer = ActivitySerializer(data = activitie)
        serializer.is_valid(raise_exception = True)
        serializer.save(user_id = self.request.user)
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    # get activities for a specific user
    def get(self, request):
        # a filter of the objects registered
        activities = ActivityModel.objects.filter(user_id = self.request.user)
        print('activities:', activities)
        serializer = ActivitySerializer(activities, many = True) # many = True because we going to get many registers
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request):
        request_data = request.data
        print('request_data:', request_data)
        activity_id = request_data["activityID"]
        print('activity_id:', activity_id)

        activity_object = get_object_or_404(ActivityModel.objects.filter(done = False), user_id = self.request.user, id = activity_id )
        print('activity_object:', activity_object)
        activity_object.done = True
        serializer = ActivityEditSerializer(instance = activity_object, data = request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    