/**
 * Created by Administrator on 2018/9/17.
 */



// 加载更多
$(function () {
    var loadBtn = $('.load-more-btn');
    loadBtn.click(function (event) {
        event.preventDefault();

        var li = $('.list-tab-group li.active');
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
                }else{
                    loadBtn.text('没有更多了。。。');
                    window.layer.msg('没有更多啦~');
                }
            }
        })
    })
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
            }
        })
    })
});