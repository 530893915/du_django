/**
 * Created by Administrator on 2018/9/11.
 */
$(function () {
    var imgCaptcha = $('.img-captcha');
    imgCaptcha.click(function () {
        imgCaptcha.attr("src",'/account/img_captcha'+'?random='+Math.random());
    })
});