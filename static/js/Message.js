$(document).ready(function() {
    //示范数据
    var example_message_data = {
        totalOfUnreadMessage: "5",
        noticeList: [{
            sender: "傅文渊",
            content: "没见过未读消息啊没见过未读消息啊没见过未读消息啊",
            time: "12/02/2016"
        }, {
            sender: "傅文渊",
            content: "听不懂人话啊",
            time: "12/02/2016"
        }, {
            sender: "傅文渊",
            content: "你这人有毒吧",
            time: "12/02/2016"
        }, {
            sender: "傅文渊",
            content: "你这人有毒吧",
            time: "12/02/2016"
        }, {
            sender: "傅文渊",
            content: "你这人有毒吧",
            time: "12/02/2016"
        }]
    }

    var userID = localStorage.getItem("ID")
    var message_data = { userID: userID }
    $.ajax({
        url: "/api/CheckMessage/",
        type: "post",
        data: message_data,
        dataType: "json",
        success: function(data) {
            //成功获得通知数据后渲染通知模板
            initMessageTemplate(data)
            //监控已读通知的按键
            ReadMessage()
        },
        error: function() {
            alert("POST " + "/api/CheckMessage/" + " ERROR!")
        }
    })
})

//渲染通知模板
function initMessageTemplate(data) {
    template.config('escape', false)
    $("li.messages-menu").html(template('message_template', data))
}

//把所有通知标记为已读
function ReadMessage() {
    $("#ReadMessage").click(function(){
        var userID = localStorage.getItem("ID")
        var readMessage_data = {userID: userID}
        $.ajax({
            url: "/api/ReadMessage/",
            type: "post",
            data: readMessage_data,
            dataType: "json",
            success: function(data) {
            },
            error: function() {
                alert("POST " + "/api/ReadMessage/" + " ERROR!")
            }
        })
    })
}
