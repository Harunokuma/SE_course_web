(function isLogin()
{
	if(localStorage.getItem("ID") != null)
      window.location.href = "../CourseIntro/"
}())

$("#submit").click(function()
{
	var userID = $("[type='text']").val();
	var passwd = $("[type= 'password']").val();
	var postdata = {
		ID: userID,
		password: passwd
	};
	$.ajax({
		type: 'POST',
		url: '../../UserVerify/',
		data: postdata,
		dataType: 'json',
		success: function(data){
			if(data.result == 'Y')
			{
				localStorage.setItem('ID', userID);
				localStorage.setItem('Identity', data.Identity);
				localStorage.setItem('Name', data.Name);
				window.location.href = '../CourseIntro';
			}
			else
				alert("wrong ID or password!");
		}
		
	});
});

