$(function () {
    function setClipboardText(event) {
        event.preventDefault()
        let node = document.createElement('div')
        let selected_data = window.getSelection().getRangeAt(0).cloneContents()
        console.debug('selected data:\n' + selected_data)
        // get copy text contain html tag
        node.appendChild(selected_data)
        let current_url = window.location.href
        let htmlData = '<div>著作权归作者所有。<br />'
            + '商业转载请联系作者获得授权，非商业转载请注明出处。<br />'
            + '作者：CloudSen<br />链接：' + current_url + '<br />'
            + '来源：Cloudable<br /><br />'
            + node.innerHTML
            + '</div>'
        let textData = '著作权归作者所有。\n'
            + '商业转载请联系作者获得授权，非商业转载请注明出处。\n'
            + '作者：Cloudsen\n链接：' + current_url + '\n'
            + '来源：Cloudable\n\n'
            + window.getSelection().getRangeAt(0)
        console.debug('htmldata:\n' + htmlData)
        console.debug('textdata:\n' + textData)
        if (event.originalEvent.clipboardData) {
            event.originalEvent.clipboardData.setData("text/html", htmlData)
            event.originalEvent.clipboardData.setData("text/plain", textData)
        }
        // IE
        else if (window.clipboardData) {
            return window.clipboardData.setData("text", textData)
        }
    }

    let answer = $('#article-detail')
    answer.on('copy', function (e) {
        console.debug('ClipboardEvent!\n')
        setClipboardText(e)
    })

    let myLazyLoad = new LazyLoad({
        elements_selector: ".lazy"
    })
})