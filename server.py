#_*_ coding:utf-8 _*_
from flask import Flask, jsonify, redirect, url_for, request
import os
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/pages/<PageName>/')
def LoadPage(PageName):
	return app.send_static_file('pages/' + PageName +'.html')

@app.route('/')
def index():
	return redirect(url_for('LoadPage', PageName = 'Login'))





#UserSystem



@app.route('/api/UserVerify/', methods=['POST'])
def UserVerify():
	print(request.headers)
	print(request.form.get('ID'))
	userID = request.form.get('ID')
	passwd = request.form.get('password')
	if len(userID) <= 2:
		identity = 'A'
	elif len(userID) <= 4:
		identity = 'T'
	elif len(userID) <= 6:
		identity = 'S'
	else:
		identity = 'V'


	if userID == passwd:
		result = "Y"
	else:
		result = "N"

	return jsonify({'result': result, 'Identity': identity, "Name": "Nemo"})


@app.route('/api/ReturnQuestion/', methods=['POST'])
def ReturnQuestion():
    data = jsonify({'question': "whats your name?"})
    return data

@app.route('/api/TestAnswer/', methods=['POST'])
def TestAnswer():
    data = jsonify({'result': "success"})
    return data

@app.route('/api/ResetPassword/', methods=['POST'])
def ResetPassword():
    data = jsonify({'result': "success"})
    return data






#MessageSystem




@app.route('/api/CheckMessage/', methods=['POST'])
def CheckMessage():
	data = jsonify({
        'totalOfUnreadMessage': "5",
        'noticeList': [{
            'sender': "傅文渊",
            'content': "没见过未读消息啊没见过未读消息啊没见过未读消息啊",
            'time': "12/02/2016"
        }, {
            'sender': "傅文渊",
            'content': "听不懂人话啊",
            'time': "12/02/2016"
        }, {
            'sender': "傅文渊",
            'content': "你这人有毒吧",
            'time': "12/02/2016"
        }, {
            'sender': "傅文渊",
            'content': "你这人有毒吧",
            'time': "12/02/2016"
        }, {
            'sender': "傅文渊",
            'content': "你这人有毒吧",
            'time': "12/02/2016"
        }]
    })
	return data


@app.route('/api/ReadMessage/', methods=['POST'])
def ReadMessage():
    data = jsonify({'result': "success"})
    return data




#Course and Teacher System


@app.route('/api/AddCourseintro/', methods=['POST'])
def AddCourseIntro():
	file = request.files['img']
	name = request.form.get('name')
	file.save(os.path.join('upload', name + '.jpg'))
	return jsonify({'result': 'success'})

@app.route('/api/Courseintro/', methods=['GET'])
def CourseIntro():
	data = jsonify({
		'introList' : [{
			'name': 'SEM',
			'content': 'this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>',
			'srcOfPic': '../../static/src/neko1.jpg'
		},{
			'name': 'SEM1',
			'content': 'this is SEM',
			'srcOfPic': '../../static/src/neko2.jpg'
		},{
			'name': 'SEM2',
			'content': 'this is SEM',
			'srcOfPic': '../../static/src/neko3.jpg'
		}]
	})
	return data

@app.route('/api/AddTeacherintro/', methods=['POST'])
def AddTeacherIntro():
	file = request.files['img']
	name = request.form.get('name')
	file.save(os.path.join('upload', name + '.jpg'))
	return jsonify({'result': 'success'})

@app.route('/api/Teacherintro/', methods=['GET'])
def TeacherIntro():
	data = jsonify({
		'introList' : [{
			'name': '刘玉生',
			'content': 'this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>this is SEM<br>',
			'srcOfPic': '../../static/src/neko1.jpg'
		},{
			'name': '邢卫',
			'content': 'this is SEM',
			'srcOfPic': '../../static/src/neko2.jpg'
		},{
			'name': '金波',
			'content': 'this is SEM',
			'srcOfPic': '../../static/src/neko3.jpg'
		}]
	})
	return data



#Material System



@app.route('/api/GetCourseMaterial/', methods=['POST'])
def GetCourseMaterial():
    data = jsonify({
        'classList': [{
            'classID': 'SEM0001',
            'className': 'SEM',
            'teacherName': '刘玉生',
            'classTime': '星期五 345',
            'srcList': [{
                'srcName': 'ch1',
                'srcUrl': 'test_url',
                'urlOfPic': '../../static/set/dist/img/default-50x50.gif'
            }, {
                'srcName': 'ch2',
                'srcUrl': 'test_url',
                'urlOfPic': '/static/set/dist/img/default-50x50.gif'
            }]
        }, {
            'classID': 'SEM0002',
            'className': 'SEM',
            'teacherName': '刘玉生1',
            'classTime': '星期五 345',
            'srcList': [{
                'srcName': 'ch1',
                'srcUrl': 'test_url',
                'urlOfPic': '/static/set/dist/img/default-50x50.gif'
            }, {
                'srcName': 'ch2',
                'srcUrl': 'test_url',
                'urlOfPic': '/static/set/dist/img/default-50x50.gif'
            }]
        }]
        })
    return data



