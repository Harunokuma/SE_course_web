# _*_ coding:utf-8 _*_
from flask import Flask, jsonify, redirect, url_for, request
import os
from werkzeug import secure_filename
import pymysql
import time


app = Flask(__name__)


@app.route('/pages/<PageName>/')
def LoadPage(PageName):
    return app.send_static_file('pages/' + PageName + '.html')


@app.route('/')
def index():
    return redirect(url_for('LoadPage', PageName='Login'))


# UserSystem

# 后端第一次实验

@app.route('/api/UserVerify/', methods=['POST'])
def UserVerify():
    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()  # 这是后端加的

    print(request.headers)
    print(request.form.get('ID'))

    userID = request.form.get('ID')
    passwd = request.form.get('password')

    cursor.execute('select password from personal_info where userID = %s', (userID,))
    password = cursor.fetchall()
    password = password[0][0]

    cursor.execute('select userType from personal_info where userID = %s', (userID,))
    identity = cursor.fetchall()
    identity = identity[0][0]

    cursor.execute('select username from personal_info where userID = %s', (userID,))
    name = cursor.fetchall()
    name = name[0][0]

    cursor.close()
    conn.close()

    if password == passwd:
        result = "Y"
    else:
        result = "N"

    return jsonify({'result': result, 'Identity': identity, 'Name': name})


@app.route('/api/ReturnQuestion/', methods=['POST'])
def ReturnQuestion():
    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    userID = request.form.get('userID')

    cursor.execute('select question from personal_info where userID = %s', (userID,))
    question = cursor.fetchall()
    question = question[0][0]

    cursor.close()
    conn.close()

    return jsonify({'question': question})


@app.route('/api/TestAnswer/', methods=['POST'])
def TestAnswer():
    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    userID = request.form.get('userID')
    ans = request.form.get('answer')

    cursor.execute('select answer from personal_info where userID = %s', (userID,))
    answer = cursor.fetchall()
    answer = answer[0][0]

    cursor.close()
    conn.close()

    if answer == ans:
        return jsonify({'result': "success"})
    else:
        return jsonify({'result': "failed"})


@app.route('/api/ResetPassword/', methods=['POST'])
def ResetPassword():
    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    userID = request.form.get('userID')
    password = request.form.get('password')

    cursor.execute('''update personal_info
    set password = %s
    where userID = %s''', (password, userID))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'result': "success"})


@app.route('/api/UserInfo/', methods=['POST'])
def UserInfo():
    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    userID = request.form.get('userID')

    cursor.execute('select question from personal_info where userID = %s', (userID,))
    question = cursor.fetchall()
    question = question[0][0]

    cursor.execute('select username from personal_info where userID = %s', (userID,))
    name = cursor.fetchall()
    name = name[0][0]

    cursor.execute('select answer from personal_info where userID = %s', (userID,))
    answer = cursor.fetchall()
    answer = answer[0][0]

    cursor.close()
    conn.close()

    return jsonify({'name': name, 'question': question, 'answer': answer})


@app.route('/api/ChangeUserInfo/', methods=['POST'])
def ChangeUserInfo():
    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    userID = request.form.get('userID')
    name = request.form.get('name')
    question = request.form.get('question')
    answer = request.form.get('answer')
    password = request.form.get('password')

    cursor.execute('''update personal_info
    set username = %s, password = %s, question =%s, answer = %s
    where userID = %s''', (name, password, question, answer, userID))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'result': "success"})


# 已知一个问题：当输入密码长于10位时，点击登录，服务器没有反应，但是没有卡死


# MessageSystem

# 第二！

@app.route('/api/CheckMessage/', methods=['POST'])
def CheckMessage():
    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    userID = request.form.get('userID')

    cursor.execute('select sender,content,time from message where receiver = %s and readornot = 0', (userID,))
    Message = cursor.fetchall()

    NewMessage = len(Message)

    j = 0
    lz = [None] * NewMessage

    while j < NewMessage:
        d = {}
        d.fromkeys(['sender', 'content', 'time'])
        d['sender'] = Message[j][0]
        d['content'] = Message[j][1]
        d['time'] = Message[j][2]
        lz[j] = d
        j = j + 1

    cursor.close()
    conn.close()

    return jsonify({'totalOfUnreadMessage': NewMessage, 'noticeList': lz})


@app.route('/api/ReadMessage/', methods=['POST'])
def ReadMessage():
    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    userID = request.form.get('userID')

    cursor.execute('''update message
    set readornot = 1
    where receiver = %s''', (userID,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'result': "success"})


# 记录一个问题：按下“将全部消息设为已读”之后，要刷新页面，才能发现新消息为0
# 第一版本完工


# Course and Teacher System
# 第三。。


@app.route('/api/AddCourseintro/', methods=['POST'])
def AddCourseIntro():
    file = request.files['img']
    name = request.form.get('name')
    content = request.form.get('content')
    file.save(os.path.join('static/src/', name + '.jpg'))

    path = '../../static/src/' + name + '.jpg'

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    cursor.execute('insert into intro_course values(%s,%s,%s)', (name, path, content))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'result': 'success'})


@app.route('/api/Courseintro/', methods=['GET'])
def CourseIntro():
    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    cursor.execute('select count(*) from intro_course')
    number = cursor.fetchall()
    number = number[0][0]

    cursor.execute('select * from intro_course')
    teacher = cursor.fetchall()

    j = 0
    lz = [None] * number

    while j < number:
        d = {}
        d.fromkeys(['name', 'srcOfPic', 'content'])
        d['name'] = teacher[j][0]
        d['srcOfPic'] = teacher[j][1]
        d['content'] = teacher[j][2]
        lz[j] = d
        j = j + 1

    cursor.close()
    conn.close()

    return jsonify({'introList': lz})


