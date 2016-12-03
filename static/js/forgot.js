$(document).ready(function() {
    $("#Question").css("display", "none")
    $("#Answer").css("display", "none")
    $("#Password").css("display", "none")

    $("[name='submit0']").click(function() {
        var userID = $("#ID").val()
        var id_data = { userID: userID }

        $.ajax({
            url: "/api/ReturnQuestion/",
            type: "post",
            data: id_data,
            dataType: "json",
            success: function(data) {
            	if(data.question == null)
            		alert("not exist ID")
            	else
            		VerifyAnswer(userID, data.question)
            },
            error: function() {
                alert("POST " + "/api/ReturnQuestion/" + " ERROR!")
            }
        })
    })
})

function VerifyAnswer(userID, question) {
    $("#Question").css("display", "block")
    $("#Answer").css("display", "block")
    $("#InputID").css("display", "none")
    $("#Question").val(question)
    $("[name='submit0']").attr("name", "submit1")
    $("#tips").html("Input your answer to reset your password")

    $("[name='submit1']").click(function() {
        var answer = $("#ans").val()
        var verifyAnswer_data = { userID: userID, answer: answer }

        $.ajax({
            url: "/api/TestAnswer/",
            type: "post",
            data: verifyAnswer_data,
            dataType: "json",
            success: function(data) {
                if(data.result == "success")
                	ChangePassword(userID)
                else if(data.result == "failed")
                	alert("Wrong answer!")
            },
            error: function() {
                alert("POST " + "/api/TestAnswer/" + " ERROR!")
            }
        })
    })
}

function ChangePassword(userID){
	$("#Question").css("display", "none")
    $("#Answer").css("display", "none")
    $("#Password").css("display", "block")
    $("[name='submit1']").attr("name", "submit2")
	$("#tips").html("Input your new password")
    $("[name='submit2']").click(function() {
    	var password = $("#passwd").val()
    	var changePassword_data = {userID: userID, password: password}
    	$.ajax({
            url: "/api/ResetPassword/",
            type: "post",
            data: changePassword_data,
            dataType: "json",
            success: function(data) {
            	if(data.result == "success")
            	{
            		alert("Reset password success!")
            		window.location.href = "../Login/"
            	}
            	else if(data.result == "failed")
            	{
            		alert("Reset password failed!")
            	}
            },
            error: function() {
                alert("POST " + "/api/ResetPassword/" + " ERROR!")
            }
        })
    })
}
