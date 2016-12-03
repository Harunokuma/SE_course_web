$(document).ready(function() {
	//示范数据
    example_homeworkCreate_data = {
        homeworkName: 'test name',
        homeworkContent: 'test content<br>test content<br>test content<br>test content<br>test content<br>',
        DDL: '12/25/2016',
        startTime: '12/04/2016',
        classList: [{
            classID: '00000',
            className: 'SEM',
            classTime: '周五 345',
            isSelect: 'Y'
        }, {
            classID: '00001',
            className: 'SER',
            classTime: '周三 345',
            isSelect: 'N'
        }, {
            classID: '00002',
            className: 'SET',
            classTime: '周一 345',
            isSelect: 'N'
        }]
    }

    //判断模式是新建、编辑还是重发
    var mode = getQueryString("mode")
    var userID = localStorage.getItem("ID")
    var homeworkID = getQueryString("homeworkID")
    var homeworkCreate_data
    var homeworkCreate_url

    if (mode == null) {
        homeworkCreate_url = "/api/intoReleaseHomework/"
        homeworkCreate_data = { userID: userID }
    } else if (mode == "edit" || mode == "repost") {
        homeworkCreate_url = "/api/ShowHomeworkEdit/"
        homeworkCreate_data = { homeworkID: homeworkID, userID: userID }
    }

    $.ajax({
        url: homeworkCreate_url,
        type: "post",
        data: homeworkCreate_data,
        dataType: "json",
        success: function(data) {
            if (mode == null) {
                data.startTime = "1/1/2016"
                data.DDL = "1/1/2016"
            }
            data.homeworkContent = data.homeworkContent.replace(/<br>/g, "\n")
            template.config('escape', false)
            $("section.content").html(template('main_template', data))
            submitHomeworkCreate()
        },
        error: function() {
            alert("POST " + homeworkCreate_url + " ERROR!")
            if (mode == null) {
                example_homeworkCreate_data.startTime = "1/1/2016"
                example_homeworkCreate_data.DDL = "1/1/2016"
            }
            data.homeworkContent = data.homeworkContent.replace(/<br>/g, "\n")
            template.config('escape', false)
            $("section.content").html(template('main_template', example_homeworkCreate_data))
            submitHomeworkCreate()
        }
    })
})

//确认作业的发布
function submitHomeworkCreate() {
    $("#submitHomeworkCreate").click(function() {
        var mode = getQueryString("mode")
        var userID = localStorage.getItem("ID")
        var homeworkID
        var name = $("#homeworkName").val()
        var content = $("#homeworkContent").val()
        var classID = $("option[selected='selected']").data("id")
        var time = $("#reservationtime").val()
        time = time.split(" - ")
        var startTime = time[0]
        var DDL = time[1]

        //ID为-1时为新建作业，否则为编辑原有作业
        if (mode == null || mode == "repost")
            homeworkID = "-1"
        else if (mode == "edit")
            homeworkID = getQueryString("homeworkID")

        var submitHomeworkCreate_data = new FormData()
        submitHomeworkCreate_data.append("userID", userID)
        submitHomeworkCreate_data.append("homeworkID", homeworkID)
        submitHomeworkCreate_data.append("name", name)
        submitHomeworkCreate_data.append("content", content)
        submitHomeworkCreate_data.append("classID", classID)
        submitHomeworkCreate_data.append("startTime", startTime)
        submitHomeworkCreate_data.append("DDL", DDL)
        submitHomeworkCreate_data.append("docFile", $("#UpFile")[0].files[0])

        $.ajax({
            url: "/api/ReleaseHomework/",
            type: "post",
            data: submitHomeworkCreate_data,
            processData: false,
            contentType: false,
            success: function(data) {
                alert("upload " + data.result + "!")
            },
            error: function() {
                alert("POST ERROR")
            }
        })
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
