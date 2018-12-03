from django.shortcuts import render

from .models import Movies, Preview
from user_operation.models import Comment
# Create your views here.
from django.views import View


# 预告页面
class AnimationView(View):
    def get(self, request):
        previews = Preview.objects.all().order_by("-add_time")[:5]
        return render(request, 'home/animation.html', {"previews": previews})


# 播放页面
class PlayView(View):
    def get(self, request, id):
        movie = Movies.objects.get(id=id)
        list = []
        for i in range(movie.star):
            list.append(i)
        print(list)
        comments = Comment.objects.filter(movie__id__in=id)
        return render(request, 'home/play.html', {"movie": movie, 'star': list, "comments": comments})


# 电影搜索
class SearchView(View):
    def get(self, request):
        search_keyword = request.GET.get('keyword', "")

        search_movies = Movies.objects.filter(title__icontains=search_keyword).order_by("-add_time")
        search_counts = Movies.objects.filter(title__icontains=search_keyword).order_by("-add_time").count()

        return render(request, 'home/search.html', {"search_movies": search_movies, "search_keyword": search_keyword,
                                                "search_counts": search_counts})
