var search = function(searchterm){
    if (isEmpty(searchterm))
    {
        window.location.replace("/")
    }
    else
    {
        window.location.replace("/search/" + searchterm)
    }
};

function isEmpty(str) {
    return (str.length === 0 || !str.trim());
}

var display_reviews = function(reviews){
    $(".review_button").remove()
	$(".rev").remove()
	$("hr").remove()

	$.each(reviews, function(index, val){
		if (index == 0)
		{
			$("#reviews").append("<hr>")
		}

        if (val["mark_as_deleted"] == false)
        {
            var div = $("<div class='rev " + index + "'>" + val["review"] + "</div>\t<button class='review_button' id=" + index + ">X</button><hr>")
        
            $("#reviews").append(div)
        }
	})
};


var post = function(new_review, id){
	var dataN = {"id": id, "review": new_review}
	$.ajax({
        type: "POST",
        url: "/add_review",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(dataN),
        success: function(result){
        	var id = result["id"]
        	var reviews = result["reviews"]

        	$("#new_review").remove()
    		$("#review_discard").remove()
    		$("#review_post").remove()

        	display_reviews(reviews)
    		define_add(id)
            define_delete(id)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
};


function define_post(id){
	$("#review_post").click(function(){
		$("#review_error").remove()
    	new_review = $("#new_review").val()

    	var counter = 0

        //check if and fields are empty
        if (new_review.trim().length == 0)
        {
            $("#new_review").after("<div class='error' id='review_error'>This box cannot be empty.</div>")
    		$("#new_review").focus()
            counter +=1
        }
    	if (counter == 0)
    	{
    		post(new_review, id)
    	}

    });
}

function define_discard(id){
	$("#review_discard").click(function(){
    	$("#new_review").remove()
    	$("#review_discard").remove()
    	$("#review_post").remove()
    	$("#review_error").remove()

    	define_add(id)
    });
}

function define_add(id){
	$("#reviews").after("<button id='add_review'>Add Review</button>")

	$("#add_review").click(function(){
    	$("#add_review").remove()

    	$("#reviews").after("<input id='new_review' type='text'>")
    	$("#new_review").after("<div class='buttons'><button class='discard' id='review_discard'>Discard</button> <button class='post' id='review_post'>Post</button></div>")

    	$("#new_review").focus()

    	$("#new_review").keyup(function(event) 
		{
			if (event.keyCode === 13) 
			{ 
				$("#review_post").click();
			}
		});

    	define_discard(id)
    	define_post(id)
    });
}



var post_rating = function(new_rating, id){
	var data = {"id": id, "rating": new_rating}
	$.ajax({
        type: "POST",
        url: "/edit_rating",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data),
        success: function(result){
        	var id = result["id"]
        	var rating = result["rating"]

        	$("#new_rating").remove()
	    	$("#rating_discard").remove()
	    	$("#rating_post").remove()
	    	$("#outof5").remove()
	    	$("#edit_div").remove()
	    	$("#rating_buttons").remove()

    		define_edit(id, rating)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
};

function define_rating_post(id){
	$("#rating_post").click(function(){
		$("#rating_error").remove()
    	new_rating = $("#new_rating").val()


    	var counter = 0

        //check if and fields are empty
        if (new_rating.trim().length == 0)
        {
            $("#new_rating").before("<div class='error specialerror' id='rating_error'>This box cannot be empty.</div>")
    		$("#ratingbox").focus()
            counter +=1
        }
        if (isNaN(new_rating) || new_rating < 0 || new_rating > 5)
        {
            $("#new_rating").before("<div class='error specialerror' id='rating_error'>Rating must be a number between 0 and 5.</div>")
    		$("#new_rating").focus()
    		counter += 1
        }
    	if (counter == 0)
    	{
    		post_rating(new_rating, id)
    	}
    });
}

function define_rating_discard(id, rating){
	$("#rating_discard").click(function(){
    	$("#new_rating").remove()
    	$("#rating_discard").remove()
    	$("#rating_post").remove()
    	$("#outof5").remove()
    	$("#edit_div").remove()
    	$("#rating_buttons").remove()
    	$("#rating_error").remove()

    	define_edit(id, rating)
    });
}


function define_edit(id, rating){
	$("#ratingbox").append("<span id='rating'>" + rating + "</span><span id='outof5'>/5</span>")
	$("#ratingbox").append("<div id='edit_div'><button id='edit_rating'>Change Rating</button></div>")

	$("#edit_rating").click(function(){
    	$("#rating").remove()
    	$("#edit_rating").remove()

    	$("#ratingbox").prepend("<input id='new_rating' type='text'>")
    	$("#ratingbox").append("<div id='rating_buttons'><button class='discard' id='rating_discard'>Discard</button> <button class='post' id='rating_post'>Post</button></div>")

    	$("#new_rating").focus()

    	$("#new_rating").keyup(function(event) 
		{
			if (event.keyCode === 13) 
			{ 
				$("#rating_post").click();
			}
		});

    	define_rating_discard(id, rating)
    	define_rating_post(id)
    });

}

function mark_del(id, rev_id){
    var data = {"id": id, "rev_id": rev_id}
    $.ajax({
        type: "POST",
        url: "/mark_del",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data),
        success: function(result){
            var id = result["id"]
            var rev_id = result["rev_id"]

            define_undo(id, rev_id)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function unmark_del(id, rev_id){
    var data = {"id": id, "rev_id": rev_id}
    $.ajax({
        type: "POST",
        url: "/unmark_del",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data),
        success: function(result){
            var reviews = result["reviews"]
            var id = result["id"]
            var rev_id = result["rev_id"]

            var review = reviews[rev_id]["review"]

            var div = $("<div class='rev " + rev_id + "'>" + review + "</div>\t<button class='review_button' id=" + rev_id + ">X</button>")
        
            $("#undo_button_" + rev_id).after(div)

            $("#undo_button_" + rev_id).remove()

            define_delete(id)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function define_undo(id, rev_id){
    $("#undo_button_" + rev_id).click(function(){
        unmark_del(id, rev_id)
    });
}

function remove_rev(id, rev_id)
{
    $("#" + rev_id).remove()
    $("." + rev_id).after("<button class='undo_button' id='undo_button_" + rev_id + "'>Undo</button>")
    $("." + rev_id).remove()

    mark_del(id, rev_id)
}

function define_delete(id){
    $(".review_button").click(function(){
        remove_rev(id, this.id)
    });
}



$(document).ready(function()
{

	//enter triggers submit
	$(".searchbar").keyup(function(event) 
	{
		if (event.keyCode === 13) 
		{ 
			$(".go").click();
		}
	});

	//submit
	$(".go").click(function(){
		searchterm = $(".searchbar").val()
		$(".searchbar").val("");

		search(searchterm)

		$(".searchbar").focus()
	});

	display_reviews(reviews)
	define_edit(id, rating)
	define_add(id)
    define_delete(id)


});