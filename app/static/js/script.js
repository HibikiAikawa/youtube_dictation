$(document).ready(function(){
    $('#reload_youtube').click(function(){
        var iframe = $('#youtube_iframe');
        iframe.attr('src', iframe.attr('src'));
    });
});
