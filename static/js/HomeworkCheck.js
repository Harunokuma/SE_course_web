$(document).ready(function(){
	data={
		homeworkName: 'test name',
		homeworkContent: 'test<br>test<br>test<br>test<br>test<br>test<br>',
		totalOfHomeworkSubmit: '50',
		totalOfUngradeHomeworkSubmit: '35',
		studentID: '3140100001',
		studentName: '春天的熊',
		srcUrl: '#',
		srcName: 'part1.pdf'
	}
	template.config('escape', false)
	$("section.content").html(template('main_template', data))
})
