$(document).ready(function(){
	data={
		list : [
			{title: 'SEM', content: 'this is SEM'},
			{title: 'SEM2', content: 'this is SEM2'},
			{title: 'SEM3', content: 'this is SEM3'}]
		}
	$("section.content").html(template('main_template', data))
})