@app.route('/api/AddTeacherintro/', methods=['POST'])
def AddTeacherIntro():
    file = request.files['img']
    name = request.form.get('name')
    content = request.form.get('content')
    file.save(os.path.join('static/src/', name + '.jpg'))

    path = '../../static/src/' + name + '.jpg'

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    cursor.execute('insert into intro_teacher values(%s,%s,%s)', (name, path, content))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'result': 'success'})


@app.route('/api/Teacherintro/', methods=['GET'])
def TeacherIntro():
    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    cursor.execute('select count(*) from intro_teacher')
    number = cursor.fetchall()
    number = number[0][0]

    cursor.execute('select * from intro_teacher')
    teacher = cursor.fetchall()

    j = 0
    lz = [None] * number

    while j < number:
        d = {}
        d.fromkeys(['name', 'srcOfPic', 'content'])
        d['name'] = teacher[j][0]
        d['srcOfPic'] = teacher[j][1]
        d['content'] = teacher[j][2]
        lz[j] = d
        j = j + 1

    cursor.close()
    conn.close()

    return jsonify({'introList': lz})


# 12.7已知问题：原有的upload图片路径有问题，upload能上传，但是不能读取。将路径调整到src
# 12.8该问题已经得到合理解决。
# 记录一个问题：保存后，虽然显示了upload success，但是窗口并没有关闭


# Material System
# 有够绕的，有点烦

@app.route('/api/GetCourseMaterial/', methods=['POST'])
def GetCourseMaterial():
    userID = request.form.get('userID')
    MaterialType = request.form.get('type')

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    cursor.execute('select userType from personal_info where userID = %s', (userID,))
    userType = cursor.fetchall()
    userType = userType[0][0]

    if userType == 'S':
        cursor.execute(
            'select count(distinct classID) from relationship natural join resource where userID = %s and type = %s',
            (userID, MaterialType))
        number = cursor.fetchall()
        number = number[0][0]  # number记载了该学生一共有多少个有该种资料的班级

        k = 0

        cursor.execute(
            'select distinct classID from relationship natural join resource where userID = %s and type = %s',
            (userID, MaterialType))
        classList = cursor.fetchall()
        class_list = number * [None]
        while k < number:
            class_list[k] = classList[k][0]
            k = k + 1  # class_list数组记载了有该种资料的班级ID

    if userType == 'T':
        cursor.execute(
            'select count(distinct classID) from class_info natural join resource where teacherID = %s and type = %s',
            (userID, MaterialType))
        number = cursor.fetchall()
        number = number[0][0]  # number记载了该老师一共有多少个有该种资料的班级

        k = 0

        cursor.execute(
            'select distinct classID from class_info natural join resource where teacherID = %s and type = %s',
            (userID, MaterialType))
        classList = cursor.fetchall()
        class_list = number * [None]
        while k < number:
            class_list[k] = classList[k][0]
            k = k + 1  # class_list数组记载了有该种资料的班级ID

    lz = number * [None]

    k = 0

    while k < number:
        cursor.execute('select classID,courseName,teacherName,classTime from class_info where classID =%s',
                       (class_list[k],))
        class_info = cursor.fetchall()
        d = {}
        d.fromkeys(['classID', 'className', 'teacherName', 'classTime', 'srcList'])
        d['classID'] = class_info[0][0]
        d['className'] = class_info[0][1]
        d['teacherName'] = class_info[0][2]
        d['classTime'] = class_info[0][3]

        cursor.execute('select count(distinct srcID) from resource where classID = %s and type = %s',
                       (class_list[k], MaterialType))
        num = cursor.fetchall()
        num = num[0][0]  # num记载了符合要求的资料的数量

        cursor.execute('select srcName,srcUrl,urlOfPic from resource where classID =%s and type = %s',
                       (class_list[k], MaterialType))
        material_info = cursor.fetchall()

        j = 0
        ls = num * [None]

        while j < num:
            e = {}
            e.fromkeys(['srcName', 'srcUrl', 'urlOfPic'])
            e['srcName'] = material_info[j][0]
            e['srcUrl'] = material_info[j][1]
            e['urlOfPic'] = material_info[j][2]
            ls[j] = e
            j = j + 1

        d['srcList'] = ls

        lz[k] = d
        k = k + 1

    cursor.close()
    conn.close()

    return jsonify({'classList': lz})


@app.route('/api/AddCourseMaterial/', methods=['POST'])
def AddCourseMaterial():
    userID = request.form.get('userID')
    classID = request.form.get('classID')
    srcName = request.form.get('srcName')
    file = request.files['srcFile']
    MaterialType = request.form.get('type')

    if MaterialType == "Courseware":
        file.save(os.path.join('static/material/', srcName + '.ppt'))
        srcUrl = '../../static/material/' + srcName + '.ppt'

    if MaterialType == "RefeMaterial":
        file.save(os.path.join('static/material/', srcName + '.pdf'))
        srcUrl = '../../static/material/' + srcName + '.pdf'

    if MaterialType == "MultiMedia":
        file.save(os.path.join('static/material/', srcName + '.mp3'))
        srcUrl = '../../static/material/' + srcName + '.mp3'

    if MaterialType == "OtherMaterial":
        file.save(os.path.join('static/material/', srcName + '.jpg'))
        srcUrl = '../../static/material/' + srcName + '.jpg'

    urlOfPic = '../../static/src/SE.jpg'

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    cursor.execute('insert into resource values(NULL,%s,%s,%s,%s,%s)',
                   (classID, srcUrl, srcName, urlOfPic, MaterialType))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'result': 'success'})


# 资料系统已知一个bug：如果一个文件都没有，就不能上传资料
# 另一个bug是前端bug，上传资料时候，后端不能正确从前端获取资料的类型
# 12.9，资料系统基本完成，第四


# Homework System

########################################################################################################################

