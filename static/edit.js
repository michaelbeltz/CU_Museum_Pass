var post = function(review, id){
	var data = {"id": id, "review": review}
	$.ajax({
        type: "POST",
        url: "/add_review",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data),
        success: function(result){
        	var id = result["id"]

        	window.location.replace("/view/" + id);
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
};


$(document).ready(function()
{
	$("#textbox").focus()

	$("#textbox").keyup(function(event) 
    {
        if (event.keyCode === 13) 
        { 
            $("#post").click();
        }
    });

    $("#discard").click(function(){
    	window.location.replace("/view/" + id);
    })

    $("#post").click(function(){
    	var review = $('#textbox').val()
    	$('#textbox').val("")

    	post(review, id)
    })
});