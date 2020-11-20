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


var create = function(item){
	$.ajax({
        type: "POST",
        url: "add_item",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(item),
        success: function(result){
            var id = result["id"]

            $(".navbar").after("<div><span class='success'>Item successfully created. <a href='/view/" + id + "'>See it here.</a></span></div>")

            $("#name_text").focus()
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

//valid submit
var valid_submit = function(item){
    $("#name_text").val("");
    $("#img_text").val("");
    $("#description_text").val("");
    $("#rating_text").val("");
    $("#review_text").val("");

    create(item)
}

//errors
function name_empty_error(){
    $("#name_text").after("<div><span class='error'>^ This box cannot be empty. ^</span></div>")
    $("#name_text").focus()
}

function image_empty_error(){
    $("#image").after("<div><span class='error'>^ This box cannot be empty. ^</span></div>")
    $("#image").focus()
}

function description_empty_error(){
    $("#description").after("<div><span class='error'>^ This box cannot be empty. ^</span></div>")
    $("#description").focus()
}

function rating_empty_error(){
    $("#rating").after("<div><span class='error'>^ This box cannot be empty. ^</span></div>")
    $("#rating").focus()
}

function review_empty_error(){
    $("#reviews").after("<div><span class='error'>^ This box cannot be empty. ^</span></div>")
    $("#reviews").focus()
}

//type error
function rating_num_error(){
    $("#rating").after("<div><span class='error'>^ Rating must be a number between 0 and 5. ^</span></div>")
    $("#rating").focus()
}


$(document).ready(function()
{
	$("#name_text").focus()


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


    //submit
    $("#submit_button").click(function(){
        $(".error").remove()
        $(".success").remove()

        var name = $("#name_text").val()
        var image = $("#img_text").val()
        var description = $("#description_text").val()
        var rating = $("#rating_text").val()
        var review = $("#review_text").val()

        item = {
            "name": name,
            "image": image,
            "description": description,
            "rating": rating,
            "review": review
        }

        var counter = 0

        //check if and fields are empty
        if (name.trim().length == 0)
        {
            name_empty_error()
            counter +=1
        }
        if (image.trim().length == 0)
        {
            image_empty_error()
            counter += 1
        }
        if (description.trim().length == 0)
        {
            description_empty_error()
            counter += 1
        }
        if (rating.trim().length == 0)
        {
            rating_empty_error()
            counter += 1
        }
        if (review.trim().length == 0)
        {
            review_empty_error()
            counter += 1
        }

        //chech if all types are valid
        if (isNaN(rating) || rating < 0 || rating > 5)
        {
            rating_num_error()
            counter +=1
        }

        //valid submit. no errors.
        if (counter == 0)
        {
            valid_submit(item)
        }
    });

});