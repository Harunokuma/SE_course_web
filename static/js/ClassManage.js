$(document).ready(function() {
    data = {
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
    template.config('escape', false)
    $("div#main_tem").html(template('main_template', data))
    $("#aaa").click(function() {
        $("div#student_tem").html(template('student_template', data))
        $("#checkAll").click(function() {
            var status = this.checked
            var boxs = document.getElementsByName("sub")
            for (var i = 0; i < boxs.length; i++) {
                var box = boxs[i]
                box.checked = status
            }
        })
        $("[name='StudentPlus']").click(function() {
            $("#studentAdd").modal();
        });
        $("[name='StudentDelete']").click(function() {
            $("#studentDelete").modal();
        });
        $("[name='ChangeGroup']").click(function() {
            $("#changeGroup").modal();
        });
        $("[name='SendMessage']").click(function() {
            $("#sendMessage").modal();
        });
    })
    $("[name='ClassPlus']").click(function() {
        $("#classAdd").modal();
    });


})
