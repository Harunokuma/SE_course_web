$(document).ready(function(){
    data={
        forumsName : "你要不要来追我呀" ,
        forumList : [{userName : "傅文渊" ,
            content : "你追我" ,
            time : "12/01/2016" ,
            url : "http://I Don't Know"},
            {userName : "傅文渊" ,
                content : "如果你追到我" ,
                time : "12/01/2016" ,
                url : "http://I Don't Know Either"},
            {userName : "傅文渊" ,
                content : "我就和你嘿嘿嘿" ,
                time : "12/01/2016" ,
                url : ""}]
    }
	template.config('escape', false)
    $("section.content").html(template('main_template', data))
    $("section.content-header").html(template('title_template', data))
})
