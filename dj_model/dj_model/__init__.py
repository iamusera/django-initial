import pymysql


# 自带的mysqlDB连接池有问题，超过数据库默认时间之后，不会自动重连
pymysql.install_as_MySQLdb()
