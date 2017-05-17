$(document).ready(function(){


function displayTweet(event) {
    $.get("/show-markov-tweet", function(results) {
                                var tweet_content = results.tweet;
                                $('#tweet-spot').html(results.tweet_content);
    });  
}




// event listener - calls ajax request for new Markov tweet & shows response
$('#submit-btn').on('click', displayTweet);


});