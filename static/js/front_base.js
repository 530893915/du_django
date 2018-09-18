$(function () {
    if(template){
        template.defaults.imports.timeSince = function (dateValue) {
            var date = new Date(dateValue);
            var datets = date.getTime(); // 都是毫秒/秒，相差10000倍
            var nowts = (new Date()).getTime();
            var timestamp = (nowts-datets)/1000;
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
    }
});