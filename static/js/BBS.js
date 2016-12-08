$(document).ready(function() {
    example_BBS_data = {
        areaList: [{
            areaID: "1",
            areaName: "软件需求工程 刘玉生老师 周五3.4.5节"
        }, {
            areaID: "2",
            areaName: "软件工程管理 金波老师 周三3.4.5节"
        }],
        forumsList: [{
            forumsID: "1",
            forumsName: "你追我",
            userName: "傅文渊",
            time: "12/01/2016",
            lastTime: "12/01/2016"
        }, {
            forumsID: "2",
            forumsName: "如果你追到我",
            userName: "傅文渊",
            time: "12/01/2016",
            lastTime: "12/01/2016"
        }, {
            forumsID: "3",
            forumsName: "我就和你嘿嘿嘿",
            userName: "傅文渊",
            time: "12/01/2016",
            lastTime: "12/01/2016"
        }]
    }

    var areaID = getQueryString("areaID")
    var userID = localStorage.getItem("ID")
    var BBS_data = { areaID: areaID, userID: userID }

    $.ajax({
        url: "/api/BBS/",
        type: "post",
        data: BBS_data,
        dataType: "json",
        success: function(data) {
            template.config('escape', false)
            $("section.content").html(template('main_template', data))
            CreateForum()
        },
        error: function() {
            alert("POST " + "/api/BBS/" + " ERROR!")
        }
    })
})

//发布新帖
function CreateForum() {
    $("#CreateForum").click(function() {
        var userID = localStorage.getItem("ID")
        var areaID = getQueryString("areaID")
        var title = $("#ForumTitle").val()
        var content = $("#ForumContent").val()
        var createForum_data = new FormData()
        createForum_data.append("userID", userID)
        createForum_data.append("areaID", areaID)
        createForum_data.append("title", title)
        createForum_data.append("content", content)
        try {
            createForum_data.append("srcFile", $("#UpFile")[0].files[0])
        } finally {
            $.ajax({
                url: "/api/CreateForum/",
                type: "post",
                data: createForum_data,
                dataType: "json",
                processData: false,
                contentType: false,
                success: function(data) {
                    alert("Create forum " + data.result)
                    location.reload()
                },
                error: function() {
                    alert("POST " + "/api/CreateForum/" + " ERROR!")
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
