/**
 * Created by Administrator on 2018/9/17.
 */

$(function () {
    template.defaults.imports.timeSince = function (dataValue) {
        var date = new Date(dataValue);
        var datets = date.getTime();
        var nowts = (new Date()).getTime();
        var timestamp = (datets - nowts)/1000;
        if(timestamp < 60){
            return '刚刚';
        }
        else if(timestamp >= 60 && timestamp < 60*60) {
            var minutes = parseInt(timestamp / 60);
            return minutes+'分钟前';
        }
        else if(timestamp >= 60*60 && timestamp < 60*60*24) {
            var hours = parseInt(timestamp / 60 / 60);
            return hours+'小时前';
        }
        else if(timestamp >= 60*60*24 && timestamp < 60*60*24*30) {
            var days = parseInt(timestamp / 60 / 60 / 24);
            return days + '天前';
        }else{
            // %Y/%m/%d %H:%M
            // JS是不支持这种日期格式化的
            var year = date.getFullYear();
            var month = date.getMonth();
            var day = date.getDay();
            var hour = date.getHours();
            var minute = date.getMinutes();
            return year+'/'+month+'/'+day+" "+hour+":"+minute;
        }
    };
});

// 加载更多
$(function () {
    var page = 2;
    var loadBtn = $('.load-more-btn');
    loadBtn.click(function (event) {
        event.preventDefault();

        duajax.get({
            'url': '/list/',
            'data': {
                'p':page
            },
            'success':function (result) {
                var newses = result['data'];
                if(newses.length>0){
                    var tpl = template("news-item",{"newses":newses});
                    var newsListGroup = $('.news-list-group');
                    newsListGroup.append(tpl);
                    page += 1;
                }else{
                    loadBtn.text('没有更多了。。。');
                    window.layer.msg('没有更多啦~');
                }
            }
        })
    })
});