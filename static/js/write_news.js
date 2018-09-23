/**
 * Created by Administrator on 2018/9/16.
 */
// 将文件上传到我们自己的服务器的代码
/*
$(function () {
    var uploadBtn = $("#upload-btn");
    uploadBtn.change(function (event) {
        var file = this.files[0];
        var formData = new FormData();
        formData.append('upfile', file);

        duajax.post({
            'url': '/cms/upload_file/',
            'data': formData,
            'processData': false,
            'contentType': false,
            'success': function (result) {
                if (result['code'] === 200) {
                    var url = result['data']['url'];
                    var thumbnailInput = $("input[name='thumbnail']");
                    thumbnailInput.val(url);
                }
            }
        });
    });
});
*/

// 上传文件到七牛
$(function () {
    // progressGroup：用来控制整个进度条是否需要显示的
    var progressGroup = $("#progress-group");
    // progressBar：用来控制这个进度条的宽度
    var progressBar = $(".progress-bar");

    function progress(response) {
        var percent = response.total.percent;
        var percentText = percent.toFixed(0) + '%';
        progressBar.css({"width":percentText});
        progressBar.text(percentText);
    }

    function error(err) {
        window.xfzalert.alertErrorToast(err.message);
        progressGroup.hide();
    }

    function complete(response) {
        // hash key
        var key = response.key;
        var domain = 'http://pd0p68u4u.bkt.clouddn.com/';
        var url = domain + key;
        var thumbnailInput = $("input[name='thumbnail']");
        thumbnailInput.val(url);
        window.xfzalert.alertSuccessToast('图片上传成功！');
        progressGroup.hide();
        progressBar.css({"width":'0'});
        progressBar.text('0%');
    }

    var uploadBtn = $("#upload-btn");
    uploadBtn.change(function () {
        var file = this.files[0];
        duajax.get({
            'url': '/cms/qntoken/',
            'success': function (result) {
                if(result['code'] === 200){
                    var token = result['data']['token'];
                    var key = file.name;
                    var putExtra = {
                        fname: key,
                        params: {},
                        mimeType: ['image/png', 'image/jpeg', 'image/gif']
                    };
                    var config = {
                        useCdnDomain: true,
                        region: qiniu.region.z0
                    };
                    var observable = qiniu.upload(file,key,token,putExtra,config);
                    observable.subscribe({
                        'next': progress,
                        'error': error,
                        'complete': complete
                    });
                    progressGroup.show();
                }

            }
        })
    })
});


// ueditor
$(function () {
    window.ue = UE.getEditor('editor',{
        'initialFrameHeight': 400,
        'serverUrl': '/ueditor/upload/'
    });
});

// 发布新闻
$(function () {
    var submitBtn = $('#submit-btn');
    submitBtn.click(function (event) {
        event.preventDefault();
        var btn = $(this);
        var title = $("input[name='title']").val();
        var desc = $("input[name='desc']").val();
        var category = $("select[name='category']").val();
        var thumbnail = $("input[name='thumbnail']").val();
        var content = window.ue.getContent();
        var news_id = btn.attr('data-news-id');
        var url = '';
        if(news_id){
            url = '/cms/edit_news/';
        }else{
            url = '/cms/write_news/';
        }

        duajax.post({
            'url': url,
            'data': {
                'title': title,
                'desc': desc,
                'category': category,
                'thumbnail': thumbnail,
                'content': content,
                'pk': news_id
            },
            'success': function (result) {
                if(result['code']===200){
                    xfzalert.alertSuccess('发表成功！',function () {
                        window.location.reload();
                    })
                }else{
                    xfzalert.alertErrorToast(result['message']);
                }
            }
        })
    })
});