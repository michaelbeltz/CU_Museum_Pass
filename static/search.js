var searchterm = ""

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

var display_museum_list = function(museums, searchterm){
	$(".result").remove()
	$(".res_box").remove()

	var num_results = museums.length

	$("#results").append("<div id='num_results'>" + num_results + " Results Found:</div>")

	$.each(museums, function(index, val){

		var name = val["name"]
		var description = val["description"]

		if (description.length > 400)
		{
			description = description.substring(0,400)
			description += "..."
		}

		var re = new RegExp(searchterm,"g");

		name = name.replace(re , "<span class='highlight'>" + searchterm + "</span>")
		description = description.replace(re, "<span class='highlight'>" + searchterm + "</span>")

		var div = $("<div class='res_box'><div class='result row'><div class='image col-md-3'><a class='result " + val["id"] + "' href='/view/" + val["id"] + "'><img src='" + val["image"] + "' alt='The facade of " + val["name"] + "' width='150'></a></div><div class='words col-md-9'><div class='name'>" + name + "</div><div class='rating'>" + val["rating"] + "/5</div><div class='description'>" + description + "</div></div></div></div><br class='res_box'>")
		// $('#button_' + val["id"]).data(val["id"])

		$("#results").append(div)
	})

};


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

	display_museum_list(museums, searchterm)

});