$(document).ready(function(){
	example_homeworkCheck_data={
		homeworkName: 'test name',
		homeworkContent: 'test<br>test<br>test<br>test<br>test<br>test<br>',
		totalOfHomeworkSubmit: '50',
		totalOfUngradeHomeworkSubmit: '35',
		studentID: '3140100001',
		studentName: '春天的熊',
		srcUrl: '#',
		srcName: 'part1.pdf'
	}

	var homeworkID = getQueryString("homeworkID")
	var userID = localStorage.getItem("ID")
	var homeworkCheck_data = {userID: userID, homeworkID: homeworkID}

	$.ajax({
		url: "/api/intoGradeHomework/",
		type: "post",
		data: homeworkCheck_data,
		dataType: "json",
		success: function(data){
			template.config('escape', false)
			$("section.content").html(template('main_template', data))
			SubmitCheck()
		},
		error: function(){
			alert("POST " + "/api/intoGradeHomework/" + " ERROR!")
		}
	})
})

function SubmitCheck() {
    $("#submitCheck").click(function() {
    	var teacherID = localStorage.getItem("ID")
    	var studentID = $(this).data("studentID")
    	var homeworkID = getQueryString("homeworkID")
    	var grade = $("#score").val()
    	var remark = $("#commet").val()

    	var submitCheck_data = {
    		teacherID: teacherID,
    		studentID: studentID,
    		homeworkID: homeworkID,
    		grade: grade,
    		remark: remark
    	}

    	$.ajax({
			url: "/api/GradeHomework/",
			type: "post",
			data: submitCheck_data,
			dataType: "json",
			success: function(data){
				alert("check " + data.result + "!")
			},
			error: function(){
				alert("POST " + "/api/GradeHomework/" + " ERROR!")
			}
		})
    })
}



//获取地址参数
function getQueryString(name) {
    var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i')
    var r = window.location.search.substr(1).match(reg)
    if (r != null) {
        return unescape(r[2])
    }
    return null
}
