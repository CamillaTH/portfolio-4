$(function(){

    //Script that animates the counts of likes 
    $('#like-counter').each(function () {
        $(this).prop('like-counter',0).animate({
            Counter: $(this).text()
        }, {
            duration: 5500,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });

  });