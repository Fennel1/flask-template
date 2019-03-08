"""
Flask 应用程序的配置文件。
* 可通过 `app.config[]` 在程序中引用这些配置。
"""

# 开发环境选项
DEBUG = True
LISTEN_HOST_DEV = r'0.0.0.0'
LISTEN_PORT_DEV = 26948

# 生产环境选项
LISTEN_HOST_PRODUCTION = r'0.0.0.0'
LISTEN_PORT_PRODUCTION = 26948

# Session
SECRET_KEY = r'xsa2Df323rUF9*EWFH&*h(dsa#Y(#&HDWDH(/,?RT'

# SQLAlchemy 数据库配置
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = r"mysql+pymysql://username:password@server:port/table?charset=utf8mb4"
