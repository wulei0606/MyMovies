from django.db import models
from datetime import datetime


# Create your models here.


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"标签名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 电影
class Movies(models.Model):
    title = models.CharField(max_length=15, verbose_name=u"电影标题")
    url = models.FileField(upload_to="movies/%Y/%m",verbose_name=u"资源文件",max_length=100)
    desc = models.CharField(max_length=300, verbose_name=u"电影简介")
    logo = models.ImageField(upload_to="logo/%Y/%m", verbose_name=u"封面图", max_length=100)
    star = models.SmallIntegerField(verbose_name=u"星级")
    playnum = models.BigIntegerField(verbose_name=u"播放量")
    commentunm = models.BigIntegerField(verbose_name=u"评论量")
    tag_name = models.ForeignKey(Tag, verbose_name=u"所属标签", null=True, on_delete=models.CASCADE)
    area = models.CharField(max_length=20, verbose_name=u"上映地区")
    release_time = models.DateTimeField(default=datetime.now, verbose_name=u"上映时间")
    length_time = models.CharField(max_length=100, verbose_name=u"播放时间")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"电影"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 上映预告
class Preview(models.Model):
    title = models.CharField(max_length=15, verbose_name=u"电影标题")
    logo = models.ImageField(upload_to="preview/%Y/%m", verbose_name=u"封面图", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"上映预告"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
