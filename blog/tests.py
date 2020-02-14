from django.test import TestCase

# Create your tests here.

from django.core.mail import send_mail
send_mail('工作日报', '非常重要的工作日报，周一必须处理！不得延误！',
          'xiangjiaotuobei@163.com', ['xiangjiaotuobei@163.com', '42967148@qq.com', 'c5t4v@163.com'],
          fail_silently=False)

# 发邮件的时候必须抄送上自己的邮箱，不然会报错554 DT:SPM 错误。
# 20200214测试github上传。