@app.route('/api/HomeworkList/', methods=['POST']) # --- 完成 --- #
def HomeworkList():
    userID = request.form.get('userID')

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')
    cursor = conn.cursor()

    cursor.execute('select count(distinct classID) from relationship natural join homework_info where userID = %s',(userID,))
    number = cursor.fetchall()
    number = number[0][0]

    k = 0

    cursor.execute('select distinct classID from relationship natural join homework_info where userID = %s', (userID,))
    classList = cursor.fetchall()
    class_list = int(number) * [None]
    while k < number:
        class_list[k] = classList[k][0]
        k = k + 1


    HomeworkList = number * [None]

    k = 0

    while k < number:
        cursor.execute('select distinct courseName, teacherName, classTime from class_info where classID = %s', (class_list[k],))
        class_info = cursor.fetchall()
        d = {}
        d.fromkeys(['className', 'teacherName', 'classTime', 'homeworkList'])
        d['className'] = class_info[0][0]
        d['teacherName'] = class_info[0][1]
        d['classTime'] = class_info[0][2]

        cursor.execute('select count(distinct homeworkID) from homework_info where classID = %s', (class_list[k],))
        num = cursor.fetchall()
        num = num[0][0]

        cursor.execute('select distinct homeworkID, homeworkName, homeworkContent, DDL, startTime from homework_info where classID = %s',\
            (class_list[k],))
        homework_info = cursor.fetchall()

        j = 0
        ls = num * [None]

        while j < num:
            e = {}
            e.fromkeys(['homeworkID', 'homeworkName', 'homeworkContent', 'DDL', 'status'])

            e['homeworkID'] = homework_info[j][0]
            e['homeworkName'] = homework_info[j][1]
            e['homeworkContent'] = homework_info[j][2]
            e['DDL'] = homework_info[j][3]

            cursor.execute('select count(distinct eventTime) from homework_belong where homeworkID = %s and studentID = %s and eventType = 0',\
                           (e['homeworkID'], userID))
            subNum = cursor.fetchall()
            subNum = subNum[0][0]

            currentTime = time.time()

            DDL = time.mktime(time.strptime(e['DDL'], "%a %b %d %H:%M:%S %Y"))

            if currentTime <= DDL:
                if subNum == 0:
                    e['status'] = 'T'
                else:
                    e['status'] = 'D'
            else:
                if subNum == 0:
                    e['status'] = 'U'
                else:
                    cursor.execute('select distinct eventTime from homework_belong where homeworkID = %s and studentID = %s and eventType = 0\
                                    order by eventTime asc', (e['homeworkID'], userID))
                    subTime = cursor.fetchall()
                    subTime = subTime[0][0]

                    if subTime <= DDL:
                        e['status'] = 'D'
                    else:
                        e['status'] = 'U'

            ls[j] = e
            j += 1

        d['homeworkList'] = ls
        HomeworkList[k] = d

        k = k + 1

    cursor.close()
    conn.close()

    return jsonify({'classList': HomeworkList})


@app.route('/api/Homework/', methods=['POST']) # --- 完成 --- #
def Homework():
    userID = request.form.get('userID')
    homeworkID = request.form.get('homeworkID')

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')
    cursor = conn.cursor()

    cursor.execute('select homeworkName, homeworkContent, teacherID, url, DDL, startTime from homework_info where homeworkID = %s',\
        (homeworkID))
    homework_info = cursor.fetchall()
    homeworkName = homework_info[0][0]
    homeworkContent = homework_info[0][1]
    teacherID = homework_info[0][2]
    url = homework_info[0][3]
    DDL = homework_info[0][4]
    startTime = homework_info[0][5]

    cursor.execute('select username from personal_info where userID = %s', (teacherID))
    teacherName = cursor.fetchall()
    teacherName = teacherName[0][0]

    currentTime = time.time()

    cursor.execute('select count(*) from (select * from homework_belong where homeworkID = %s and studentID = %s) as derive',\
                   (homeworkID, userID))
    eventNumber = cursor.fetchall()
    eventNumber = eventNumber[0][0]
    
    if currentTime > time.mktime(time.strptime(DDL, "%a %b %d %H:%M:%S %Y")):
        eventList = (eventNumber + 2) * [None]
        start = 1
        e = {}
        e.fromkeys(['type', 'body', 'timeToNow'])
        if currentTime > time.mktime(time.strptime(DDL, "%a %b %d %H:%M:%S %Y")):
            e['type'] = 'STOP'
            e['body'] = 'past due'
            interval = currentTime - time.mktime(time.strptime(DDL, "%a %b %d %H:%M:%S %Y"))
            interval = interval / 86400
            e['timeToNow'] = '%d days ago' % interval
            eventList[0] = e
    else:
        eventList = (eventNumber + 1) * [None]
        start = 0


    cursor.execute('select eventTime from homework_belong where homeworkID = %s and studentID = %s order by eventTime DESC',\
        (homeworkID, userID))
    eventTime = cursor.fetchall()

    k = start
    while k < eventNumber + start:
        e = {}
        e.fromkeys(['type', 'body', 'timeToNow'])

        timeStamp = eventTime[k][0]
        interval = currentTime - timeStamp
        interval = interval / 86400
        e['timeToNow'] = '%d days ago' % interval
        cursor.execute('select eventType from homework_belong where homeworkID = %s and studentID = %s and eventTime = %s',\
            (homeworkID, userID, str(timeStamp)))

        etype = cursor.fetchall()
        etype = etype[0][0]

        if etype == 0:
            e['type'] = 'COMMIT'
            e['body'] = ' '

        elif etype == 1:
            cursor.execute('select grade from homework_belong where homeworkID = %s and studentID = %s and eventTime = %s',\
                (homeworkID, userID, str(timeStamp)))
            grade = cursor.fetchall()
            grade = grade[0][0]

            cursor.execute('select grade from homework_belong where homeworkID = %s and eventType = 1 order by grade desc',\
                           (homeworkID))
            gradeall = cursor.fetchall()
            n = 1
            while gradeall[n - 1][0] != grade:
                n = n + 1

            cursor.execute('select count(distinct studentID) from homework_belong where homeworkID = %s', (homeworkID))
            stuAmt = cursor.fetchall()
            stuAmt = stuAmt[0][0]

            rank = n / stuAmt

            e['type'] = 'CHECK'
            e['body'] = 'Your score is ' + str(grade) + ' and your current rank is ' + str(rank)


        elif etype == 2:
            cursor.execute('select remark from homework_belong where homeworkID = %s and studentID = %s and eventTime = %s',\
                (homeworkID, userID, str(timeStamp)))
            remark = cursor.fetchall()
            remark = remark[0][0]

            e['type'] = 'COMMENT'
            e['body'] = remark

        eventList[k] = e
        k = k + 1

    e = {}
    e.fromkeys(['type', 'body', 'timeToNow'])

    e['type'] = 'POST'
    e['body'] = ' '
    cursor.execute('select startTime from homework_info where homeworkID = %s', (homeworkID))
    postTime = cursor.fetchall()
    postTime = postTime[0][0]
    interval = currentTime - time.mktime(time.strptime(postTime, "%a %b %d %H:%M:%S %Y"))
    interval = interval / 86400
    e['timeToNow'] = '%d days ago' % interval

    eventList[eventNumber + start] = e

    cursor.close()
    conn.close()

    print(eventList)
    return jsonify({
        'homeworkName': homeworkName,
        'homeworkContent': homeworkContent,
        'teacherName': teacherName,
        'url': url,
        'DDL': DDL,
        'eventList': eventList
    })


