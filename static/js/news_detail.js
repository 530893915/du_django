/**
 * Created by Administrator on 2018/9/18.
 */

$(function () {
    var submitBtn = $('#submit-comment-btn');
    var textarea = $('.comment-textarea');
    submitBtn.click(function () {

        var content = textarea.val();
        var news_id = submitBtn.attr('data-news-id');

        duajax.post({
            'url': '/add_comment/',
            'data': {
                'content': content,
                'news_id': news_id
            },
            'success': function (result) {
                if (result['code'] === 200) {
                    var comment = result['data'];
                    var tpl = template('comment-item', {'comment': comment});
                    var commentGroup = $('.comment-list-group');
                    commentGroup.prepend(tpl);
                    window.layer.alert('评论成功！', {icon: 6});
                    textarea.val('');
                } else {
                    window.layer.tips(result['message'], '#submit-comment-btn',{anim: 6,tips: [4, '#cc3a2e'], time: 4000});
                }
            }
        });
    })
});
