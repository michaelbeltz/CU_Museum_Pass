var searchterm = ""

var search = function(searchterm){
	var data = {"searchterm": searchterm}
	$.ajax({
        type: "POST",
        url: "get_search",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data),
        success: function(result){
            var museums = result["museums"]
            
            display_museum_list(museums)
            define_click()
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
};

var display_museum_list = function(museums){
	$(".result").remove()
	$(".X").remove()
    $(".res_box").remove()

	$.each(museums, function(index, val){
		var div = $("<button class='X " + val["id"] + "' id='button_" + val["id"] + "' data-id='" + val["id"] + "'>X</button><div class='res_box'><a class='result " + val["id"] + "' href='/view/" + val["id"] + "'><div class='result row'><div class='image col-md-3'><img src='" + val["image"] + "' width='150'></div><div class='words col-md-9'><div class='name'>" + val["name"] + "</div><div class='rating'>" + val["rating"] + "/5</div><div class='description'>" + val["description"] + "</div></div></div></a></div>")
		// $('#button_' + val["id"]).data(val["id"])

		$("#results").append(div)
	})
};

var define_click = function(){
    $(".X").click(function(){
    	id = this.dataset.id
        delete_item(id)
    })
}

var delete_item = function(id){
	var data_to_del = {"id": id, "searchterm": searchterm} 
    $.ajax({
        type: "POST",
        url: "delete_item",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_del),
        success: function(result){
            var museums = result["museums"]
            
            display_museum_list(museums)
            define_click()
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}


$(document).ready(function()
{
	$("#searchbar").focus()

	//enter triggers submit
    $("#searchbar").keyup(function(event) 
    {
        if (event.keyCode === 13) 
        { 
            $("#submit").click();
        }
    });

    //submit
    $("#submit").click(function(){
        searchterm = $("#searchbar").val()
        $("#searchbar").val("");

        search(searchterm)

        $("#searchbar").focus()
    });

    define_click()

});