$(document).ready(function(){
	data={
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
	template.config('escape', false)
	$("section.content").html(template('main_template', data))
})