## MVC 优化

- flask_script自定义启动命令
- 多环境配置文件
- flask_debugtoolbar
- 错误处理器
- 请求拦截器

## MVC优化：自动以启动命令

    # application.py
    from flask_script import Manager
    
    manager = Manager(app)
    
    # manager.py
    from flask_script import Server
    
    manager.add_command("runserver", Server(host='0.0.0.0',
    use_debugger=True, use_reloader=True))
    
    manager.run()


添加其他命令

    from flask_script import Command
    
    @Command
    def create_all():
        from application import db
        from common.models.user import User
        db.create_all() 
        
    # 引入命令
    manager.add_command("create_all", create_all)
    
优化入口函数
    
    def main():
        manager.run()   
        
    if __name__ == "__main__":
        try:
            import sys
            sys.exit( main() )
        except Exception as e:
            import traceback
            traceback.print_exc() 
            
sys.exit()会引发一个异常：SystemExit，如果这个异常没有被捕获，那么python解释器将会退出。如果有捕获此异常的代码，那么这些代码还是会执行。捕获这个异常可以做一些额外的清理工作。0为正常退出，其他数值（1-127）为不正常，可抛异常事件供捕获。            

## MVC优化：多环境配置

- base_setting.py


    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENCODING = "utf8mb4"
- local_setting.py

    
    # 获取base_setting.py中的配置
    from config.base_setting import *

    SQLALCHEMY_DATABASE_URI = 'mysql://flask_for_movie:flask_for_movie@47.115.163.10/' \
                          'flask_for_movie'
                          
- production_setting.py


    # application.py
    app.config.from_pyfile("config/base_setting.py")
    # ops_config=local|production
    # linux export ops_config=local|production
    # windwos set ops_config=local|production
    
    if "ops_config" in os.environ:
        app.config.from_pyfile("config/%s_setting.py"%(\
        os.environ['ops_config']))                           

## Debug工具

    # www.py
    
    toolbar需要打开app.debug = True 和设置SECRET_KEY
    
    from flask_debugtoolbar import DebugToolbarExtension
    
    toolbar = DebugToolbarExtension(app) 
    
在base_setting中设置

    SECRET_KEY = "123456imooc"   
    
注意：
1.DEBUG=True才会生效
2.日志信息会显示到Logging中 

## 拦截器

新建intercept目录，在目录下新建Auth.py

    from application import app
    
    @app.before_request
    def before_request():
        app.logger.info("-------before--------")
        return
    
    @app.after_request
    def after_request(response):
        app.logger.info("-------after--------")
        return response   
在目录下新建errorHandler.py

    from application import app

    @app.errorhandler( 404 )
    def error_404( e ):
        return "404 not found"
在www.py中引入对应函数

    from intercepts.Auth import *
    from intercepts.errorHandler import *
    
## MVC目录定制
    |- application.py 全局变量类
    |- common
    |   |- libs
    |   |- models  数据库models类
    |- config 配置文件夹
    |- controllers MVC中的C层文件夹
    |      |-index.py 
    |- intercepts
    |      |- 拦截器
    |- manager.py 入口文件
    |- requirement.txt python扩展列表
    |- static 静态文件css，js，images存放文件夹
    |- templates 模板存放文件夹
    |      |- common
    |      |- index.html
    |-www.py 路由核心文件              