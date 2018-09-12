/**
 * Created by Administrator on 2018/9/11.
 */

// 点击刷新图形验证码
$(function () {
    var imgCaptcha = $('.img-captcha');
    imgCaptcha.click(function () {
        imgCaptcha.attr("src",'/account/img_captcha'+'?random='+Math.random());
    })
});

// 点击发送短信验证码
$(function () {
   var smsCaptcha = $('.sms-captcha-btn');
   smsCaptcha.click(function () {
        smsCaptcha.addClass('disabled');
        var telephone = $('input[name="telephone"]').val();
        $.get({
            'url': '/account/sms_captcha/',
            'data': {
                'telephone': telephone
            },
            'success': function (result) {
                var count = 60;
                var timer = setInterval(function () {
                    smsCaptcha.text(count);
                    count--;
                    if(count <= -1){
                        clearInterval(timer);
                        smsCaptcha.text('发送验证码');
                        smsCaptcha.removeClass('disabled');
                    }
                },1000);
                console.log('短信发送成功！');
            },
            'fail': function (error) {
                console.log('error');
            }
        });
   })
});

// 登录注册功能
// $(function () {
//
//    var telephoneI = $("input[name='telephone']");
//    var usernameI = $("input[name='username']");
//    var imgCaptchaI = $("input[name='img-captcha']");
//    var password1I = $("input[name='password1']");
//    var password2I = $("input[name='password2']");
//    var smsCaptchaI = $("input[name='sms-captcha']");
//    var submitBtn = $(".submit-btn");
//    submitBtn.click(function (event) {
//
//        event.preventDefault();
//        var telephone = telephoneI.val();
//        var username = usernameI.val();
//        var imgCaptcha = imgCaptchaI.val();
//        var password1 = password1I.val();
//        var password2 = password2I.val();
//        var smsCaptcha = smsCaptchaI.val();
//
//
//    });
// });