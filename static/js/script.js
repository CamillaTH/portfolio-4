$(function(){

/*---------------------------------------
  Constants
-----------------------------------------*/
//const timeout3Seconds = setTimeout(3000);



/*---------------------------------------
  Functions
-----------------------------------------*/

    //function that animates the counts of likes 
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

    // removes shaker class 
    $.removeShakerClass = function() {
        $("#like-post-detail,#like-comment-detail").removeClass( "fa-shake" );
    }


function stopTimeout3Seconds() {
    clearTimeout(timeout3Secionds);
  }

/*---------------------------------------
  Animations and style manipulations  
-----------------------------------------*/
    //add tootltip to like container
    $(".like-container").attr('title', 'View post to like it!');
    
    //add tootltip to like container detail
    $(".like-container-detail,#like-comment-detail").attr('title', 'Like post!');

    $("#like-post-detail,#like-comment-detail").hover(
        function () {
         console.log("sadas")
          $(this).addClass("fa-solid");
        },
        function () {
            $(this).removeClass("fa-solid");
          }
    )

    // add shake animation to like button
    $("#like-post-detail,#like-comment-detail").on( "click", function() {
      $("#like-post-detail,#like-comment-detail").addClass( "fa-shake" );
      //wait 2 seconds then remove shaker class
      timeout = setTimeout($.removeShakerClass, 2000);
    });

    //init like animation
    $.initLikeAnimation();


  });