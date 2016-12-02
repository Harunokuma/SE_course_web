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
            studentID: "3140103547",
            name: "傅文渊",
            group: "1",
            score: "100"
        }, {
            studentID: "3140103547",
            name: "傅文渊",
            group: "1",
            score: "100"
        }, {
            studentID: "3140103547",
            name: "傅文渊",
            group: "1",
            score: "100"
        }, {
            studentID: "3140103547",
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
                $("input[type='checkbox']").each(function() {
                    $(this).attr("checked", status)
                })
        })
    })
})