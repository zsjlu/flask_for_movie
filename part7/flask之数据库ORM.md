##flask结合SQLAlchemy打通数据库通讯

Flask-SQLAlchemy

安装

    pip install flask_sqlalchemy
    pip install mysqlclient # win10可能安装不了

数据库配置

    from flask_sqlalchemy import SQLAlchemy
    
    app.config['SQLALCHEMY_DATABASE_URI']=
    'mysql://root:123456@127.0.0.1/mysql'
    db = SQLAlchemy(app)

Flask查询数据库

    from sqlalchemy import text
    sql = text("select * from `user`")
    result = db.engine.execute(sql)
    context['result'] = result
    
    <p>
        {% for item in result %}
        {{ item['b'] }}
        {% endfor %}
    </p>

循环引用
    
    局部引用解决

application拆分为三个文件

- 启动文件 manager.py
    
    - 注意加入 from www import *，这manager.py才可以找到app
    
- 核心配置文件 application.py
- 路由注册文件 www.py
    
    
    
    
    
##通过Model访问数据

案例
    
    # 生成数据表
    from application import db
    
    class User(db.Model):
        Host = db.Column(db.String(80),primary_key=True)
        User = db.Column(db.String(120))

    # 访问数据表
    from common.models.user import User
    
    result = User.query.all()
    context['result'] = result
    
杀掉python进程

    ps -ef|grep python
    
    kill -9 pid
    
问题：

- models中的字段类型定义为python类型，注意与数据库对应
    
    
    

##自动生成model


***都需要先设计数据库***


一、自动生成model

    flask-sqlacodegen
    
        -pip install flask-sqlacodegen
        

        flask-sqlacodegen 'mysql://flask_for_movie:flask_for_movie@47.115.163.10/flask_for_movie'\
        --tables user --outfile "common/models/user.py" --flask
        
二、通过model生成数据库表

- 在协同开发时使用
- 自己app发布，在生产上建立表结构
- 在manager.py的入口函数添加下面的代码，并设置选择迁移的库的名字



    from common.models.user import User
    from application import db
    
    db.Model = User
    db.create_all()  
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask_for_movie:flask_for_movie@47.115.163.10/' \
                                        'flask_for_movie'
    db = SQLAlchemy(app) 
    
Tips:

- 链接执行路径：ln -s /usr/local/python3/bin/flask-sqlacodegen /usr/local/bin   
    