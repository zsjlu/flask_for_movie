uwsgi --http-socket :5000 --wsgi-file manager.py --callable app --ocesses 4 --threads 2


## uwsgi使用
    
    [uwsgi]
    chdir=/home/flask_for_movie/part9/9.4
    # 指定项目目录
    http=0.0.0.1:82
    # 指定监听ip和端口
    module=manager
    # 指定模块
    callable=app
    # 该对象就是一个wsgi接口，如Flask中的app
    master=true
    # 使用主进程管理其他进程
    processes=4
    pidifle=/tmp/logs/movie.pid
    # 指定pid文件
    daemonize=/tmp/logs/movie.log
    # 使进程在后台运行，并将日志打到指定的日志文件或者udp服务器
    static-map=/static=/home/www/part9/9.4/static
    # 静态资源映射以加快请求速度

使用以下命令以命令行的方式启动uwsgi

    uwsgi --ini uwsgi.ini  
    
查看进程

    ps -ef | grep uwsgi
    
重启服务

1.

    uwsgi --stop /tmp/logs/movie.pid
    
    uwsgi --ini uwsgi.ini
    
2.

                  