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


$(function () {
    var deleteBtns = $(".delete-btn");
    deleteBtns.click(function () {
        var pk = $(this).attr('data-news-id');
        xfzalert.alertConfirm({
            'text': '您确定要删除这篇新闻吗？',
            'confirmCallback': function () {
                duajax.post({
                    'url': '/cms/delete_news/',
                    'data': {
                        'pk': pk
                    },
                    'success': function (result) {
                        if(result['code'] === 200){
                            // window.location.reload();
                            window.location = window.location.href;
                            window.xfzalert.alertSuccessToast('删除成功！');
                        }
                    }
                });
            }
        })
    });
});
