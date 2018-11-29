from django.shortcuts import render

from .models import Movies
# Create your views here.
from django.views import View


class AnimationView(View):
    def get(self,request):
        return render(request,'home/animation.html')


class PlayView(View):
    def get(self,request,id):
        movie = Movies.objects.get(id=id)
        list=[]
        for i in range(movie.star):
            list.append(i)
        print(list)
        return render(request,'home/play.html',{"movie":movie,'star':list})