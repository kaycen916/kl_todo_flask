from flask import Flask, render_template, request, session, Blueprint, make_response
from flask_restful import Api, Resource, reqparse

from marshmallow import ValidationError

from ..model.user import UserModel, UserSchema
from .. import db
from .abort_msg import abort_msg

auth = Blueprint('auth', __name__)
api = Api(auth)

# users_schema = UserSchema()

class Signup(Resource):
    def post(self):
        try:
            # 資料驗證
            # request.form接收前端Form表單傳過來的帳密
            # Marshmallow中的users_schema.load進行驗證
            user_data = UserSchema().load(request.form, partial=True)

            # 註冊
            # 將驗證過後的帳密放入UserModel(user_data)，實例化新的使用者
            new_user = UserModel(user_data) #model裡已加密
            new_user.save_db() # 存入db
            new_user.save_session() # 設定session
            return {'msg': 'registrastion success'}, 200
        
        # 密碼少於 6 碼、或缺少帳號/密碼欄位
        except ValidationError as error:
            return {'errors': error.messages}, 400
        # 其他錯誤
        except Exception as e:
            return {'errors': abort_msg(e)}, 500 # 將錯誤訊息清理過後回覆給前端
    def get(self):
        return make_response(render_template('signup.html'))

class Login(Resource):
    def post(self):
        try:
            # 資料驗證
            user_data = UserSchema().load(request.form)
            name = user_data['name']
            password = user_data['password']

            # 登入
            query = UserModel.get_user(name)
            if query != None and query.verify_password(password):
                query.save_session()
                return {'msg': 'ok'}, 200
            else:
                return {'errors': 'incorrect username or password'}, 400
        except ValidationError as error:
            return {'errors': error.messages}, 400

        except Exception as e:
            return {'errors': abort_msg(e)}, 500
    
    def get(self):
        return make_response(render_template('login.html'))

class Logout(Resource):
    def get(self):
        UserModel.remove_session()
        return {'msg': 'logout'}, 200

class Modify(Resource):
    def post(self):
        try:
            user_data = UserSchema().load(request.form)
            name = user_data['name']
            password = user_data['password'] # 新密碼
            
            if name not in session['username']:
                return {'errors': 'User not logged in'}, 401

            user = UserModel.get_user(name)
            if user:
                user.password = password
                db.session.commit() # 更新資料庫
                return {'msg': 'Password updated successfully'}, 200
            else:
                return {'errors': 'User not found'}, 404
        except:
            return
    def get(self):
        return make_response(render_template('modify.html'))

api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(Modify, '/modify')