@app.route('/api/SubmitHomework/', methods=['POST']) #上传作业
def SubmitHomework():
    userID = request.form.get('userID')
    file = request.files['srcFile']
    homeworkID = request.form.get('homeworkID')

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')
    cursor = conn.cursor()

    currentTime = time.time()
    homeworkName = str(homeworkID) + '-' + str(userID) + '-' + str(currentTime)
    srcFile = '../../static/homework/' + homeworkName + '.rar'
    file.save(os.path.join('static/homework/', homeworkName + '.rar'))

    cursor.execute('select classID from homework_info where homeworkID = %s', (homeworkID,))
    classID = cursor.fetchall()
    classID = classID[0][0]

    cursor.execute('insert into homework_belong values (%s, %s, %s, %s, %s, %s, %s, %s, %s)' \
                   , (homeworkID, userID, classID, homeworkName, srcFile, '0', ' ', '0', str(currentTime)))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'result': 'success'})


@app.route('/api/HomeworkManage/', methods=['POST']) # --- 完成 --- #
def HomeworkManage():
    userID = request.form.get('userID')

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')
    cursor = conn.cursor()

    cursor.execute('select count(distinct classID) from homework_info where teacherID = %s', (userID,))
    classNum = cursor.fetchall()
    classNum = classNum[0][0]

    classList = classNum * [None]

    cursor.execute('select distinct classID from homework_info where teacherID = %s', (userID,))
    classInfo = cursor.fetchall()

    k = 0
    while k < classNum:
        classID = classInfo[k][0]

        ch = {}
        ch.fromkeys(['classID', 'className', 'teacherName', 'classTime', 'homeworkList'])

        cursor.execute('select courseName, teacherName, classTime from class_info where classID = %s', (classID,))
        cc = cursor.fetchall()
        ch['classID'] = classID
        ch['className'] = cc[0][0]
        ch['teacherName'] = cc[0][1]
        ch['classTime'] = cc[0][2]

        cursor.execute('select count(distinct homeworkID) from homework_info where classID = %s', (classID,))
        hNum = cursor.fetchall()
        hNum = hNum[0][0]

        hl = hNum * [None]

        cursor.execute('select distinct homeworkID, homeworkName, homeworkContent, DDL from homework_info where classID = %s',(classID,))
        hf = cursor.fetchall()

        l = 0
        while l < hNum:
            hll = {}
            hll.fromkeys(['homeworkID', 'homeworkName', 'homeworkIntro', 'DDL', 'status'])

            hll['homeworkID'] = hf[l][0]
            hll['homeworkName'] = hf[l][1]
            hll['homeworkIntro'] = hf[l][2][: 50]
            hll['DDL'] = hf[l][3]


            currentTime = time.time()
            if currentTime >= time.mktime(time.strptime(hll['DDL'], "%a %b %d %H:%M:%S %Y")):
                hll['status'] = 'D'
            else:
                hll['status'] = 'T'

            hl[l] = hll

            l = l + 1

        ch['homeworkList'] = hl
        classList[k] = ch

        k = k + 1

    cursor.close()
    conn.close()

    return jsonify({'classList': classList})


@app.route('/api/ShowHomeworkEdit/', methods=['POST']) # --- 完成 --- #
def ShowHomeworkEdit():
    homeworkID = request.form.get('homeworkID')
    userID = request.form.get('userID')

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')
    cursor = conn.cursor()

    cursor.execute('select homeworkName, homeworkContent, DDL, startTime from homework_info where homeworkID = %s',(homeworkID,))
    homework_info = cursor.fetchall()

    homeworkName = homework_info[0][0]
    homeworkContent = homework_info[0][1]
    DDL = homework_info[0][2]
    startTime = homework_info[0][3]

    DDL = time.strftime("%m/%d/%Y", time.localtime(time.mktime(time.strptime(DDL, "%a %b %d %H:%M:%S %Y"))))
    startTime = time.strftime("%m/%d/%Y", time.localtime(time.mktime(time.strptime(startTime, "%a %b %d %H:%M:%S %Y"))))

    cursor.execute('select classID from homework_info where homeworkID = %s', (homeworkID,))
    classSelec = cursor.fetchall()
    classSelec = classSelec[0][0]

    cursor.execute('select count(distinct classID) from class_info where teacherID = %s', (userID,))
    classNum = cursor.fetchall()
    classNum = classNum[0][0]

    classList = classNum * [None]

    cursor.execute('select classID, courseName, classTime from class_info where teacherID = %s', (userID,))
    classl = cursor.fetchall()

    k = 0
    while k < classNum:
        c = {}
        c.fromkeys(['classID, className, classTime, isSelect'])

        c['classID'] = classl[k][0]
        c['className'] = classl[k][1]
        c['classTime'] = classl[k][2]

        if (classl[k][0] == classSelec):
            c['isSelect'] = 'Y'
        else:
            c['isSelect'] = 'N'

        classList[k] = c

        k = k + 1

    cursor.close()
    conn.close()

    return jsonify({
        'homeworkName': homeworkName,
        'homeworkContent': homeworkContent,
        'DDL': DDL,
        'startTime': startTime,
        'classList': classList
    })


