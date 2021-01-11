技术选型
====
* python3
* Flask
* MySQL
* Bootstrap
* jQuery

虚拟机
======
virtualbox：centos7_node

IP:192.168.0.105

网络
=====
ASIX AX88772C USB2.0 to Fast Ethernet Adapter

centos安装python3.7.3
=====
•	Linux环境安装

-    yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel  mysql-devel gcc gcc-devel python-devel  
-    wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz    

    或wget http://npm.taobao.org/mirrors/python/3.7.3/Python-3.7.3.tgz    

-    tar -zxvf Python-3.7.3.tgz
-    mkdir /usr/local/python3
-    cd Python-3.7.3 
-    ./configure --prefix=/usr/local/python3
-    make && make install

    在centos下安装python3.7.0以上版本时报错ModuleNotFoundError: No module named '_ctypes'的解决办法
	yum install libffi-devel

-    ln -s /usr/local/python3/bin/python3 /usr/bin/python3

linux 安装 virtualenv和virtualenvwrapper
=====

- 安装pip3 和 virtualenv

    - [pip源配置](https://www.cnblogs.com/bigb/p/12146418.html)
    - ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
    - pip3 install virtualenv
    - ln -s /usr/local/python3/bin/virtualenv /usr/bin/virtualenv
    - virtualenv -p /usr/bin/python3  vir_python3


- [virtualenvwrapper](https://www.cnblogs.com/VinsonYang/p/12333079.html)
    
    - 基本使用
    - workon 列出或使用某个虚拟换环境
    - deactivate 退出
    - mkvirtualenv 建虚拟环境
    - rmvirtualenv 删除虚拟环境
    
虚拟机Centos如何和主机共享目录
===========

[请查看word文档](https://www.cnblogs.com/zsjlovewm/p/14265182.html)