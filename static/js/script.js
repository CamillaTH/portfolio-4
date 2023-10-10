$(function(){
/*---------------------------------------
  Functions
-----------------------------------------*/

    //Script that animates the counts of likes 
    $.initLikeAnimation = function () {
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
}

/*---------------------------------------
  Animations and style manipulations  
-----------------------------------------*/
    //add tootltip to like container
    $(".like-container").attr('title', 'View post to like it!');

    //init like animation
    $.initLikeAnimation();








    

  });