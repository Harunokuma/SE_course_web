$(document).ready(function(){
    data_message={
        totalOfUnreadMessage : "3",
        noticeList : [{sender : "傅文渊" ,
            title : "看什么看" ,
            content : "没见过未读消息啊没见过未读消息啊没见过未读消息啊" ,
            time : "12/02/2016"},
            {sender : "傅文渊" ,
                title : "还看" ,
                content : "听不懂人话啊" ,
                time : "12/02/2016"},
            {sender : "傅文渊" ,
                title : "还不关掉？？？？" ,
                content : "你这人有毒吧" ,
                time : "12/02/2016"}
        ]
    }
	template.config('escape', false)
    $("li.messages-menu").html(template('message_template', data_message))
})
