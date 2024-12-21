from flask_shopping import create_app, db
from flask_migrate import Migrate
from flask_script import Manager
from flask_cors import CORS
from flask_shopping.user.models import User  # Import the User model

app = create_app('develop')
CORS(app, supports_credentials=True)  # 解决跨域问题
manager = Manager(app)
migrate = Migrate(app, db)
#manager.add_command('db', MigrateCommand)  # 移除这行

@app.route('/test_db_connection')
def test_db_connection():
    try:
        # 尝试查询数据库中的用户
        user = User.query.first()
        if user:
            return f'数据库连接成功，用户: {user.name},密码:{user.password}'
        else:
            return '数据库连接成功，但没有找到用户'
    except Exception as e:
        return f'数据库连接失败: {e}'
    
@app.route('/check_user/<username>/<password>')
def check_user(username, password):
    try:
        user = User.query.filter_by(name=username).first()
        if user and user.check_password(password):
            return f'用户 {username} 存在，密码正确'
        elif user:
            return f'用户 {username} 存在，但密码错误'
        else:
            return f'用户 {username} 不存在'
    except Exception as e:
        return f'检查用户时出错: {e}'
    
@app.route('/get_user_password/<username>')
def get_user_password(username):
    try:
        user = User.query.filter_by(name=username).first()
        if user:
            return f'用户 {username} 的密码是: {user.password}'
        else:
            return f'用户 {username} 不存在'
    except Exception as e:
        return f'获取用户密码时出错: {e}'

if __name__ == '__main__':
    app.run()
    # manager.run()