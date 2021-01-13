## Flask 路由注册

- app.route 和 app.add_url_rule
- 蓝图

## 解读HTTP请求流程

- 浏览器如何完成整个HTTP请求？

    - 客户端-》域名服务器-》客户端-》web服务器-》客户端（三次握手）
   
    - 客户端 - web服务 - 后端服务器
    
## 获取请求对象的GET和POST参数

  - get
    
        @index_page.route("get")
        def get():
            var_a = requtest.args.get("a", "")
            return "request:%s,params:%s,var_a:%s"\
            %(request.method, request.args, var_a)
  - post
  
         @index_page.route("post",methods=["POST"])
         def post():
            var_a = request.form['a']if 'a' in request.form else ""
            return "request:%s,params:%s,var_a:%s" %\
            (request.method, request.form, var_a)
    
    测试工具
    
      - postman
      
    POST上传文件
        
        @index_page.route("/upload", methods=["POST"])
        def upload():
            f = request.files['file'] if 'file' in request.files else None
            return "request:%s,params:%s,f:%s" % \
           (request.method, request.files, f)
              
   POST上传文件注意事项：enctype="multipart/form-data"
   
   request.value既可以获取到post参数又可以获取get参数
   
    @cached_property
    def values(self):
        """A :class:`werkzeug.datastructures.CombinedMultiDict` that combines
        :attr:`args` and :attr:`form`."""
        args = []
        for d in self.args, self.form:
            if not isinstance(d, MultiDict):
                d = MultiDict(d)
            args.append(d)
        return CombinedMultiDict(args)

curl 方法测试接口

    - 从新打开一个终端
    - get
        - curl "http://192.168.0.105:5000/imooc/get"

    - post
        - curl "http://192.168.0.105:5000/imooc/get？a=b"

    - upload        
        - curl -X POSThttp://192.168.0.105:5000/imooc/upload-H 'content-type:multipart/form-data'-F 'file=@/home/www/ppt5/5.3/indexController.py'


 
        
