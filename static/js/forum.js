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

    var userID = localStorage.getItem("ID")
    var forumID = getQueryString("forumID")
    var forum_data = {userID: userID, forumID: forumID}

    $.ajax({
        url: "/api/Forum/",
        type: "post",
        data: forum_data,
        dataType: "json",
        success: function(data){
            template.config('escape', false)
            $("section.content-header").html(template('title_template', data))
            $("section.content").html(template('main_template', data))
            
            SubmitForum()
        },
        error:function(){
            alert("POST " + "/api/Forum/" + " ERROR!")
        }
    })
})

function SubmitForum() {
    $("#SubmitForum").click(function() {
        var userID = localStorage.getItem("ID")
        var forumID = getQueryString("forumID")
        var content = $("#ForumContent").val()
        var submitForum_data = new FormData()
        submitForum_data.append("userID", userID)
        submitForum_data.append("forumID", forumID)
        submitForum_data.append("content", content)
        try {
            submitForum_data.append("srcFile", $("#UpFile")[0].files[0])
        } finally {
            $.ajax({
                url: "/api/SubmitForum/",
                type: "post",
                data: submitForum_data,
                dataType: "json",
                processData: false,
                contentType: false,
                success: function(data) {
                    alert("Re forum " + data.result)
                    location.reload()
                },
                error: function() {
                    alert("POST " + "/api/SubmitForum/" + " ERROR!")
                }
            })
        }
    })
}

//获取地址参数
function getQueryString(name) {
    var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i')
    var r = window.location.search.substr(1).match(reg)
    if (r != null) {
        return unescape(r[2])
    }
    return null
}