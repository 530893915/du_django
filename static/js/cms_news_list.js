/**
 * Created by Administrator on 2018/9/23.
 */

$(function () {
    var todayDate = new Date();
    var todayStr = todayDate.getFullYear() + '/' + (todayDate.getMonth()+1) + '/' + todayDate.getDate();
    var options = {
        'showButtonPanel': true,
        'format': 'yyyy/mm/dd',
        'startDate': '2018/9/1',
        'endDate': todayStr,
        'language': 'zh-CN',
        'todayBtn': 'linked',
        'todayHighlight': true,
        'clearBtn': true,
        'autoclose': true
    };
    // 初始化开始日期
    $("input[name='start']").datepicker(options);
    // 初始化截止日期
    $("input[name='end']").datepicker(options);

});
