$(document).ready(function () {

    $('body').bootstrapMaterialDesign()

    particlesJS.load('particles-js', '/static/redqueen/js/particles/particlesjs-config.json', function () {
        console.debug('particles.js config loaded...')
    })
})