#Homework System



@app.route('/api/HomeworkList/', methods=['POST'])
def HomeworkList():
    data = jsonify({     
        'classList': [{
            'classID': 'SEM0001',
            'className': 'SEM',
            'teacherName': '刘玉生',
            'classTime': '星期五 345',
            'homeworkList':[{
                'homeworkID': '00000',
                'homeworkName': 'test title',
                'homeworkContent': 'anything<br>anything',
                'DDL': '2016-12-20',
                'status': 'T'
            },{
                'homeworkID': '00001',
                'homeworkName': 'test title',
                'homeworkContent': 'anything<br>anything<br>anything<br>anything<br>anything<br>',
                'DDL': '2016-12-20',
                'status': 'D'
            },{
                'homeworkID': '00002',
                'homeworkName': 'test title',
                'homeworkContent': 'anything<br>anything<br>anything<br>anything<br>anything<br>',
                'DDL': '2016-12-20',
                'status': 'U'
            }]
        },{
            'classID': 'SEM0002',
            'className': 'SEM',
            'teacherName': '刘玉生',
            'classTime': '星期五 789',
            'homeworkList':[{
                'homeworkID': '00000',
                'homeworkName': 'test title',
                'homeworkContent': 'anything<br>anything<br>anything<br>anything<br>anything<br>',
                'DDL': '2016-12-20',
                'status': 'T'
            },{
                'homeworkID': '00001',
                'homeworkName': 'test title',
                'homeworkContent': 'anything<br>anything<br>anything<br>anything<br>anything<br>',
                'DDL': '2016-12-20',
                'status': 'D'
            },{
                'homeworkID': '00002',
                'homeworkName': 'test title',
                'homeworkContent': 'anything<br>anything<br>anything<br>anything<br>anything<br>',
                'DDL': '2016-12-20',
                'status': 'U'
            }]
        }]
    })
    return data

@app.route('/api/Homework/', methods=['POST'])
def Homework():
    data = jsonify({
            'homeworkName': 'test name',
            'homeworkContent': 'test<br>test<br>test<br>test<br>test<br>test<br>',
            'teacherName': 'Mr.J',
            'url': '#',
            'DDL': '12/01/2016',
            'eventList': [{
                'type': 'CHECK',
                'body': '零分',
                'timeToNow': '28 mins ago'
            }, {
                'type': 'COMMENT',
                'body': '强无敌',
                'timeToNow': '5 hours ago'
            }, {
                'type': 'STOP',
                'body': '',
                'timeToNow': '2 days ago'
            }, {
                'type': 'COMMIT',
                'body': '',
                'timeToNow': '3 days ago'
            }, {
                'type': 'POST',
                'body': '',
                'timeToNow': '5 days ago'
            }]
        })
    return data

@app.route('/api/HomeworkManage/', methods=['POST'])
def HomeworkManage():
    data = jsonify({
        'classList' : [{
            'classID': 'SEM0001',
            'className': 'SEM',
            'teacherName': '刘玉生',
            'classTime': '星期五 345',
            'homeworkList':[{
                'homeworkID': '00000',
                'homeworkName': 'test title',
                'homeworkContent': 'anything<br>anything',
                'DDL': '2016-12-20',
                'status': 'T'
            },{
                'homeworkID': '00001',
                'homeworkName': 'test title',
                'homeworkContent': 'anything<br>anything<br>anything<br>anything<br>anything<br>',
                'DDL': '2016-12-20',
                'status': 'D'
            },{
                'homeworkID': '00002',
                'homeworkName': 'test title',
                'homeworkContent': 'anything<br>anything<br>anything<br>anything<br>anything<br>',
                'DDL': '2016-12-20',
                'status': 'U'
            }]
        },{
            'classID': 'SEM0002',
            'className': 'SEM',
            'teacherName': '刘玉生',
            'classTime': '星期五 789',
            'homeworkList':[{
                'homeworkID': '00000',
                'homeworkName': 'test title',
                'homeworkContent': 'anything<br>anything<br>anything<br>anything<br>anything<br>',
                'DDL': '2016-12-20',
                'status': 'T'
            },{
                'homeworkID': '00001',
                'homeworkName': 'test title',
                'homeworkContent': 'anything<br>anything<br>anything<br>anything<br>anything<br>',
                'DDL': '2016-12-20',
                'status': 'D'
            },{
                'homeworkID': '00002',
                'homeworkName': 'test title',
                'homeworkContent': 'anything<br>anything<br>anything<br>anything<br>anything<br>',
                'DDL': '2016-12-20',
                'status': 'U'
            }]
        }]
    })
    return data

