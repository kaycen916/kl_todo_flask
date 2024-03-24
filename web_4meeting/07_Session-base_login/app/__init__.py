from flask import Flask, abort, render_template, request,jsonify, session, Blueprint

from flask_sqlalchemy import SQLAlchemy

from .config.config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # 設定config
    app.config.from_object(config[config_name])
    register_extensions(app)
    register_blueprints(app)

    @app.route('/')
    def index():
        # session['username'] = 'user1'
        # session['role'] = 'normal'
        # session['uid'] = '123456'
        # return session['username']
        return 'success'
    
    @app.route('/create_all')
    def create_db():
        db.create_all()
        # session['username'] = 'user2'
        # session['role'] = 'admin'
        # session['uid'] = '123456'
        # return session['username']
        return 'success'
    
    # # 判斷權限: normal
    # @app.route('/normal_member')
    # @check_login('normal')
    # def member_normal_page():
    #     name = session.get('username')
    #     role = session.get('role')
    #     uid = session.get('uid')
    #     return f'type: normal, {name}, {role}, {uid}'

    # # 判斷權限: admin
    # @app.route('/admin_member')
    # @check_login('admin')
    # def member_admin_page():
    #     name = session.get('username')
    #     role = session.get('role')
    #     uid = session.get('uid')
    #     return f'type: admin, {name}, {role}, {uid}'
    
    # 表格建立
    @app.route('/member_list')
    def member_list_page():        
        from .model.user import UserModel, UserSchema
        
        # 1
        # users = UserModel.query.all()
        # # return users # 不能直接return list
        # return render_template('member_list.html', users=users)

        # 2
        users = UserModel.query.all()
        schema = UserSchema(many=True) # 處理多個物件
        users_data = schema.dump(users) # 序列化成字典
        # return jsonify(users_data)
        return render_template('member_list.html', users=users_data)

        # 3
        # users = UserModel.query.with_entities(UserModel.uid, UserModel.name).order_by(UserModel.uid.asc()).all()
        # return render_template('member_list.html', users=users)

    return app

def register_extensions(app):
    db.init_app(app)

def register_blueprints(app):
    from .view.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

def check_login(check_role):
    def decorator(func):
        def wrap(*args, **kw):
            # 先檢查session
            user_role = session.get('role')
            print(user_role)
            print(type(user_role))

            if user_role == None or user_role =='':
                return abort(401)
            else:
                if check_role =='admin' and check_role == user_role:
                    return func(*args, **kw)
                if check_role == 'normal':
                    return func(*args, **kw)
                else:
                    return abort(401)
        wrap.__name__ = func.__name__
        return wrap
    return decorator