$(document).ready(function() {
    example_homework_data = {
        homeworkName: 'test name',
        homeworkContent: 'test<br>test<br>test<br>test<br>test<br>test<br>',
        teacherName: 'Mr.J',
        url: '#',
        DDL: '12/01/2016',
        eventList: [{
            type: 'CHECK',
            body: '零分零分零分！',
            timeToNow: '28 mins ago'
        }, {
            type: 'COMMENT',
            body: '你这个比做得有点好啊',
            timeToNow: '5 hours ago'
        }, {
            type: 'STOP',
            body: '',
            timeToNow: '2 days ago'
        }, {
            type: 'COMMIT',
            body: '',
            timeToNow: '3 days ago'
        }, {
            type: 'POST',
            body: '',
            timeToNow: '5 days ago'
        }]
    }

   	//获取
    var homeworkID = getQueryString('homeworkID')
    var userID = localStorage.getItem('ID')
    homework_data = { userID: userID, homeworkID: homeworkID }

    $.ajax({
        url: "/api/Homework/",
        type: "post",
        data: homework_data,
        dataType: "json",
        success: function(data) {
            template.config('escape', false)
            $("section.content").html(template('main_template', data))
            submitHomework()
        },
        error: function(){
        	alert("POST " + "/api/Homework/" + " ERROR!")
        }
    })
})

//上传作业
function submitHomework(){
	$("#UpFile").change(function(){
		var homeworkID = getQueryString('homeworkID')
    	var userID = localStorage.getItem('ID')
    	var submit_data = new FormData()
    	submit_data.append("userID", userID)
    	submit_data.append("homeworkID", homeworkID)
    	submit_data.append("srcFile", $("#UpFile")[0].files[0])

    	$.ajax({
    		url: "/api/SubmitHomework/",
    		type: "post",
            data: submit_data,
            processData: false,
            contentType: false,
            success: function(data) {
                alert("upload " + data.result + "!")
            },
            error: function() {
                alert("POST ERROR")
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
