import os
#配置mysql的参数
class Config:
    MYSQL_DIALECT='mysql'
    MYSQKL_DRIVER='pymysql'
    MYSQL_NAME='root'
    MYSQL_PWD='123456'
    MYSQL_HOST='localhost'
    MYSQL_PORT='3306'
    MYSQL_DB='shop_env'
    MYSQL_CHARSET='utf8mb4'
    SQLALCHEMY_DATABASE_URI=f'{MYSQL_DIALECT}+{MYSQKL_DRIVER}://{MYSQL_NAME}:{MYSQL_PWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?{MYSQL_CHARSET}'
    SQlALCHEMY_TRACK_MODIFICATIONS=True

    SECRET_KEY =os.urandom(16)
    #设置json数据不使用ascall
    JSON_AS_ASCII = False
    RESTFUL_JSON={"ensure_ascii":False}
    DEBUG=True
    #设置token的过期时间
    JWT_EXPIRATION_DELTA = 60 * 60 * 24 *7
    # 设置可以上传的图片类型
    ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif']
    # 获取当前项目的根路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # 设置图片上传的路径
    UPLOAD_FOLDER = os.path.join(BASE_DIR,'flask_shopping', 'static/upload')



class DevelopmentConfig(Config):
    #开发环境
    DEBUG=True
class ProductionConfig(Config):
    #生产环境
    pass
class TestingConfig(Config):
    #测试环境
    pass

config_map={
    'develop':DevelopmentConfig,
    'product':ProductionConfig,
    'test':TestingConfig
}