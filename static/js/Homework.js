$(document).ready(function(){
	data={
		homeworkName: 'test name',
		homeworkContent: 'test<br>test<br>test<br>test<br>test<br>test<br>',
		teacherName: 'Mr.J',
		url: '#',
		DDL: '12/01/2016',
		eventList: [{
			type: 'CHECK',
			body: '零分零分零分！',
			timeToNow: '28 mins ago'
		},{
			type: 'COMMENT',
			body: '你这个比做得有点好啊',
			timeToNow: '5 hours ago'
		},{
			type: 'STOP',
			body: '',
			timeToNow: '2 days ago'
		},{
			type: 'COMMIT',
			body: '',
			timeToNow: '3 days ago'
		},{
			type: 'POST',
			body: '',
			timeToNow: '5 days ago'
		}]
	}
	template.config('escape', false)
	$("section.content").html(template('main_template', data))
})
