$(() => {
    // bootstrap material 需要的
    $('body').bootstrapMaterialDesign()

    // 加载粒子效果
    particlesJS.load('particles-js', '/static/redqueen/js/particles/particlesjs-config.json', () => {
        console.debug('particles.js config loaded...')
    })

    // 计算canvas的高度，占满整个页面
    function doHeightCalulate(lastHeight, newHeight) {
        console.group('document height changed...')
        console.debug('document last height: ' + lastHeight)
        console.debug('document new height: ' + newHeight)
        let $particalesDiv = $('#particles-js')
        console.group('before caculate height:\n')
        console.debug('canvase height: ' + $particalesDiv.height())
        console.debug('document height: ' + $(document).height())
        console.groupEnd()
        // $(document).height() - 4
        $particalesDiv.height($('.footer').offset().top)
        console.group('after caculate height:\n')
        console.debug('canvase height: ' + $particalesDiv.height())
        console.debug('document height: ' + $(document).height())
        console.groupEnd()
        console.groupEnd()
    }

    function onElementHeightChange(elm, callback) {
        let lastHeight = $(elm).height(), newHeight = 0
        // 一来先计算一次
        if (callback) {
            callback(lastHeight, newHeight)
        }
        (function run() {
            newHeight = $(elm).height()
            if (lastHeight !== newHeight)
                callback(lastHeight, newHeight)
            lastHeight = newHeight
            if (elm.onElementHeightChangeTimer)
                clearTimeout(elm.onElementHeightChangeTimer)
            elm.onElementHeightChangeTimer = setTimeout(run, 200)
        })()
    }

    onElementHeightChange(document, doHeightCalulate)

    /* 按下GoTop按鈕時的事件 */
    $('#gotop').click(() => {
        $('html,body').animate({scrollTop: 0}, 'slow')
        return false
    })

    /* 偵測卷軸滑動時，往下滑超過400px就讓GoTop按鈕出現 */
    $(window).scroll(() => {
        if ($(this).scrollTop() > 400) {
            $('#gotop').fadeIn()
        } else {
            $('#gotop').fadeOut()
        }
    })

    // CSRF
    function getCookie(name) {
        let cookieValue = null
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';')
            for (let i = 0; i < cookies.length; i++) {
                let cookie = jQuery.trim(cookies[i])
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                    break
                }
            }
        }
        return cookieValue
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
    }

    $.ajaxSetup({
        beforeSend: (xhr, settings) => {
            let $captchaMassage = $('#captcha-message')
            let csrftoken = getCookie('csrftoken')
            console.debug('csrftoken: ' + csrftoken)
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken)
            }
            if ($captchaMassage) {
                $captchaMassage.text('数据处理中...请稍后~')
            }
        }
    })
})