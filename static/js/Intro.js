$(document).ready(function(){
	data={
		introList : [{
			name: 'SEM',
			content: 'this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>',
			srcOfPic: '../../static/src/neko1.jpg'
		},{
			name: 'SEM1',
			content: 'this is SEM',
			srcOfPic: '../../static/src/neko2.jpg'
		},{
			name: 'SEM2',
			content: 'this is SEM',
			srcOfPic: '../../static/src/neko3.jpg'
		}]
	}
	template.config('escape', false)
	$("section.content").html(template('main_template', data))
})
