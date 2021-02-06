;
var member_reg_ops={
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $(".reg_wrap .do-reg").click(function(){
            var btn_target = $(this);
            if( btn_target.hasClass("disabled")){
                common_ops.alert( "正在处理！！请不要重复点击~~");
                return;
            }
            var login_name = $(".reg_wrap input[name=login_name]").val();
            var login_pwd = $(".reg_wrap input[name=login_pwd]").val();
            var login_pwd2 = $(".reg_wrap input[name=login_pwd2]").val();
            if( login_name == undefined || login_name.length < 1){
                common_ops.alert( "请你输入正确的登陆用户名~~" );
                return ;
            }

            if( login_pwd == undefined || login_pwd.length < 6){
                common_ops.alert( "请你输入正确的登陆秘密，并且不能小于6个字符~~" );
                return ;
            }

            if( login_pwd2 == undefined || login_pwd2 != login_pwd){
                common_ops.alert( "请确认你的登陆秘密是否一致~~" );
                return ;
            }
            btn_target.addClass("disabled");
            $.ajax({
                url: common_ops.buildUrl("/member/reg"),
                type: "POST",
                data: {
                    login_name: login_name,
                    login_pwd:login_pwd,
                    login_pwd2: login_pwd2,
                },
                dataType: 'json',
                success: function( res ){
                    btn_target.removeClass("disabled");
                    var callback_ = null;
                    if( res.code == 200){
                        callback_ = function(){
                            window.location.href=common_ops.buildUrl("/");
                    };
                }
                common_ops.alert(res.msg, callback_);
            }
        });
    });
    }
};

$(document).ready(function(){
    member_reg_ops.init()
});