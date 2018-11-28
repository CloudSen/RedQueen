$()
{
    // ----------------------------------- 配置 ---------------------------------------
    let url = "https://storeweb.cn/api/friend_link"
    // 1 == 小图 2 ==大图
    let logo_size = 1
    // ----------------------------------- 配置 ---------------------------------------

    $('.site-friend-link').html('正在向『个站商店』请求友链数据……')
    get_friend_link_api(0)

    function get_friend_link_api(timeout) {
        $.ajax({
            type: 'get',
            url: url,
            async: true,
            dataType: 'jsonp',
            data: {
                size: logo_size
            },
            timeout: 3000,
            success: function (success) {
                if (success['success'] === 1) {
                    //console.log(success['data']);
                    template_make(success['data'])
                    set_storeweb_info(success['information'])
                } else {
                    $('.site-friend-link').html(success['info'])
                }
            },
            complete: function (XMLHttpRequest, status) {
                if (status === 'timeout') {
                    if (timeout === 1) {
                        $('.site-friend-link').html('获取数据超时……请联系个站商店小彦')
                    } else {
                        url = "http://storeweb.cn/api/friend_link"
                        $('.site-friend-link').html('https 获取数据超时……尝试http获取……')
                        get_friend_link_api(1)
                    }
                }
            }
        })
    }

    function template_make(data) {
        //console.log(data)
        $('.site-friend-link').html('')
        $.each(data, function (key, value) {
            //console.log(value.name);
            let template = $('#links-template').text()
            template = template.replace('%%name%%', value.name)
            template = template.replace('%%logo_cn%%', value.logo_cn)
            template = template.replace('%%intro_link%%', value.intro_link)
            template = template.replace('%%domain%%', 'http://' + value.domain)
            template = template.replace('%%update_count%%', value.update_count)
            if (value.update_count === 0) {
                template = template.replace('%%update_hide%%', 'hide')
            } else {
                template = template.replace('%%update_hide%%', 'F')
            }
            let template_id = $(template)
            $('.site-friend-link').prepend(template_id)
        })
    }

    function set_storeweb_info(information) {
        $('.site-friend-link-homepage').attr('href', information['homepage'])
        $('.site-friend-link-project').attr('href', information['project'])
        //$('.site-friend-link-storeweb').attr('href',information['storeweb']);
    }
}