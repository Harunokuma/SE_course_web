$(document).ready(function(){
	data={
		homeworkName: 'test name',
		homeworkContent: 'test content<br>test content<br>test content<br>test content<br>test content<br>',
		DDL: '12/25/2016',
		startTime: '12/04/2016',
		classList: [{
			classID: '00000',
			className: 'SEM',
			classTime: '周五 345',
			isSelect: 'Y'
		},{
			classID: '00001',
			className: 'SER',
			classTime: '周三 345',
			isSelect: 'N'
		},{
			classID: '00002',
			className: 'SET',
			classTime: '周一 345',
			isSelect: 'N'
		}]
	}
	template.config('escape', false)
	$("section.content").html(template('main_template', data))
})
