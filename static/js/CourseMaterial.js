$(document).ready(function() {
    data = {
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
    $("section.content").html(template('main_template', data))
    $("[name='MaterialPlus']").click(function() {
    	var name = $(this).data("name")
    	var id = $(this).data("id")
        $("#AddModal").modal()
        $("#ClassName").val(name)
        $("#ClassName").data("id", id)
    })
})
