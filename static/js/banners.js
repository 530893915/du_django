/**
 * Created by Administrator on 2018/9/20.
 */

// 右上关闭
function addCloseBannerEvent(bannerItem) {
    var closeBtn = bannerItem.find('.close-btn');
    closeBtn.click(function () {
        bannerItem.remove();
    });
}

// 绑定选择图片的事件
function addImageSelectEvent(bannerItem) {
    var image = bannerItem.find(".banner-image");
    var imageSelect = bannerItem.find(".image-select");
    image.click(function () {
        imageSelect.click();
    });
    imageSelect.change(function () {
        var file = this.files[0];
        var formData = new FormData();
        formData.append('upfile',file);
        
        duajax.post({
            'url': '/cms/upload_file/',
            'data': formData,
            'processData': false,
            'contentType': false,
            'success': function (result) {
                if(result['code']===200){
                    var url = result['data']['url'];
                    image.attr('src',url);
                }
            }
        })
    });
}

// 点击保存
function addSaveBannerEvent(bannerItem) {
    var saveBtn = bannerItem.find(".save-btn");
    var image = bannerItem.find(".banner-image");
    var titleh3 = bannerItem.find("input[name='title-h3']");
    var titlep = bannerItem.find("input[name='title-p']");
    var priorityInput = bannerItem.find("input[name='priority']");
    var linktoInput = bannerItem.find("input[name='link_to']");
    saveBtn.click(function () {
        var image_url = image.attr('src');
        var title_h3 = titleh3.val();
        var title_p = titlep.val();
        var priority = priorityInput.val();
        var link_to = linktoInput.val();

        duajax.post({
            'url': '/cms/add_banner/',
            'data': {
                'image_url': image_url,
                'title_h3': title_h3,
                'title_p': title_p,
                'priority': priority,
                'link_to': link_to
            },
            'success': function (result) {
                if(result['code']===200){
                    var bannerId = result['data']['banner_id'];
                    bannerItem.attr('data-banner-id',bannerId);
                    var prioritySpan = bannerItem.find('.priority-span');
                    prioritySpan.text("优先级："+ priority);
                }else{
                    xfzalert.alertErrorToast(result['message']);

                }
            }
        })

    });
}

// 网页加载完毕后就执行获取轮播图列表的事件
$(function () {
    duajax.get({
        'url': '/cms/banner_list/',
        'success': function (result) {
            if(result['code']===200){
                var banners = result['data']['banners'];
                for(var i=0; i<banners.length; i++){
                    var banner = banners[i];
                    createBannerItem(banner);
                }

            }
        }
    })
});

// 绑定添加轮播图按钮的点击事件
$(function () {
    var addBtn = $('#add-banner-btn');
    addBtn.click(function () {
        createBannerItem();
    });
});

function createBannerItem(banner) {
    var tpl = template("banner-item",{'banner':banner});
    var bannerListGroup = $(".banner-list-group");
    var bannerItem = null;
    if(banner){
        bannerListGroup.append(tpl);
        bannerItem = bannerListGroup.find('.banner-item:last');
    }else{
        bannerListGroup.prepend(tpl);
        bannerItem = bannerListGroup.find('.banner-item:first');
    }
    addCloseBannerEvent(bannerItem);
    addImageSelectEvent(bannerItem);
    addSaveBannerEvent(bannerItem);
}


