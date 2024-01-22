
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','PUT','POST'])
def index(request):
    

        courses={
            'course_name':'python',
            'learn':['flask','django','tornado'],
            'curse_provider':'scaler'

        }
        if request.method=='GET':
            print('get met')
            return Response(courses)
        elif request.method=='POST':
            print('post met')
            return Response(courses)

# Create your views here.