@app.route('/api/intoReleaseHomework/', methods=['POST']) # --- 完成 --- #
def intoReleaseHomework():
    userID = request.form.get('userID')

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')
    cursor = conn.cursor()

    cursor.execute('select username from personal_info where userID = %s', (userID,))
    teacherName = cursor.fetchall()
    teacherName = teacherName[0][0]

    cursor.execute('select count(distinct classID) from class_info where teacherName = %s', (teacherName,))
    classNum = cursor.fetchall()
    classNum = classNum[0][0]

    cursor.execute('select classID, courseName, classTime from class_info where teacherName = %s', (teacherName,))
    class_info = cursor.fetchall()

    classList = int(classNum) * [None]

    k = 0
    while k < classNum:
        c = {}
        c.fromkeys(['classID', 'className', 'classTime'])

        c['classID'] = class_info[k][0]
        c['className'] = class_info[k][1]
        c['classTime'] = class_info[k][2]

        classList[k] = c

        k = k + 1

    cursor.close()
    conn.close()

    return jsonify({'classList': classList})



@app.route('/api/ReleaseHomework/', methods=['POST']) #发布作业
def ReleaseHomework():
    userID = request.form.get('userID')
    name = request.form.get('name')
    content = request.form.get('content')
    DDL = request.form.get('DDL')
    startTime = request.form.get('startTime')
    classID = request.form.get('classID')
    docFile = request.files['docFile']
    homeworkID = request.form.get('homeworkID')

    DDL = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime(time.mktime(time.strptime(DDL, "%m/%d/%Y"))))
    startTime = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime(time.mktime(time.strptime(startTime, "%m/%d/%Y"))))

    fileName = homeworkID + '-' + name
    docFile.save(os.path.join('static/homework_post/', fileName + '.rar'))
    url = '../../static/homework_post/' + fileName + '.rar'

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')
    cursor = conn.cursor()

    if homeworkID == "-1":
        cursor.execute('select homeworkID from homework_info order by homeworkID DESC ')
        largestID = cursor.fetchall()
        
        if len(largestID) == 0:
            homeworkID = 1
        else:
            largestID = largestID[0][0]
            homeworkID = largestID + 1
        cursor.execute('insert into homework_info values(%s, %s, %s, %s, %s, %s, %s, %s)', \
                       (homeworkID, classID, name, content, userID, startTime, DDL, url))
    else:
        cursor.execute('update homework_info set classID = %s, name = %s, content = %s, userID = %s, \
                       startTime = %s, DDL = %s, url = %s where homeworkID = %s', \
                       (classID, name, content, userID, startTime, DDL, url, homeworkID))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'result': 'success'})

@app.route('/api/intoGradeHomework/', methods=['POST']) # --- 完成 --- #
def intoGradeHomework():
    userID = request.form.get('userID')
    homeworkID = request.form.get('homeworkID')
    studentID = request.form.get('studentID')


    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')
    cursor = conn.cursor()

    cursor.execute('select homeworkName, homeworkContent from homework_info where homeworkID = %s', (homeworkID))
    h_info = cursor.fetchall()
    homeworkName = h_info[0][0]
    homeworkContent = h_info[0][1]

    cursor.execute('select count(distinct studentID) from homework_belong where homeworkID = %s and eventType = 0', (homeworkID))
    totalOfHomeworkSubmit = cursor.fetchall()
    totalOfHomeworkSubmit = totalOfHomeworkSubmit[0][0]

    cursor.execute('select count(distinct studentID) from homework_belong where homeworkID = %s and eventType = 1', (homeworkID))
    totalOfHomeworkGrade = cursor.fetchall()
    totalOfHomeworkGrade = totalOfHomeworkGrade[0][0]

    totalOfUngradeHomeworkSubmit = totalOfHomeworkSubmit - totalOfHomeworkGrade

    if (studentID == '0'):
        studentID = "have not chosen"
        studentName = "have not chosen"
        srcUrl = "#"
        srcName = "have not chosen"

    else:
        cursor.execute('select studentID, srcFile, homeworkName from homework_belong where homeworkID = %s and studentID = %s',\
                       (homeworkID, studentID))

        randomH = cursor.fetchall()
        if len(randomH) == 0:
            srcUrl = '#'
            srcName = 'not submitted yet'

        else:
            studentID = randomH[0][0]
            srcUrl = randomH[0][1]
            srcName = randomH[0][2]
    
        cursor.execute('select username from personal_info where userID = %s', (studentID))
        studentName = cursor.fetchall()
        studentName = studentName[0][0]

    cursor.execute('select classID from homework_info where homeworkID = %s', (homeworkID))
    classID = cursor.fetchall()
    classID = classID[0][0]


    cursor.execute('select count(distinct userID) from relationship where classID = %s', (classID))
    stuAmt = cursor.fetchall()
    stuAmt = stuAmt[0][0]

    studentList = stuAmt * [None]

    cursor.execute('select userID from relationship where classID = %s', (classID))
    students = cursor.fetchall()

    k = 0
    while k < stuAmt:
        student = students[k][0]

        list = {}
        list.fromkeys(['studentID', 'studentName', 'status'])

        list['studentID'] = student

        cursor.execute('select username from personal_info where userID = %s', (student))
        name = cursor.fetchall()
        name = name[0][0]

        list['studentName'] = name

        cursor.execute('select count(distinct studentID) from homework_belong where homeworkID = %s and studentID = %s\
                       and eventType = 1',(homeworkID, student))
        ifScore = cursor.fetchall()
        ifScore = ifScore[0][0]

        if ifScore > 0:
            list['status'] = 'scored'
        else:
            cursor.execute('select count(distinct studentID) from homework_belong where homeworkID = %s and studentID = %s\
                           and eventType = 0', (homeworkID, student))
            ifSubmit = cursor.fetchall()
            ifSubmit = ifSubmit[0][0]

            if ifSubmit > 0:
                list['status'] = 'submited but not scored'
            else:
                list['status'] = 'not submited'

        studentList[k] = list

        k = k + 1

    cursor.close()
    conn.close()

    return jsonify({
        'homeworkName': homeworkName,
        'homeworkContent': homeworkContent,
        'totalOfHomeworkSubmit': totalOfHomeworkSubmit,
        'totalOfUngradeHomeworkSubmit': totalOfUngradeHomeworkSubmit,
        'studentID': studentID,
        'studentName': studentName,
        'srcUrl': srcUrl,
        'srcName': srcName,
        'studentList': studentList
    })