@app.route('/api/intoGradeHomework/', methods=['POST'])
def intoGradeHomework():
    data = jsonify({
        'homeworkName': 'test name',
        'homeworkContent': 'test<br>test<br>test<br>test<br>test<br>test<br>',
        'totalOfHomeworkSubmit': '50',
        'totalOfUngradeHomeworkSubmit': '35',
        'studentID': '3140100001',
        'studentName': '春天的熊',
        'srcUrl': '#',
        'srcName': 'part1.pdf'
    })
    return data

@app.route('/api/intoReleaseHomework/', methods=['POST'])
def intoReleaseHomework():
    data = jsonify({
        'homeworkName': 'test name',
        'homeworkContent': 'test content<br>test content<br>test content<br>test content<br>test content<br>',
        # DDL: '12/25/2016',
        # startTime: '12/04/2016',
        'classList': [{
            'classID': '00000',
            'className': 'SEM',
            'classTime': '周五 345',
            'isSelect': 'Y'
        }, {
            'classID': '00001',
            'className': 'SER',
            'classTime': '周三 345',
            'isSelect': 'N'
        }, {
            'classID': '00002',
            'className': 'SET',
            'classTime': '周一 345',
            'isSelect': 'N'
        }]
        })
    return data

@app.route('/api/ShowHomeworkEdit/', methods=['POST'])
def ShowHomeworkEdit():
    data = jsonify({
        'homeworkName': 'test name',
        'homeworkContent': 'test content<br>test content<br>test content<br>test content<br>test content<br>',
        'DDL': '12/25/2016',
        'startTime': '12/04/2016',
        'classList': [{
            'classID': '00000',
            'className': 'SEM',
            'classTime': '周五 345',
            'isSelect': 'Y'
        }, {
            'classID': '00001',
            'className': 'SER',
            'classTime': '周三 345',
            'isSelect': 'N'
        }, {
            'classID': '00002',
            'className': 'SET',
            'classTime': '周一 345',
            'isSelect': 'N'
        }]
        })
    return data




#Class System



@app.route('/api/ClassManage/', methods=['POST'])
def ClassManage():
    data = jsonify({
        'classList': [{
            'classID': '00000',
            'className': 'SEM',
            'classTime': '周五 345',
            'teacherName': '刘玉生'
        }, {
            'classID': '00001',
            'className': 'SER',
            'classTime': '周三 345',
            'teacherName': '刘玉生'
        }, {
            'classID': '00002',
            'className': 'SET',
            'classTime': '周一 345',
             'teacherName': '刘玉生'
        }]
        })
    return data


@app.route('/api/intoClass/', methods=['POST'])
def IntoClass():
    data = jsonify({
        'studentList': [{
            'studentID': '00000',
            'name': 'fwy',
            'group': '3',
            'score': '100'
        }, {            'studentID': '00000',
            'name': 'fwy',
            'group': '3',
            'score': '100'
        }, {            'studentID': '00000',
            'name': 'fwy',
            'group': '3',
            'score': '100'
        }, {            'studentID': '00000',
            'name': 'fwy',
            'group': '3',
            'score': '100'
        }]
        })
    return data


#BBS System


@app.route('/api/BBS/', methods=['POST'])
def BBS():
    data = jsonify({
        'areaList': [{
            'areaID': '00000',
            'areaName': 'SEM',
        }, {
            'areaID': '00010',
            'areaName': 'SEDM',
        }],
        'forumsList': [{
            'forumsID': '00001',
            'forumsName': 'xuxuxu',
            'userName': 'fwy',
            'time': '12/20/2016',
            'lastTime': '13/20/2016'
        }, {
            'forumsID': '00001',
            'forumsName': 'xuxuxu',
            'userName': 'fwy',
            'time': '12/20/2016',
            'lastTime': '14/20/2016'
        }]
        })
    return data


@app.route('/api/Forum/', methods=['POST'])
def Forum():
    data = jsonify({
        'forumList': [{
            'userName': '00dsfsd001',
            'content': 'xuxsagasguxu',
            'time': '12/20/2016',
            'url': 'www.baidu.com',
            'fileName': 'baibu'
        }, {
            'userName': '00sdfsdf001',
            'content': 'xuxusdfsaxu',
            'time': '12/20/2016',
            'url': '',
            'fileName': ''
        }]
        })
    return data






if __name__ == '__main__':
    app.run(debug=True)

