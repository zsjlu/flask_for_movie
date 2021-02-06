;
var common_ops = {
    buildUrl:function(path, params){
        var url = "" + path;
        var _params_url = ""
        if (params){
            _params_url = Object.keys( params).map(function(k){
                return [encodeURIComponent(k),encodeURIComponent(params[k])].join("=")
            }).join("&");
            _params_url = "?" + _params_url;
        }

        return url + _params_url;
    },

    alert: function(msg, callback){
        layer.alert(msg,{
            yes:function(index){
                if( typeof callback == "function"){
                    callback();
                }
                layer.close(index);
            }
        })
    }
};