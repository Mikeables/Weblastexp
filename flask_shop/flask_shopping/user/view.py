from flask_shopping.user import user,user_api
from flask_cors import CORS
from flask_shopping.user import models
from flask_shopping import db
from flask import request, Flask, jsonify
from flask_restful import Resource,reqparse
from flask_shopping.utils import message
from flask_shopping.utils.tokens import generate_token,verify_token,login_required

app = Flask(__name__)
CORS(app)  # 启用 CORS

import re
@user.route('/')
def index():
    return "User Hellso"

class Users(Resource):
    def get(self):
        #创建RequestParser对象
        parser = reqparse.RequestParser()
        #增加参数
        parser.add_argument('pnum',type = int,default=1,location='args')
        parser.add_argument('psize',type=int,default=10,location='args')
        parser.add_argument('name',type=str,location='args')
        #解析参数
        args = parser.parse_args()
        #获取里面的数据
        name = args.get('name')
        pnum = args.get('pnum')
        psize = args.get('psize')
        #判断是否传递了name
        if name:
            #获取用户列
            user_list = models.User.query.filter(models.User.name.like(f'%{name}%')).paginate(page = pnum,per_page = psize)
        else:
            #获取用户列表
            user_list = models.User.query.paginate(page=pnum,per_page=psize)
        data = {
            'total':user_list.total,
            'pnum':pnum,
            'data':[u.to_dict() for u in user_list.items]

        }
        return {'status':200,'msg':'获取用户列表成功','data':data}
    
    def post(self):
        #注册用户
        #接受用户信息
        name = request.get_json().get('name')
        pwd  = request.get_json().get('pwd')
        real_pwd  = request.get_json().get('real_pwd')
       
        #验证数据的正确性
        if not all([name,pwd]):
            return message.to_dict_msg(10000)
        if pwd != real_pwd:
            return message.to_dict_msg(10013)
        if len(name)<2:
            return message.to_dict_msg(10011)
        
        
        nick_name = request.get_json().get('nick_name')
        email = request.get_json().get('email')
        phone = request.get_json().get('phone')

        if not re.match(r'1[345678]\d{9}',phone):
            return message.to_dict_msg(10014)
        if not re.match(r'^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',email):
            return message.to_dict_msg(10015)
        #接受角色id信息
        role_id = request.get_json().get('role_id')
        
        try:
            #判断用户名是否存在
            user = models.User.query.filter(models.User.name == name).first()
            if user:
                return {'status':400,'msg':'用户名已存在'}
        except Exception as e:
            print(e)

        #创建用户对象
        #判断是否传递了角色id
        if role_id:
            user = models.User(name=name,password=pwd,phone=phone,email=email,nick_name=nick_name,role_id=role_id)
        else:
             user = models.User(name=name,password=pwd,phone=phone,email=email,nick_name=nick_name)
        db.session.add(user)
        db.session.commit()
        return {'status':200,'msg':'增加成功了'}
user_api.add_resource(Users,'/users/')

class User(Resource):
    def get(self,id):
        user = models.User.query.get(id)
        if user:
            return {'status': 200, 'msg': '查询成功', 'data': user.to_dict()}
        else:
            return {'status':404,'msg':'用户不存在'}


    def put(self,id):
        try:
            user = models.User.query.get(id)
            paser = reqparse.RequestParser()
            paser.add_argument('nick_name',type = str)
            paser.add_argument('phone',type = str)
            paser.add_argument('email',type = str)
            #增加角色id
            paser.add_argument('role_id',type = int)
            args = paser.parse_args()
            if args.get('nick_name'):
                user.nick_name = args.get('nick_name')
            if args.get('phone'):
                user.phone = args.get('phone')
            if args.get('email'):
                user.email = args.get('email')
            #判断是否传递了角色id
            if args.get('role_id'):
                user.role_id = args.get('role_id')
            
            db.session.commit()
            return {'status':200,'msg':'修改成功','data':user.to_dict()}
        except Exception as e:
            print(e)
            return {'status':400,'msg':'修改成功'}


    def delete(self,id):
        try:
            user = models.User.query.get(id)
            if user:
                db.session.delete(user)
                db.session.commit()
                
            return {'status':200,'msg':'删除成功'}
            
        except Exception as e:
            print(e)
            return {'status':400,'msg':'删除失败'}

user_api.add_resource(User,'/user/<int:id>/')


@user.route('/login', methods=['POST'])
def login():
    # 获取用户名
    name = request.get_json().get('name')  # content-type:application/json
    # 获取密码
    pwd = request.get_json().get('pwd')
    # 判断是否传递数据完整
    if not all([name, pwd]):
        return jsonify({'status': 10000, 'msg': '数据不完整'})
    else:
        # 通过用户名获取用户对象
        user = models.User.query.filter_by(name=name).first()
        # 判断用户是否存在
        if user:
            if user.check_password(pwd):
                # 生成一个token
                token = generate_token({'id': user.id})
                return jsonify({'status': 200, 'msg': '登录成功', 'data': {'token': token}})
    return jsonify({'status': 10001, 'msg': '用户名或密码错误'})
if __name__ == '__main__':
    app.run(debug=True)


@app.route('/verify', methods=['GET'])
def verify_user():
    name = request.args.get('name')
    pwd = request.args.get('pwd')
    
    if not all([name, pwd]):
        return jsonify({'status': 10000, 'msg': '数据不完整'})
    
    user = models.User.query.filter_by(name=name).first()
    
    if user and user.check_password(pwd):
        return jsonify({'status': 200, 'msg': '用户验证成功'})
    else:
        return jsonify({'status': 10001, 'msg': '用户名或密码错误'})

if __name__ == '__main__':
    app.run(debug=True)

@user.route('/reset_pwd/<int:id>/')
def rest_pwd(id):
    try:
        #根据id 获取用户信息
        user = models.User.query.get(id)
        #重置密码
        user.password = '123456'
        #提交事务
        db.session.commit()
        return {'status':200,'msg':'重置密码成功 密码为:123456'}

    except Exception as e:
        print(e)
        return {'status':400,'msg':'重置密码失败'}

@user.route('/test/')
@login_required
def test_login_required():
    return {'status': 200, 'msg': '验证成功'}