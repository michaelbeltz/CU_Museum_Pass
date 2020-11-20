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

var display_museum_list = function(museums){
	$(".result").remove()
    $(".res_box").remove()

    $("#results").append("<div id='num_results'>Latest 10 Entries:</div>")

    var counter = 0

	$.each(museums.reverse(), function(index, val){

        var description = val["description"]

        if (description.length > 300)
        {
            description = description.substring(0,300)
            description += "..."
        }

        if (counter < 10)
        {
    		var div = $("<div class='res_box'><div class='result row'><div class='image col-md-3'><a class='result " + val["id"] + "' href='/view/" + val["id"] + "'><img src='" + val["image"] + "' alt='The facade of " + val["name"] + "' width='150'></a></div><div class='words col-md-9'><div class='name'>" + val["name"] + "</div><div class='rating'>" + val["rating"] + "/5</div><div class='description'>" + description + "</div></div></div></div><br class='res_box'>")

    		$("#results").append(div)
            counter += 1
        }
	})
};


$(document).ready(function()
{
	$(".searchbar").focus()

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

    display_museum_list(museums)

});