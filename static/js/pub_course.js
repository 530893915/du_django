$(function () {
    window.ue = UE.getEditor('editor',{
        'serverUrl': '/ueditor/upload/'
    });
});

$(function () {
    var submitBtn = $('#submit-btn');
    submitBtn.click(function (event) {
        event.preventDefault();

        var title = $("#title-input").val();
        var category_id = $("#category-select").val();
        var teacher_id = $("#teacher-select").val();
        var video_url = $("#video-input").val();
        var cover_url = $("#cover-input").val();
        var price = $("#price-input").val();
        var duration = $("#duration-input").val();
        var profile = window.ue.getContent();

        duajax.post({
            'url': '/cms/pub_course/',
            'data': {
                'title': title,
                'category_id': category_id,
                'teacher_id': teacher_id,
                'video_url': video_url,
                'cover_url': cover_url,
                'price': price,
                'duration': duration,
                'profile': profile
            },
            'success': function (result) {
                if(result['code'] === 200){
                    xfzalert.alertSuccessToast('发布成功！');
                    window.location = window.location.href;
                }
            }
        });
    });
});