@app.route('/api/GradeHomework/', methods=['POST']) # --- 完成 --- #
def GradeHomework():
    teacherID = request.form.get('teacherID')
    studentID = request.form.get('studentID')
    homeworkID = request.form.get('homeworkID')
    grade = request.form.get('grade')
    remark = request.form.get('remark')

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')
    cursor = conn.cursor()

    cursor.execute('select classID from homework_info where homeworkID = %s', (homeworkID,))
    classID = cursor.fetchall()
    classID = classID[0][0]

    currentTime = time.time()

    cursor.execute('select score from relationship where userID = %s', (studentID,))
    currenScore = cursor.fetchall()
    currenScore = currenScore[0][0]

    currenScore = currenScore + int(grade)

    cursor.execute('update relationship set score = %s where userID = %s',(currenScore, studentID))

    cursor.execute('insert into homework_belong values(%s, %s, %s, %s, %s, %s, %s, %s, %s)', \
                   (homeworkID, studentID, classID, ' ', ' ', grade, ' ', '1', str(currentTime)))

    currentTime = time.time()

    cursor.execute('insert into homework_belong values(%s, %s, %s, %s, %s, %s, %s, %s, %s)', \
                   (homeworkID, studentID, classID,' ', ' ', '0', remark, '2', str(currentTime)))

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'result': 'success'})

########################################################################################################################



# Class System
# 从你开始做第四个。12.8
# 但事实上这是第五个做的模块12.9

@app.route('/api/ClassManage/', methods=['POST'])
def ClassManage():
    userID = request.form.get('userID')
    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    cursor.execute('select count(*) from class_info where teacherID = %s', (userID,))
    number = cursor.fetchall()
    number = number[0][0]

    cursor.execute('select classID,courseName,teacherName,classTime from class_info where teacherID = %s', (userID,))
    class_info = cursor.fetchall()

    j = 0
    lz = [None] * number

    while j < number:
        d = {}
        d.fromkeys(['classID', 'courseName', 'teacherName', 'classTime'])
        d['classID'] = class_info[j][0]
        d['coureseName'] = class_info[j][1]
        d['teacherName'] = class_info[j][2]
        d['classTime'] = class_info[j][3]
        lz[j] = d
        j = j + 1

    cursor.close()
    conn.close()

    return jsonify({'classList': lz})


# 12.8暂时搁浅，因为这个需要作业系统的支持。待完成。
# 12.9重新开工，暂时无视score部分，将其设为常数0

@app.route('/api/intoClass/', methods=['POST'])
def IntoClass():
    classID = request.form.get('classID')
    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    cursor.execute('select count(*) from relationship where classID = %s', (classID,))
    number = cursor.fetchall()
    number = number[0][0]  # number是该课程的学生数目

    cursor.execute(
        'select userID,username,groupID,score from relationship natural join personal_info where classID = %s',
        (classID,))
    class_info = cursor.fetchall()

    j = 0
    lz = [None] * number

    while j < number:
        d = {}
        d.fromkeys(['studentID', 'name', 'group', 'score'])
        d['studentID'] = class_info[j][0]
        d['name'] = class_info[j][1]
        d['group'] = class_info[j][2]
        d['score'] = class_info[j][3]
        lz[j] = d
        j = j + 1

    cursor.close()
    conn.close()

    return jsonify({'studentList': lz})


@app.route('/api/ChangeGroup/', methods=['POST'])
def ChangeGroup():
    classID = request.form.get('classID')
    studentList = []
    studentList = request.form.getlist('studentList[]')
    group = request.form.get('group')

    number = len(studentList)  # 记载了学生数量

    print('this is studentList')
    print(studentList)
    print(number)

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    k = 0

    while k < number:
        cursor.execute('update relationship set groupID = %s where classID = %s and userID = %s',
                       (group, classID, studentList[k]))
        conn.commit()
        k = k + 1

    cursor.close()
    conn.close()

    return jsonify({'result': 'success'})


@app.route('/api/AddStudent/', methods=['POST'])
def AddStudent():
    studentID = request.form.get('studentID')
    classID = request.form.get('classID')

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    cursor.execute('insert into relationship values(%s,%s,0,0)', (studentID, classID))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'result': 'success'})


