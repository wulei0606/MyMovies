from django.urls import reverse

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View

from users.models import UserProfile
from .forms import LoginForm


#自定义登录验证,用于可以用邮箱或用户名登录
class CuseomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class IndexView(View):
    def get(self,request):
        return render(request,'home/index.html')

class LoginView(View):
    def get(self,request):
        return render(request,'home/login.html')
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")

            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, 'home/login.html', {"msg": "用户未激活"})
            else:
                return render(request, 'home/login.html', {"msg": "用户名或密码错误"})

        else:
            return render(request, 'home/login.html', {"login_form": login_form})

#退出
class LoginOutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))