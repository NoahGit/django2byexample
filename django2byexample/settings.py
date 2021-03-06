"""
Django settings for django2byexample project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r5jk8_-poh!e&nsyetdx7$f%pbbt-(nzj1=j)obmm(y)*g-ky-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = "*"

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'taggit',
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django2byexample.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django2byexample.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# 向控制台写入邮件，用于程序测试，将所有邮件输出到shell中
# EMALL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# 没有本地SMTP服务器，用邮件服务提供商的SMTP服务器
# 昨天遇到一个问题，pycharm 中运行不了django的程序，看错误是：
# django.core.exceptions.ImproperlyConfigured: Requested setting CACHES,
# but settings are not configured. You must either define the environment variable
# DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
# 结果百度了半天没结果，最后还是在 老外的网站上找到了答案。
# 本来django项目在 python shell 中可以完美运行，在pycharm里面就不行，
# 原因是pycharm 要你配置一个  环境变量  DJANGO_SETTINGS_MODULE
# 这个变量告诉django项目去找哪一个settings 文件。  具体的步骤：
# 1、Run  -->  EditConfigures
# 2、找到python一项  具体名字是 Python tests（注意不是django那一个），
# 然后修改里面的Environment variables 添加一项。名称是DJANGO_SETTINGS_MODULE
# 值是你的settings,比如 mysite.settings 。

EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = 'xiangjiaotuobei@163.com'  # 填写你的邮件地址
EMAIL_HOST_PASSWORD = 'gaoyong1983'  # 邮箱的smtp授权码
EMAIL_PORT = 25
EMAIL_USE_TLS = True

