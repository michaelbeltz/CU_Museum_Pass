var display_reviews = function(reviews){
	$.each(reviews, function(index, val){
		var div = $("<div>" + val + "</div>")
		
		$("#reviews").append(div)
	})
};

var define_click = function(){
    $("#edit").click(function(){
        window.location.replace("/edit/" + id);
    })
}

$(document).ready(function()
{
	display_reviews(reviews)
    define_click()

});