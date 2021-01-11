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

linxu安装python3.7.3
=====
•	Linux环境安装

-    yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel  mysql-devel gcc gcc-devel python-devel  
-    wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz    
- 或wget http://npm.taobao.org/mirrors/python/3.7.3/Python-3.7.3.tgz    
-    tar -zxvf Python-3.7.3.tgz
-    mkdir /usr/local/python3
-    cd Python-3.7.3 
-    ./configure --prefix=/usr/local/python3
-    make && make install
-    ln -s /usr/local/python3/bin/python3 /usr/bin/python3
