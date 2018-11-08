$(document).ready(function () {
    // bootstrap material 需要的
    $('body').bootstrapMaterialDesign()

    // 加载粒子效果
    particlesJS.load('particles-js', '/static/redqueen/js/particles/particlesjs-config.json', function () {
        console.debug('particles.js config loaded...')
    })

    // 计算canvas的高度，占满整个页面
    let $particalesDiv = $('#particles-js')
    console.group('before caculate height:\n')
    console.debug('canvase height: ' + $particalesDiv.height())
    console.debug('document height: ' + $(document).height())
    console.groupEnd()
    $particalesDiv.height($(document).height())
    console.group('after caculate height:\n')
    console.debug('canvase height: ' + $particalesDiv.height())
    console.debug('document height: ' + $(document).height())
    console.groupEnd()

    // 回到顶部按钮
    /* 按下GoTop按鈕時的事件 */
    $('#gotop').click(function(){
        $('html,body').animate({ scrollTop: 0 }, 'slow')
        return false
    });

    /* 偵測卷軸滑動時，往下滑超過400px就讓GoTop按鈕出現 */
    $(window).scroll(function() {
        if ( $(this).scrollTop() > 400){
            $('#gotop').fadeIn()
        } else {
            $('#gotop').fadeOut()
        }
    });
})