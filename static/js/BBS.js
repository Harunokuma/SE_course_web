$(document).ready(function(){
    data={
        areaList : [{areaID : "1" ,
            areaName : "软件需求工程 刘玉生老师 周五3.4.5节" },
			{areaID : "2" ,
            areaName : "软件工程管理 金波老师 周三3.4.5节" }] ,
        forumsList : [{forumsID : "1" ,
            forumsName : "你追我" ,
            userName : "傅文渊" ,
            time : "12/01/2016" ,
            lastTime : "12/01/2016"},
            {forumsID : "2" ,
                forumsName : "如果你追到我" ,
                userName : "傅文渊" ,
                time : "12/01/2016" ,
                lastTime : "12/01/2016"},
            {forumsID : "3" ,
                forumsName : "我就和你嘿嘿嘿" ,
                userName : "傅文渊" ,
                time : "12/01/2016" ,
                lastTime : "12/01/2016"}]
    }
	template.config('escape', false)
    $("section.content").html(template('main_template', data))
})
