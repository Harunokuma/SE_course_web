$(document).ready(function() {
    example_classManage_data = {
        classList: [{
            classID: "1",
            className: "软件需求工程",
            teacherName: "刘玉生",
            classTime: "周五3.4.5节"
        }, {
            classID: "2",
            className: "软件工程管理",
            teacherName: "金波",
            classTime: "周三3.4.5节"
        }],
        studentList: [{
            studentID: "3140103547",
            name: "傅文渊",
            group: "1",
            score: "100"
        }, {
            studentID: "3140103548",
            name: "傅文渊",
            group: "1",
            score: "100"
        }, {
            studentID: "3140103549",
            name: "傅文渊",
            group: "1",
            score: "100"
        }, {
            studentID: "3140103540",
            name: "傅文渊",
            group: "1",
            score: "100"
        }, {
            studentID: "3140103541",
            name: "傅文渊",
            group: "1",
            score: "100"
        }]
    }

    var userID = localStorage.getItem("ID")
    classManage_data = { userID: userID }

    $.ajax({
        url: "/api/ClassManage/",
        type: "POST",
        data: classManage_data,
        dataType: "json",
        success: function(data) {
            template.config('escape', false)
            $("div#main_tem").html(template('main_template', data))
                //点击班级后载入学生信息
            loadStudent()
                //点击添加班级后弹出模态框
            $("[name='ClassPlus']").click(function() {
                $("#classAdd").modal();
                $("#submitAddClass").click(function() {
                    var userID = localStorage.getItem("ID")
                    var courseName = $("#CourseName").val()
                    var classTime = $("#ClassTime").val()
                    var addClass_data = { userID: userID, courseName: courseName, classTime: classTime }
                    $.ajax({
                        url: "/api/AddClass/",
                        type: "post",
                        data: addClass_data,
                        dataType: "json",
                        success: function(data) {
                            alert("Add class " + data.result)
                        },
                        error: function() {
                            alert("POST " + "/api/AddClass/" + " ERROR!")
                        }
                    })
                })
            });
        },
        error: function() {
            alert("POST " + "/api/ClassManage/" + " ERROR!")
            
            // template.config('escape', false)
            // $("div#main_tem").html(template('main_template', example_classManage_data))
            // loadStudent()
            // $("[name='ClassPlus']").click(function() {
            //     $("#classAdd").modal();
            // });
        }
    })


})

function loadStudent() {
    $("[name='ClassLabel']").click(function() {
        var classID = $(this).data("id")
        var intoClass_data = { classID: classID }

        $.ajax({
            url: "/api/intoClass/",
            type: "post",
            data: intoClass_data,
            dataType: "json",
            success: function(data) {
                template.config('escape', false)
                $("div#student_tem").html(template('student_template', data))
                $("#stuList").data("id", classID)
                $("#checkAll").click(function() {
                    var status = this.checked
                    var boxs = document.getElementsByName("sub")
                    for (var i = 0; i < boxs.length; i++) {
                        var box = boxs[i]
                        box.checked = status
                    }
                })
                loadModal()
            },
            error: function() {
                alert("POST " + "/api/intoClass/" + " ERROR!")
                // template.config('escape', false)
                // $("div#student_tem").html(template('student_template', example_classManage_data))
                // loadModal()
            }
        })
    })
}

function loadModal() {
    //添加学生的模态框操作
    $("[name='StudentPlus']").click(function() {
        $("#studentAdd").modal();
        $("#submitAddStudent").click(function() {
            var studentID = $("#StudentID").val()
            var classID = $("stuList").data("id")
            var addStudent_data = { studentID: studentID, classID: classID }
            $.ajax({
                url: "/api/AddStudent/",
                type: "post",
                data: addStudent_data,
                dataType: "json",
                success: function(data) {
                    alert("Add student " + data.result)
                },
                error: function() {
                    alert("POST " + "/api/AddStudent/" + " ERROR!")
                }
            })
        })
    })

    //删除学生的模态框操作
    $("[name='StudentDelete']").click(function() {
        $("#studentDelete").modal();

        //显示删除学生列表
        var deleteList = getChecked()
        $("#Student-delete").html("")
        for (var i = 0; i < deleteList.length; i++) {
            var stu = deleteList[i]
            $("#Student-delete").append(stu.studentID + " ")
            $("#Student-delete").append(stu.studentName + "\n")
        }
        //确认删除学生
        $("#submitDeleteStudent").click(function(){
            var studentList = []
            for (var i = 0; i < deleteList.length; i++) {
                var stu = deleteList[i]
                studentList.push({ studentID: stu.studentID })
            }
            var classID = $("#stuList").data("id")
            var deleteStudent_data = { studentList: studentList, classID: classID }

            $.ajax({
                url: "/api/DeleteStudent/",
                type: "post",
                data: deleteStudent_data,
                dataType: "json",
                success: function(data) {
                    alert("Delete student " + data.result)
                },
                error: function() {
                    alert("POST " + "/api/DeleteStudent/" + " ERROR!")
                }
            }) 
        })

    })

    //改变学生分组的模态框操作
    $("[name='ChangeGroup']").click(function() {
        $("#changeGroup").modal();

        //确认改变分组操作
        $("#submitChangeGroup").click(function(){
            var checkedList = getChecked()
            var studentList = []
            for (var i = 0; i < checkedList.length; i++) {
                var stu = checkedList[i]
                studentList.push({ studentID: stu.studentID })
            }
            var classID = $("#stuList").data("id")
            var group = $("#Group").val()
            var changeGroup_data = { classID: classID, studentList: studentList, group: group }

            $.ajax({
                url: "/api/ChangeGroup/",
                type: "post",
                data: changeGroup_data,
                dataType: "json",
                success: function(data) {
                    alert("Change group " + data.result)
                },
                error: function() {
                    alert("POST " + "/api/ChangeGroup/" + " ERROR!")
                }
            })
        })
    })

    //发送通知的模态框操作
    $("[name='SendMessage']").click(function() {
        $("#sendMessage").modal();
        //确认发送通知的操作
        $("#submitSendMessage").click(function(){
            var checkedList = getChecked()
            var studentList = []
            for (var i = 0; i < checkedList.length; i++) {
                var stu = checkedList[i]
                studentList.push({ studentID: stu.studentID })
            }
            var classID = $("#stuList").data("id")
            var content = $("#Content").val()
            var userID = localStorage.getItem("ID")
            var sendMessage_data = {
                userID: userID,
                classID: classID,
                studentList: studentList,
                content: content
            }
            $.ajax({
                url: "/api/SendMessage/",
                type: "post",
                data: sendMessage_data,
                dataType: "json",
                success: function(data) {
                    alert("Send message " + data.result)
                },
                error: function() {
                    alert("POST " + "/api/SendMessage/" + " ERROR!")
                }
            })
        })
    })
}

function getChecked() {
    var studentList = []
    var boxs = document.getElementsByName("sub")
    for (var i = 0; i < boxs.length; i++) {
        var box = boxs[i]
        if (box.checked == true)
            studentList.push({ studentID: box.dataset.id, studentName: box.dataset.name })
    }
    return studentList
}
