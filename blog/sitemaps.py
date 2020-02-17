# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/2/16 20:42
# File   : sitemaps.py
# IDE    : PyCharm

from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    @staticmethod
    def lastmod(obj):
        return obj.updated
