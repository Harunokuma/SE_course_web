$(document).ready(function() {
    example_data = {
        classList: [{
            classID: 'SEM0001',
            className: 'SEM',
            teacherName: '刘玉生',
            classTime: '星期五 345',
            srcList: [{
                srcName: 'ch1',
                srcUrl: 'test_url',
                urlOfPic: '../../static/set/dist/img/default-50x50.gif'
            }, {
                srcName: 'ch2',
                srcUrl: 'test_url',
                urlOfPic: '../../static/set/dist/img/default-50x50.gif'
            }]
        }, {
            classID: 'SEM0002',
            className: 'SEM',
            teacherName: '刘玉生1',
            classTime: '星期五 345',
            srcList: [{
                srcName: 'ch1',
                srcUrl: 'test_url',
                urlOfPic: '../../static/set/dist/img/default-50x50.gif'
            }, {
                srcName: 'ch2',
                srcUrl: 'test_url',
                urlOfPic: '../../static/set/dist/img/default-50x50.gif'
            }]
        }]
    }

    //判断是哪个页面
    var pageName = window.location.pathname
    var userID = localStorage.getItem('ID')
    var type = ""
    if (pageName.indexOf("Courseware") != -1)
        type = "Courseware"
    else if (pageName.indexOf("RefeMaterial") != -1)
        type = "RefeMaterial"
    else if (pageName.indexOf("MultiMedia") != -1)
        type = "MultiMedia"
    else if (pageName.indexOf("OtherMaterial") != -1)
        type = "OtherMaterial"

    var material_data = { userID: userID, type: type }
    $.ajax({
        url: "/api/GetCourseMaterial/",
        type: "post",
        data: material_data,
        dataType: "json",
        success: function(data) {
            template.config('escape', false)
            $("section.content").html(template('main_template', data))
            //监控添加资料按键
            MaterialPlus(type)
        },
        error: function() {
            alert("POST " + "/api/GetCourseMaterial/" + " ERROR!")
        }
    })
})

//按下添加资料按键时，弹出模态框
function MaterialPlus(type) {
    $("[name='MaterialPlus']").click(function() {
        var name = $(this).data("name")
        var id = $(this).data("id")
        $("#AddModal").modal()
        $("#ClassName").val(name)
        $("#ClassName").data("id", id)
        $("#addCourseMaterial").click(function(){
            AddMaterial(type)
        })
    })
}

//确认添加时，向服务器发送数据
function AddMaterial(type) {
    var classID = $("#ClassName").data("id")
    var srcName = $("#CourseMaterialName").val()
    var userID = localStorage.getItem("ID")
    var addMaterial_data = new FormData()
    addMaterial_data.append("userID", userID)
    addMaterial_data.append("classID", classID)
    addMaterial_data.append("srcName", srcName)
    addMaterial_data.append("type", type)
    addMaterial_data.append("srcFile", $("#UpFile")[0].files[0])
    $.ajax({
        url: "/api/AddCourseMaterial/",
        type: "post",
        data: addMaterial_data,
        processData: false,
        contentType: false,
        success: function(data) {
            alert("upload " + data.result + "!")
        },
        error: function() {
            alert("POST ERROR")
        }
    })
}
