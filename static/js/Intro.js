$(document).ready(function() {
    //示范用的数据
    example_intro_data = {
        introList: [{
            name: 'SEM',
            content: 'this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>',
            srcOfPic: '/static/src/neko1.jpg'
        }, {
            name: 'SEM1',
            content: 'this is SEM',
            srcOfPic: '/static/src/neko2.jpg'
        }, {
            name: 'SEM2',
            content: 'this is SEM',
            srcOfPic: '/static/src/neko3.jpg'
        }]
    }

    //根据不同的页面选择不同的接口
    var pageName = window.location.pathname
    var getUrl = ""
    if (pageName.indexOf("CourseIntro") != -1)
        getUrl = "/api/Courseintro/"
    else if (pageName.indexOf("TeacherIntro"))
        getUrl = "/api/TeacherIntro/"

    //向服务器请求页面数据
    $.ajax({
        url: getUrl,
        type: "get",
        dataType: "json",
        success: function(data) {
            initIntroTemplate(data)
        },
        error: function() {
            alert("GET " + getUrl + " ERROR!")
        }
    })
})

//根据返回的数据渲染页面
function initIntroTemplate(data) {
    template.config('escape', false)
    $("section.content").html(template('main_template', data))
    addIntro()
}

//显示添加介绍的模态框
$("#PlusButton").click(function() {
    $("#AddModal").modal()
})

//添加介绍信息的按钮触发函数
function addIntro() {
    $("#addCourseIntro").click(function() {
        var name = $("#CourseName").val()
        var content = $("#CourseIntro").val()
        var form = new FormData()
        form.append("name", name)
        form.append("content", content)
        form.append("img", $("#UpImg")[0].files[0])
        $.ajax({
            url: "/api/AddCourseintro/",
            type: "post",
            data: form,
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

    $("#addTeacherIntro").click(function() {
        var name = $("#TeacherName").val()
        var content = $("#TeacherIntro").val()
        var form = new FormData()
        form.append("name", name)
        form.append("content", content)
        form.append("img", $("#UpImg")[0].files[0])
        $.ajax({
            url: "/api/AddTeacherintro/",
            type: "post",
            data: form,
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
