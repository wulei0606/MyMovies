from datetime import datetime

from django.db import models
from users.models import UserProfile
from movies.models import Movies
# Create your models here.

#评论
class Comment(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u"用户",on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies,verbose_name=u"电影",on_delete=models.CASCADE)
    content = models.CharField(max_length=255,verbose_name=u"评论内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"电影评论"
        verbose_name_plural = verbose_name

class Moviecol(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, verbose_name=u"电影", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"电影收藏"
        verbose_name_plural = verbose_name
