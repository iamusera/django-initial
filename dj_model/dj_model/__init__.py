# import pymysql
#
#
# # 自带的mysqlDB连接池有问题，超过数据库默认时间之后，不会自动重连
# pymysql.install_as_MySQLdb()


# 导入pip3 install pymysql==0.7.11
# 启动服务器出现以下错误
# raise ImproperlyConfigured("mysqlclient 1.3.3 or newer is required; you have %s" % Database.__version__)
# django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.3 or newer is required; you have 0.7.11.None
# 解决方案
# 到D:\Program Files\Python36\Lib\site-packages\Django-2.0.6-py3.6.egg\django\db\backends\mysql
# 文件下的base.py文件中，将以下内容注释掉
# # version = Database.version_info
# # if version < (1, 3, 3):
# # raise ImproperlyConfigured("mysqlclient 1.3.3 or newer is required; you have %s" % Database.__version__)
#
# 将(1, 3, 3) 版本信息更改也是可以解决的