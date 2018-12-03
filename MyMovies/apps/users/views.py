from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import PageNotAnInteger, Paginator
from django.core.serializers import json
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from apps.utils.mixin_utils import LoginRequiredMixin

from users.models import UserProfile
from movies.models import Movies, Tag
from .forms import LoginForm, RegisterForm, UserInfoForm, ModifyPwdForm


# 自定义登录验证,用于可以用邮箱或用户名登录
class CuseomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 首页
class IndexView(View):

    def get(self, request,page):
        if not page:
            page = 1
        # 所有标签
        all_tag = Tag.objects.all()
        # 星级转换
        star_list = [(1, '1星'), (2, '2星'), (3, '3星'), (4, '4星'), (5, '5星')]
        all_star = map(lambda x: {'num': x[0], 'info': x[1]}, star_list)
        # 年份列表
        import time
        now_year = time.localtime()[0]
        year_range = [year for year in range(int(now_year) - 1, int(now_year) - 5, -1)]
        page_movies = Movies.objects
        selected = dict()
        # 获取链接中的标签id，0为显示所有
        tag_id = request.GET.get('tag_id', 0)
        if int(tag_id) != 0:
            page_movies = page_movies.filter(tag_id=tag_id)
        selected['tag_id'] = tag_id

        # 获取链接中的星级数字，0为显示所有
        star_num = request.GET.get('star_num', 0)
        if int(star_num) != 0:
            page_movies = page_movies.filter(star=star_num)
        selected['star_num'] = int(star_num)

        time_year = request.GET.get('time_year', 1)  # 1为所有日期，0为更早，月份为所选
        if int(time_year) == 0:
            page_movies = page_movies  # !!!没写这个功能
        elif int(time_year) == 1:
            page_movies = page_movies  # 所有年份的电影
        else:
            page_movies = page_movies.filter(release_time__year=time_year)  # 筛选年份
        selected['time_year'] = time_year

        play_num = request.GET.get('play_num', 1)  # 1为从高到低，0为从低到好
        if int(play_num) == 1:
            page_movies = page_movies.order_by('-playnum')
        else:
            page_movies = page_movies.order_by('playnum')
        selected['play_num'] = play_num

        comment_num = request.GET.get('comment_num', 1)  # 1为从高到低，0为从低到好
        if int(comment_num) == 1:
            page_movies = page_movies.order_by('-commentunm')
        else:
            page_movies = page_movies.order_by('commentunm')
        selected['comment_num'] = comment_num

        page_movies = Paginator(page_movies, 12)
        page_movies=page_movies.page(page)

        return render(request, 'home/index.html', {"all_tag": all_tag,
                                                   "all_star": all_star,
                                                   "now_year": now_year,
                                                   "year_range": year_range,
                                                   "selected": selected,
                                                   "page_movies": page_movies})


# 登录
class LoginView(View):

    def get(self, request):
        return render(request, 'home/login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")

            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'home/index.html')
                else:
                    return render(request, 'home/login.html', {"msg": "用户未激活", "login_form": login_form})
            else:
                return render(request, 'home/login.html', {"msg": "用户名或密码错误", "login_form": login_form})

        else:
            return render(request, 'home/login.html', {"login_form": login_form})


# 退出
class LoginOutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


# 邮箱注册用户
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'home/register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get("email", "")
            if UserProfile.objects.filter(email=email):
                return render(request, "home/register.html", {"msg": "邮箱已被注册", "register_form": register_form})
            pass_word = request.POST.get("password", "")
            user_name = request.POST.get("username", "")
            if UserProfile.objects.filter(username=user_name):
                return render(request, "home/register.html", {"msg": "用户名已存在", "register_form": register_form})
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = email
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            # send_register_email(user_name,"register")
            return render(request, "home/login.html")
        else:
            return render(request, "home/register.html", {"register_form": register_form})


# 用户中心
class UserInfoView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home/user.html', {})

    def post(self, request):
        userinfoform = UserInfoForm(request.POST, instance=request.user)
        if userinfoform.is_valid():
            userinfoform.save()
            return HttpResponseRedirect(reverse('userinfo'))
        else:
            return render(request, "home/user.html", {"userinfoform": userinfoform, "msg": "信息验证失败"})


# 修改密码
class PwdView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home/pwd.html', {})

    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            print(pwd1)
            print(request.user.password)
            if not check_password(pwd1, request.user.password):
                return render(request, 'home/pwd.html', {"msg": "旧密码错误"})
            if pwd2 == pwd1:
                return render(request, 'home/pwd.html', {"msg": "新密码与旧密码一致"})
            user = request.user
            user.password = make_password(pwd2)
            user.save()
            return render(request, 'home/pwd.html', {"msg": "密码修改成功"})
        else:
            pass
