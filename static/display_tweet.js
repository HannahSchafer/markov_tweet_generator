$(document).ready(function(){


function displayTweet(event) {
    var twitter_handle = $("#twitter_handle").val();
    $.get("/show-markov-tweet", {"twitter_handle" : twitter_handle}, 
                                function(results) {
                                $('#tweet-spot').html(results.tweet);
    
    });  
    event.preventDefault();
}




// event listener - calls ajax request for new Markov tweet & shows response
$('#submit-btn').on('click', displayTweet);


});