# 这里有一个前端bug：后端不能从前端正确获取classID
# 此bug已经被解决


@app.route('/api/DeleteStudent/', methods=['POST'])
def DeleteStudent():
    classID = request.form.get('classID')
    studentList = []
    studentList = request.form.getlist('studentList[]')

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    number = len(studentList)  # 记载了学生数量

    k = 0

    while k < number:
        cursor.execute('delete from relationship where classID = %s and userID = %s', (classID, studentList[k]))
        conn.commit()
        k = k + 1

    cursor.close()
    conn.close()

    return jsonify({'result': 'success'})


@app.route('/api/SendMessage/', methods=['POST'])
def SendMessage():
    userID = request.form.get('userID')
    content = request.form.get('content')
    studentList = []
    studentList = request.form.getlist('studentList[]')
    nowtime = time.strftime('%m/%d/%Y', time.localtime())

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    number = len(studentList)  # 记载了学生数量

    # 这我才发现，发送通知是具体到人啊，不是具体到班
    # 信息系统重构，将原有的两张message表合为一张，并将personal_info中的NewMessage字段删除
    # 世界变得清爽了


    k = 0

    while k < number:
        cursor.execute('select username from personal_info where userID = %s', (userID,))
        sender = cursor.fetchall()
        sender = sender[0][0]

        cursor.execute('insert into message values(NULL,%s,%s,%s,%s,0)', (sender, studentList[k], content, nowtime))
        conn.commit()
        k = k + 1

    cursor.close()
    conn.close()

    return jsonify({'result': 'success'})


@app.route('/api/AddClass/', methods=['POST'])
def AddClass():
    userID = request.form.get('userID')
    courseName = request.form.get('courseName')
    classTime = request.form.get('classTime')

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    cursor.execute('select username from personal_info where userID = %s', (userID,))
    teacherName = cursor.fetchall()
    teacherName = teacherName[0][0]

    cursor.execute('insert into class_info values(NULL,%s,%s,%s,%s)', (courseName, userID, teacherName, classTime))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'result': 'success'})


# 50*50小图标，前端老哥帮忙改改。强迫症害死人。





# BBS System
# 12.15晚开工并结束

@app.route('/api/BBS/', methods=['POST'])
def BBS():
    areaID = request.form.get('areaID')
    userID = request.form.get('userID')

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    cursor.execute('select userType from personal_info where userID = %s', (userID,))
    userType = cursor.fetchall()
    userType = userType[0][0]

    if userType == 'V':
        d = {}
        lz = [None]
        d.fromkeys(['areaID', 'areaName'])
        d['areaID'] = '-1'
        d['areaName'] = '游客留言板'
        lz[0] = d

    if userType != 'V':
        cursor.execute('select areaID,areaname from area')
        area_info = cursor.fetchall()

        number = len(area_info)

        j = 0
        lz = [None] * number

        while j < number:
            d = {}
            d.fromkeys(['areaID', 'areaName'])
            d['areaID'] = area_info[j][0]
            d['areaName'] = area_info[j][1]
            lz[j] = d
            j = j + 1

    # if areaID == '-1':
    # 	cursor.execute('select forumID,title,userName,time,lastTime from forums natural join personal_info')
    # 	forum_info = cursor.fetchall()

    # 	number = len(forum_info)

    # 	j = 0
    # 	la = [None] * number

    # 	while j < number:
    # 		d = {}
    # 		d.fromkeys(['forumsID','forumsName','userName','time','lastTime'])
    # 		d['forumsID'] = forum_info[j][0]
    # 		d['forumsName'] = forum_info[j][1]
    # 		d['userName'] = forum_info[j][2]
    # 		d['time'] = forum_info[j][3]
    # 		d['lastTime'] = forum_info[j][4]
    # 		la[j] = d
    # 		j = j + 1


    # if areaID != '-1':               #旧内容不合时宜，已被注释。12.17

    cursor.execute(
        'select forumID,title,userName,time,lastTime from forums natural join personal_info where areaID = %s',
        (areaID,))
    forum_info = cursor.fetchall()

    number = len(forum_info)

    j = 0
    la = [None] * number

    while j < number:
        d = {}
        d.fromkeys(['forumsID', 'forumsName', 'userName', 'time', 'lastTime'])
        d['forumsID'] = forum_info[j][0]
        d['forumsName'] = forum_info[j][1]
        d['userName'] = forum_info[j][2]
        d['time'] = forum_info[j][3]
        d['lastTime'] = forum_info[j][4]
        la[j] = d
        j = j + 1

    cursor.close()
    conn.close()

    return jsonify({'areaList': lz, 'forumsList': la})


@app.route('/api/CreateForum/', methods=['POST'])
def CreateForum():
    userID = request.form.get('userID')
    title = request.form.get('title')
    content = request.form.get('content')
    areaID = request.form.get('areaID')

    nowtime = time.strftime('%m/%d/%Y', time.localtime())

    file = request.form.get('srcFile')
    srcpath = None
    srcname = None

    if file != "null":
        file = request.files['srcFile']
        file.save(os.path.join('static/share/', userID + title + '.doc'))
        srcpath = '../../static/share/' + userID + title + '.doc'
        srcname = userID + title + '.doc'

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    cursor.execute('insert into forums values(NULL,%s,%s,%s,%s,%s)', (areaID, title, userID, nowtime, nowtime))
    conn.commit()

    cursor.execute('select max(forumID) from forums')
    forumID = cursor.fetchall()
    forumID = forumID[0][0]

    cursor.execute('insert into floor values(%s,1,%s,%s,%s,%s,%s)',
                   (forumID, userID, content, nowtime, srcpath, srcname))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'result': 'success'})


