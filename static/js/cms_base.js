$(function () {
    // http://127.0.0.1:8000/cms/staffs/
    var url = window.location.href;
    // http:
    var protocol = window.location.protocol;
    // 127.0.0.1:8000
    var host = window.location.host;
    var domain = protocol + '//' + host;
    var path = url.replace(domain,'');
    var menuLis = $(".sidebar-menu li");
    for(var index=0;index<menuLis.length;index++){
        var li = $(menuLis[index]);
        var a = li.children("a");
        var href = a.attr('href');
        if(href === path){
            li.addClass('active');
        }
    }
});