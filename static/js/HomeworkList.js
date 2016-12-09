$(document).ready(function(){
	example_homeworkList_data={
		classList : [{
			classID: 'SEM0001',
			className: 'SEM',
			teacherName: '刘玉生',
			classTime: '星期五 345',
			homeworkList:[{
				homeworkID: '00000',
				homeworkName: 'fuck it',
				homeworkContent: 'anything<br>anything',
				DDL: '2016-12-20',
				status: 'T'
			},{
				homeworkID: '00001',
				homeworkName: 'fuck it',
				homeworkContent: 'anything<br>anything<br>anything<br>anything<br>anything<br>',
				DDL: '2016-12-20',
				status: 'D'
			},{
				homeworkID: '00002',
				homeworkName: 'fuck it',
				homeworkContent: 'anything<br>anything<br>anything<br>anything<br>anything<br>',
				DDL: '2016-12-20',
				status: 'U'
			}]
		},{
			classID: 'SEM0002',
			className: 'SEM',
			teacherName: '刘玉生',
			classTime: '星期五 789',
			homeworkList:[{
				homeworkID: '00000',
				homeworkName: 'fuck it',
				homeworkContent: 'anything<br>anything<br>anything<br>anything<br>anything<br>',
				DDL: '2016-12-20',
				status: 'T'
			},{
				homeworkID: '00001',
				homeworkName: 'fuck it',
				homeworkContent: 'anything<br>anything<br>anything<br>anything<br>anything<br>',
				DDL: '2016-12-20',
				status: 'D'
			},{
				homeworkID: '00002',
				homeworkName: 'fuck it',
				homeworkContent: 'anything<br>anything<br>anything<br>anything<br>anything<br>',
				DDL: '2016-12-20',
				status: 'U'
			}]
		}]
	}

	var userID = localStorage.getItem('ID')
	var homeworkList_data = {userID: userID}
	$.ajax({
		url: '/api/HomeworkList/',
		type: "post",
		data: homeworkList_data,
		dataType: "json",
		success: function(data){
			template.config('escape', false)
			$("section.content").html(template('main_template', data))
		},
		error: function(){
			alert("POST " + "/api/HomeworkList/" + " ERROR!")
		}
	})
})