//自执行检查是否未登录
(function isLogin()
{
  if(localStorage.getItem("ID") == null)
      window.location.href = "../Login/"
}())

$(document).ready(function() {
    var pageName = window.location.pathname;
    if (pageName.indexOf("CourseIntro") != -1)
        pageName = "CI";
    else if (pageName.indexOf("TeacherIntro") != -1)
        pageName = "TI";
    else if (pageName.indexOf("Course") != -1 || pageName.indexOf("Material") != -1 || pageName.indexOf("Media") != -1)
        pageName = "CW";
    else if (pageName.indexOf("Homework") != -1)
        pageName = "HS";
    else if (pageName.indexOf("ClassManage") != -1)
        pageName = "CM";
    else if (pageName.indexOf("BBS") != -1 || pageName.indexOf("forum") != -1)
        pageName = "BBS";
    else
        pageName = "normal";

    //加载Profile模态框
    $("html").append("<div id='modal'></div>");
    $("div#modal").load("../../static/StaticPage/ProfileModal.html");

    $("header.main-header").load("../../static/StaticPage/main-header.html", function() {

        //登出时跳转至登陆界面，并将账号信息清空
        $("#Signout").click(function() {
            localStorage.removeItem("ID");
            localStorage.removeItem("Identity");
            localStorage.removeItem("Name");
            window.location.href = "../Login/";
        });

        //打开模态框
        $("#profile").click(function() {
            $("#mymodal").modal();
            LoadProfile()
            ChangeProfile()
        });
        
        ModifyPage();
    });

    $("aside.main-sidebar").load("../../static/StaticPage/main-sidebar.html", function() {
        if (pageName != "normal")
            $("li#sidebar-" + pageName).addClass("active");
        ModifyPage();
    });

    $("footer.main-footer").load("../../static/StaticPage/main-footer.html");
});

function LoadProfile(){
    var userID = localStorage.getItem("ID")
    var loadProfile_data = {userID: userID}

    $.ajax({
        url: "/api/UserInfo/",
        type: "post",
        data: loadProfile_data,
        dataType: "json",
        success: function(data){
            $("#ProfileName").val(data.name)
            $("#ProfileQues").val(data.question)
            $("#ProfileAns").val(data.answer)
            $("#ProfilePass").val(data.password)
        },
        error: function(){
            alert("POST " + "/api/UserInfo/" + " ERROR!")
        }
    })
}

function ChangeProfile(){
    $("#ChangeProfile").click(function(){
        var userID = localStorage.getItem("ID")
        var name = $("#ProfileName").val()
        var question = $("#ProfileQues").val()
        var answer = $("#ProfileAns").val()
        var password = $("#ProfilePass").val()
        var changeProfile_data = {
            userID: userID,
            name: name,
            question: question,
            answer: answer,
            password: password
        }

        $.ajax({
            url: "/api/ChangeUserInfo/",
            type: "post",
            data: changeProfile_data,
            dataType: "json",
            success: function(data){
                alert("Change profile " + data.result)
            },
            error: function(){
                alert("POST ERROR!")
            }
        })
    })
}


function ModifyPage() {
    identity = localStorage.getItem("Identity");
    name = localStorage.getItem("Name");
    if (identity == 'T') //如果用户为老师
    {
        $("#tree-HL").remove();
        $("[name='UserType']").html("Teacher");
    } else if (identity == 'A') {
        $("#sidebar-HS").remove();
        $("#PlusButton").remove();
        $("#sidebar-CM").remove();
        $("[name='UserType']").html("Administrator");
    } else if (identity == 'S') {
        $("#tree-HM").remove();
        $("#tree-HC").remove();
        $("#sidebar-CM").remove();
        $("#PlusButton").remove();
        $("[name='MaterialPlus']").remove();
        $("[name='UserType']").html("Student");
    } else if (identity == 'V') {
        $("#sidebar-CW").remove();
        $("#sidebar-HS").remove();
        $("#sidebar-CM").remove();
        $("#PlusButton").remove();
        $("[name='UserType']").html("Visitor");
    }

    $("[name='UserName']").html(name);
};
