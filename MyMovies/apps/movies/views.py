from django.shortcuts import render

# Create your views here.
from django.views import View


class AnimationView(View):
    def get(self,request):
        return render(request,'home/animation.html')