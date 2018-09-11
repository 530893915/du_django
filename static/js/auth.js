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