@app.route('/api/Forum/', methods=['POST'])
def Forum():
    forumID = request.form.get('forumID')
    returnID = request.form.get('userID')

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    cursor.execute('select areaID,userID from forums where forumID = %s', (forumID,))
    detail = cursor.fetchall()
    areaID = detail[0][0]
    areaID = int(areaID)
    sourceID = detail[0][1]  # 发帖的人的ID

    if areaID < 10:
        cursor.execute(
            'select userName,content,time,srcpath,srcname from floor natural join personal_info where forumID = %s',
            (forumID,))
        forumList = cursor.fetchall()

        number = len(forumList)

        j = 0
        lz = [None] * number

        while j < number:
            d = {}
            d.fromkeys(['userName', 'content', 'time', 'url', 'fileName'])
            d['userName'] = forumList[j][0]
            d['content'] = forumList[j][1]
            d['time'] = forumList[j][2]
            d['url'] = forumList[j][3]
            d['fileName'] = forumList[j][3]
            lz[j] = d
            j = j + 1

    if areaID == 11:
        courseName = '软件需求工程'
        cursor.execute(
            'select classID,groupID from relationship natural join class_info where userID = %s and courseName = %s',
            (sourceID, courseName))
        sourcerelation = cursor.fetchall()
        sourceclassID = sourcerelation[0][0]
        sourcegroupID = sourcerelation[0][1]

        cursor.execute(
            'select classID,groupID from relationship natural join class_info where userID = %s and courseName = %s',
            (returnID, courseName))
        returnrelation = cursor.fetchall()
        returnclassID = returnrelation[0][0]
        returngroupID = returnrelation[0][1]

        if sourceclassID == returnclassID and sourcegroupID == returngroupID:
            cursor.execute(
                'select userName,content,time,srcpath,srcname from floor natural join personal_info where forumID = %s',
                (forumID,))
            forumList = cursor.fetchall()

            number = len(forumList)

            j = 0
            lz = [None] * number

            while j < number:
                d = {}
                d.fromkeys(['userName', 'content', 'time', 'url', 'fileName'])
                d['userName'] = forumList[j][0]
                d['content'] = forumList[j][1]
                d['time'] = forumList[j][2]
                d['url'] = forumList[j][3]
                d['fileName'] = forumList[j][3]
                lz[j] = d
                j = j + 1
        else:
            d = {}
            lz = [None] * 1
            d.fromkeys(['userName', 'content', 'time', 'url', 'fileName'])
            d['userName'] = "管理员"
            d['content'] = "此内容对您不可见"
            d['time'] = "现在时刻"
            d['url'] = 'NULL'
            d['fileName'] = 'NULL'
            lz[0] = d

    if areaID == 22:
        courseName = '软件工程管理'
        cursor.execute(
            'select classID,groupID from relationship natural join class_info where userID = %s and courseName = %s',
            (sourceID, courseName))
        sourcerelation = cursor.fetchall()
        sourceclassID = sourcerelation[0][0]
        sourcegroupID = sourcerelation[0][1]

        cursor.execute(
            'select classID,groupID from relationship natural join class_info where userID = %s and courseName = %s',
            (returnID, courseName))
        returnrelation = cursor.fetchall()
        returnclassID = returnrelation[0][0]
        returngroupID = returnrelation[0][1]

        if sourceclassID == returnclassID and sourcegroupID == returngroupID:
            cursor.execute(
                'select userName,content,time,srcpath,srcname from floor natural join personal_info where forumID = %s',
                (forumID,))
            forumList = cursor.fetchall()

            number = len(forumList)

            j = 0
            lz = [None] * number

            while j < number:
                d = {}
                d.fromkeys(['userName', 'content', 'time', 'url', 'fileName'])
                d['userName'] = forumList[j][0]
                d['content'] = forumList[j][1]
                d['time'] = forumList[j][2]
                d['url'] = forumList[j][3]
                d['fileName'] = forumList[j][3]
                lz[j] = d
                j = j + 1
        else:
            d = {}
            lz = [None] * 1
            d.fromkeys(['userName', 'content', 'time', 'url', 'fileName'])
            d['userName'] = "管理员"
            d['content'] = "此内容对您不可见"
            d['time'] = "现在时刻"
            d['url'] = 'NULL'
            d['fileName'] = 'NULL'
            lz[0] = d
    cursor.close()
    conn.close()

    return jsonify({'forumList': lz})


@app.route('/api/SubmitForum/', methods=['POST'])  # 这个是回复，不是提交
def SubmitForum():
    userID = request.form.get('userID')
    content = request.form.get('content')
    forumID = request.form.get('forumID')

    nowtime = time.strftime('%m/%d/%Y', time.localtime())

    file = request.form.get('srcFile')
    srcpath = None
    srcname = None

    conn = pymysql.connect(user='root', password='password', database='tas', charset='UTF8')  # 这是后端加的
    cursor = conn.cursor()

    cursor.execute('select * from floor where forumID = %s', (forumID,))
    forumList = cursor.fetchall()
    number = len(forumList)
    num = str(number)

    if file != "null":
        file = request.files['srcFile']
        file.save(os.path.join('static/share/', userID + num + '.doc'))
        srcpath = '../../static/share/' + userID + num + '.doc'
        srcname = userID + num + '.doc'

    number = number + 1

    cursor.execute('update forums set lastTime = %s where forumID = %s', (nowtime, forumID))
    conn.commit()

    cursor.execute('insert into floor values(%s,%s,%s,%s,%s,%s,%s)',
                   (forumID, number, userID, content, nowtime, srcpath, srcname))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'result': 'success'})


# 2016.12.17夜更新：
# 现在游客只能进入游客留言板了
# 现在只有同组人员能进入自己组内的帖子了，其他人可以进入，但是看不到帖子内容。
# 基本上OK了！

# 2017.01.01夜更新：
# 各项功能完备，但是老师不能进入讨论区，有bug。
# 上传功能完备。
# 50*50小图标，前端老哥帮忙改改。

if __name__ == '__main__':
    app.run(debug=True)

