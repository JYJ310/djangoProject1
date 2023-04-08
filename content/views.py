from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import Feed

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')


        return render(request, 'star/main.html', context=dict(feeds=feed_list))

