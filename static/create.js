var create = function(item){
	$.ajax({
        type: "POST",
        url: "add_item",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(item),
        success: function(result){
            var id = result["id"]
            
            window.location.replace("/view/" + id);
        },
        error: function(request, status, error){
            displayError()
        }
    });
};

var displayError = function(){
    $("#submit").after("<div><span class='error'>There was an error adding the item.</span></div>")
    $("#name_text").focus()
}

$(document).ready(function()
{
	$("#name_text").focus()

    //submit
    $("#submit_button").click(function(){
        $(".error").remove()

        var name = $("#name_text").val()
        var image = $("#img_text").val()
        var description = $("#description_text").val()
        var rating = $("#rating_text").val()
        var review = $("#review_text").val()

        $("#name_text").val("");
        $("#img_text").val("");
        $("#description_text").val("");
        $("#rating_text").val("");
        $("#review_text").val("");

        item = {
            "name": name,
            "image": image,
            "description": description,
            "rating": rating,
            "review": review
        }

        create(item)

        $("#name_text").focus()
    });

});