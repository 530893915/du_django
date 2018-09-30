/**
 * Created by Administrator on 2018/9/17.
 */

$(function () {
      layer.open({
        type: 1
        ,title: false //不显示标题栏
        ,closeBtn: false
        ,area: '300px;'
        ,shade: 0.8
        ,id: 'LAY_layuipro' //设定一个id，防止重复弹出
        ,btn: ['好的~','溜了溜了...']
        ,btnAlign: 'c'
        ,moveType: 1 //拖拽模式，0或者1
        ,content: '<div style="padding: 50px; line-height: 22px; background-color: #283b3c; color: #fff; font-weight: 300;">嗨！<br><br>这里是DUDU的个人网站，用于学习笔记的整理。<br><br>欢迎！O(∩_∩)O<br></div>'
        ,success: function(){

        }
    });
});



// 点击切换分类
$(function () {
    var categoryUl = $('.list-tab-group');
    var liTags = categoryUl.children();
    var loadBtn = $('.load-more-btn');
    liTags.click(function () {

        var li = $(this);
        var categoryId = li.attr('data-category-id');

        duajax.get({
            'url': '/list/',
            'data': {
                'category_id': categoryId
            },
            'success': function (result) {
                var newses = result['data'];
                var tpl = template("news-item",{"newses":newses});
                var newsListGroup = $(".news-list-group");
                newsListGroup.empty();
                newsListGroup.append(tpl);
                li.addClass('active1').siblings().removeClass('active1');
                loadBtn.attr('data-page',2);
                loadBtn.text('加载更多');
            }
        })
    })
});

// 加载更多
$(function () {
    var loadBtn = $('.load-more-btn');
    loadBtn.click(function () {
        layer.load();
        var li = $('.list-tab-group li.active1');
        var category_id = li.attr('data-category-id');
        var page = parseInt(loadBtn.attr('data-page'));

        duajax.get({
            'url': '/list/',
            'data': {
                'p':page,
                'category_id': category_id
            },
            'success':function (result) {
                var newses = result['data'];
                if(newses.length>0){
                    var tpl = template("news-item",{"newses":newses});
                    var newsListGroup = $('.news-list-group');
                    newsListGroup.append(tpl);
                    page += 1;
                    loadBtn.attr('data-page',page);
                    layer.closeAll('loading');
                }else{
                    loadBtn.text('没有更多了。。。');
                    window.layer.msg('没有更多啦~',{anim: 6});
                    layer.closeAll('loading');
                }
            }
        })
    })
});