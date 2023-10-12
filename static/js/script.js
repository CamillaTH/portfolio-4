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

    //show comment submittet msg
    $(document).ready(function() {
      const storedCommentMessage = localStorage.getItem('commentConfirmationMessage');
      if (storedCommentMessage) {
        $('.comment-confirmation').show().text(storedCommentMessage);
        // Clear the stored message
        localStorage.removeItem('commentConfirmationMessage');
        //wait 4 seconds then hide comment comfirmation msg
        timeout = setTimeout($.hideCommentConfirmationMsg, 4000);
       }

      $('.comment-form > button').bind('click', function(){
        $.showCommentConfirmationMsg();
      });
    });

    // hides comment confirmation message 
    $.hideCommentConfirmationMsg = function() {
      $('.comment-confirmation').hide();
      //remove confirmation from message local storage
      localStorage.removeItem('commentConfirmationMessage');
    }

    // hides comment confirmation message 
    $.showCommentConfirmationMsg = function() {
      $('.comment-confirmation').show();
      //add confirmation message to local storage since when form is submitted the page realoads 
      localStorage.setItem('commentConfirmationMessage', 'Your comment have been submitted! It will be shown when approved by post owner');
    }
    
     // removes shaker class 
     $.removeShakerClass = function() {
      $("#like-post-detail,#like-comment-detail").removeClass( "fa-shake" );
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
      timeout = setTimeout($.removeShakerClass, 5000);
    });

  
    //init like animation
    $.initLikeAnimation();

  });