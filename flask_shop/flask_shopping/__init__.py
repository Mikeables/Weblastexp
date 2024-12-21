from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_map
from flask_cors import CORS
db = SQLAlchemy()

def create_app(config_name):
    #创建app实例
    app =Flask(__name__)
    #根据config_name获取配置类
    obj=config_map.get(config_name)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/shop_env'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 添加这一行
    #根据配置类加载配置信息
    app.config.from_object(obj)
    #初始化db
    db.init_app(app)
    CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})  # 配置 CORS
    
    #获取user蓝图对象
    from flask_shopping.user import user
    app.register_blueprint(user)
    from flask_shopping.menu import menu_bp
    #获取menu蓝图对象
    app.register_blueprint(menu_bp)
    #获取role蓝图对象
    from flask_shopping.role import role_bp
    #注册蓝图
    app.register_blueprint(role_bp)
    #获取category蓝图对象
    from flask_shopping.category import cate_bp
    app.register_blueprint(cate_bp)
    #获取attribute蓝图对象
    from flask_shopping.category import attr_bp
    app.register_blueprint(attr_bp)

    #获取product蓝图对象
    from flask_shopping.product import product_bp
    app.register_blueprint(product_bp)

    #获取order蓝图对象
    from flask_shopping.order import order_bp
    app.register_blueprint(order_bp)

    #返回flask app实例
    return app



