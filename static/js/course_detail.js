/**
 * Created by Administrator on 2018/9/24.
 */


$(function () {
    var span = $(".video-container span");
    var video_url = span.attr("data-video-url");
    var cover_url = span.attr('data-cover-url');
    var course_id = span.attr('data-course-id');
    var player = cyberplayer("playercontainer").setup({
        width: '100%',
        height: '100%',
        file: video_url,
        image: cover_url,
        autostart: false,
        stretching: "uniform",
        repeat: false,
        volume: 100,
        controls: true,
        tokenEncrypt: "true",
        // AccessKey
        ak: '93cef76cad614a4dbc64b1baae4f465b'
    });
    player.on("beforePlay",function (e) {
        if(!/m3u8/.test(e.file)){
            return;
        }

        duajax.get({
            'url': '/course/course_token/',
            'data': {
                'video_url': video_url,
                'course_id': course_id
            },
            'success': function (result) {
                if(result['code'] === 200){
                    var token = result['data']['token'];
                    player.setToken(e.file,token);
                }else{
                    window.layer.msg(result['message'],{icon:5});
                    player.stop();
                }
            }
        });
    });
});