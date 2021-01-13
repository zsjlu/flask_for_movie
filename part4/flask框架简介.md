# 启动服务方法
## linux

export FLASK_APP=index_1.py

ln -s 

flask run

## windows

set FLASK_APP=index_1.py

flask run

### 配置启动主机可以访问

参数 --host 0.0.0.0

app.run(host = "0.0.0.0", debug=True)

## Werkzeug 
是一个WSGI工具包，也可以作为一个Web框架的底层库

## CGI FastCGI WSGI UWSGI uwsgi

CGI(Common Gateway Interface):通用网关接口是一种重要的
互联网技术，可以让一个客户端，从网页浏览器向执行在网络服务器
上的程序请求数据。CGI描述了服务器和请求处理程序之间传输数据
的一种标准。定义了客户端服务器之间如何传数据。

FastCGI(Fast Common Gateway Interface)是一种让交互程序
与Web服务器通信的协议。FastCGI是早期通用网关接口（CGI）的增强
版本。FastCGI致力于减少网页服务器与CGI程序之间互动的开销，从而
使服务器可以同时处理更多的网页请求。我们常见的Nginx、Apache都
有实现该协议

WSGI：Web服务器网关接口（Python Web Server Gateway Interface，
缩写为WSGI）是为Python语音定义的Web服务器和Web应用程序或框架
之间的一种简单而通用的接口。自从WSGI被开发出来以后，许多其他语言
中也出现了类似接口。为python定义的web服务器和web框架之间的接口
标准。

uWSGI:一个Web Server，即一个实现了WSGI的服务器

uwsgi:一个uWSGI服务器实现的独有的协议

## Flask 配置

- 网络配置：
  - app.run()和app.run（host=0.0.0.0）
  - 127.0.0.1和0.0.0.0的区别

- Flask配置加载方式--变量配置
  - app.config['DEBUG'] = True
  - app.config.update(DEBUG=Ture, SECRET_KEY='...') # 更新配置
   
- Flask配置加载方式--模块配置
  - app.config.from_object('config.base_setting')

- Flask配置加载方式--环境变量配置 
    
  - app.config.from_envvar('ops_config')
    
  - windows用set，linux用export
    
- Flask配置加载方式--文件配置

  - app.config.from_pyfile('config/base_setting.py')
  - 主要使用方式
  


 
