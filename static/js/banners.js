/**
 * Created by Administrator on 2018/9/20.
 */

// 右上关闭(删除)
function addCloseBannerEvent(bannerItem) {
    var closeBtn = bannerItem.find('.close-btn');
    var bannerId = bannerItem.attr('data-banner-id');
    closeBtn.click(function () {
        if(bannerId){
            xfzalert.alertConfirm({
                'text': '您确定要删除这个轮播图吗？',
                'confirmCallback': function () {

                    duajax.post({
                        'url': '/cms/delete_banner/',
                        'data': {
                            'banner_id': bannerId
                        },
                        'success': function (result) {
                            if(result['code']===200){
                                bannerItem.remove();
                                window.xfzalert.alertSuccessToast('删除成功！');
                            }
                        }
                    })
                }
            })
        }else{
            bannerItem.remove();
        }

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
    var bannerId = bannerItem.attr('data-banner-id');
    var url = '';
    if(bannerId){
        url = '/cms/edit_banner/'
    }else{
        url = '/cms/add_banner/'
    }
    saveBtn.click(function () {
        var image_url = image.attr('src');
        var title_h3 = titleh3.val();
        var title_p = titlep.val();
        var priority = priorityInput.val();
        var link_to = linktoInput.val();

        duajax.post({
            'url': url,
            'data': {
                'image_url': image_url,
                'title_h3': title_h3,
                'title_p': title_p,
                'priority': priority,
                'link_to': link_to,
                'pk': bannerId
            },
            'success': function (result) {
                if(result['code']===200){
                    if(!bannerId){
                        bannerId = result['data']['banner_id'];
                        bannerItem.attr('data-banner-id',bannerId);
                        window.xfzalert.alertSuccessToast('保存成功！');
                    }else{
                        window.xfzalert.alertSuccessToast('修改成功！');
                    }
                    var prioritySpan = bannerItem.find('.priority-span');
                    prioritySpan.text("优先级："+ priority);

                }else{
                    window.xfzalert.alertErrorToast(result['message']);
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
    var bannerListGroup = $('.banner-list-group');
    addBtn.click(function () {
        var length = bannerListGroup.children().length;
        if(length >=6){
            window.xfzalert.alertErrorToast('最多添加6个轮播图！');
        }else{
            createBannerItem();
        }
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




