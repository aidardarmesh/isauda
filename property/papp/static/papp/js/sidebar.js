$(document).ready(function(){
    $('#menu-toggle').click(function(e){
        e.preventDefault();
        $('#wrapper').toggleClass('toggled');
        $('#overlay').fadeToggle('slow', 'swing');
    });

    $('#overlay').click(function(){
        $('#overlay').fadeOut('slow');
        $('#wrapper').removeClass('toggled');
    });
});