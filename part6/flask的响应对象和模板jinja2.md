## flask响应请求

    - text/html
    
    - Json
    
    - 模板响应
    
### 响应html

        @index_page.route("/")
        def index():
            return "index page"
            
        @index_page.route("same")
        def index_same():
            response = make_response("index page", 200)
            return response
         
### 响应json

        @index_page.route("json")
        def index_json():
            import json
            data = {"a":"b"}
            response = make_response(json.dumps(data))
            response.headers['Content-Type'] = 'application/json'
            return response
            
        @index_page.route("json_same")
        def index_json_same()
            data={"a":"b"}
            # jsonify会默认进行序列化和添加json头部信息
            response = make_response(jsonify(data))
            return response


        # 默认查找当前目录下templates目录下的html文件,jinja2模板
        @index_page.route("/template")
        def template():
        return render_template("index.html")
        
## JinJa2 模板语法详情讲解

传递变量

    @index_page.route("/")
    def index():
        name = "imooc"
        return render_template("index.html", name=name)
       
    @index_page.route("/same")
    def index_same():
        name = "imooc"
        context = {"name": name}
        return render_template("index.html", **context)
        
Jinja2显示变量

    <p>var name = {{ anme }} </p>  

Jinja2基本语法

- 判断if
- 循环for
- 模板继承
  
    
    <p>
    {% if user %}
        {{user.nickname}} {{user.qq}}{{user.home_page}}
        {%endif%}
    </p>
    
    <p>
        {% for tmp_num in num_list %}
        {{ tmp_num }}
        {% endfor %}
    </p>
 
Jinja2模板继承




     
            
        