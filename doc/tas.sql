-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 2017-01-02 16:50:48
-- 服务器版本： 5.7.11-log
-- PHP Version: 5.6.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

create database if not exists `tas`;
USE `tas`;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tas`
--

-- --------------------------------------------------------

--
-- 表的结构 `area`
--

CREATE TABLE `area` (
  `areaID` int(11) NOT NULL,
  `areaname` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `area`
--

INSERT INTO `area` (`areaID`, `areaname`) VALUES
(-1, '游客留言板'),
(1, '软件需求工程课程讨论区'),
(2, '软件工程管理课程讨论区'),
(11, '软件需求工程小组讨论区'),
(22, '软件工程管理小组讨论区');

-- --------------------------------------------------------

--
-- 表的结构 `class_info`
--

CREATE TABLE `class_info` (
  `classID` int(11) NOT NULL,
  `courseName` varchar(20) NOT NULL,
  `teacherID` varchar(10) NOT NULL,
  `teacherName` varchar(20) NOT NULL,
  `classTime` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `class_info`
--

INSERT INTO `class_info` (`classID`, `courseName`, `teacherID`, `teacherName`, `classTime`) VALUES
(1, '软件需求工程', '1111', '刘玉生', '周五 345'),
(2, '软件需求工程', '2222', '林海', '周一 678'),
(3, '软件工程管理', '3333', '金波', '周二 345');

-- --------------------------------------------------------

--
-- 表的结构 `floor`
--

CREATE TABLE `floor` (
  `forumID` int(11) NOT NULL,
  `floornum` int(11) NOT NULL,
  `userID` varchar(20) NOT NULL,
  `content` varchar(1000) NOT NULL,
  `time` varchar(40) NOT NULL,
  `srcpath` varchar(100) DEFAULT NULL,
  `srcname` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `floor`
--

INSERT INTO `floor` (`forumID`, `floornum`, `userID`, `content`, `time`, `srcpath`, `srcname`) VALUES
(3, 1, '3140100001', '第一组的同学快来集合！', '01/02/2017', '../../static/share/31401000011班第1组专用讨论帖.doc', '31401000011班第1组专用讨论帖.doc'),
(3, 2, '3140100002', '我来报到啦！', '01/02/2017', NULL, NULL),
(3, 3, '3140100003', '都比前来报到', '01/02/2017', NULL, NULL),
(3, 4, '3140100004', '我来报到啦，顺便给大家带一个文档作参考！', '01/02/2017', '../../static/share/31401000043.doc', '31401000043.doc'),
(4, 1, '3140100002', '咱们这课程网站做的还行吧', '01/02/2017', NULL, NULL),
(5, 1, '3140100002', '第二组的同学，出来聊聊天吧！', '01/02/2017', NULL, NULL),
(5, 2, '3140100003', '作为同组人，挤挤', '01/02/2017', NULL, NULL),
(5, 3, '3140100005', '我是第二组的，真的都可以看见诶！', '01/02/2017', NULL, NULL),
(6, 1, '3140100003', '其实没啥可水的', '01/02/2017', NULL, NULL),
(7, 1, '3140100005', '都来吧都来吧！', '01/02/2017', NULL, NULL),
(8, 1, '201701', '呜呜呜', '01/02/2017', NULL, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `forums`
--

CREATE TABLE `forums` (
  `forumID` int(11) NOT NULL,
  `areaID` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `userID` varchar(10) NOT NULL,
  `time` varchar(40) NOT NULL,
  `lastTime` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `forums`
--

INSERT INTO `forums` (`forumID`, `areaID`, `title`, `userID`, `time`, `lastTime`) VALUES
(3, 11, '1班第1组专用讨论帖', '3140100001', '01/02/2017', '01/02/2017'),
(4, -1, '报到的时候顺便水一贴', '3140100002', '01/02/2017', '01/02/2017'),
(5, 1, '听说在这里发帖子大家都可以看见', '3140100002', '01/02/2017', '01/02/2017'),
(6, -1, '2号都水了，我也要水', '3140100003', '01/02/2017', '01/02/2017'),
(7, 11, '1班第2组专用讨论帖', '3140100005', '01/02/2017', '01/02/2017'),
(8, -1, '我只能看见游客区，不开心', '201701', '01/02/2017', '01/02/2017');

-- --------------------------------------------------------

--
-- 表的结构 `homework_belong`
--

CREATE TABLE `homework_belong` (
  `homeworkID` int(11) NOT NULL,
  `studentID` varchar(10) NOT NULL,
  `classID` int(11) NOT NULL,
  `homeworkName` varchar(50) NOT NULL,
  `srcFile` varchar(100) NOT NULL,
  `grade` int(11) NOT NULL,
  `remark` varchar(200) NOT NULL,
  `eventType` int(11) NOT NULL,
  `eventTime` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `homework_info`
--

CREATE TABLE `homework_info` (
  `homeworkID` int(11) NOT NULL,
  `classID` int(11) NOT NULL,
  `homeworkName` varchar(50) NOT NULL,
  `homeworkContent` varchar(1000) NOT NULL,
  `teacherID` varchar(10) NOT NULL,
  `startTime` varchar(40) NOT NULL,
  `DDL` varchar(40) NOT NULL,
  `url` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `intro_course`
--

CREATE TABLE `intro_course` (
  `name` varchar(20) NOT NULL,
  `srcOfPic` varchar(100) NOT NULL,
  `content` varchar(10000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `intro_course`
--

INSERT INTO `intro_course` (`name`, `srcOfPic`, `content`) VALUES
('软件工程管理', '../../static/src/软件工程管理.jpg', '软件工程管理的对象是软件工程项目。它所涉及的范围覆盖了整个软件工程过程。为使软件项目开发获得成功，关键问题是必须对软件项目的工作范围、可能风险、需要资源（人、硬件/软件）、要实现的任务、经历的里程碑、花费工作量（成本）、进度安排等做到心中有数。这种管理在技术工作开始之前就应开始，在软件从概念到实现的过程中继续进行，当软件工程过程最后结束时才终止。<br><br>软件项目管理是为了使软件项目能够按照预定的成本、进度、质量顺利完成，而对人员（People）、产品（Product）、过程（Process）和项目(Project)进行分析和管理的活动。<br><br>软件项目管理的根本目的是为了让软件项目尤其是大型项目的整个软件生命周期（从分析、设计、编码到测试、维护全过程）都能在管理者的控制之下，以预定成本按期，按质的完成软件交付用户使用。而研究软件项目管理为了从已有的成功或失败的案例中总结出能够指导今后开发的通用原则，方法，同时避免前人的失误。'),
('软件需求工程', '../../static/src/软件需求工程.jpg', '软件需求是指用户对目标软件系统在功能、行为、性能、设计约束等方面的期望。通过对应问题及其环境的理解与分析，为问题涉及的信息、功能及系统行为建立模型，将用户需求精确化、完全化，最终形成需求规格说明，这一系列的活动即构成软件开发生命周期的需求分析阶段。需求分析是介于系统分析和软件设计阶段之间的桥梁。一方面，需求分析以系统规格说明和项目规划作为分析活动的基本出发点，并从软件角度对它们进行检查与调整；另一方面，需求规格说明又是软件设计、实现、测试直至维护的主要基础。良好的分析活动有助于避免或尽早剔除早期错误，从而提高软件生产率，降低开发成本，改进软件质量。');

-- --------------------------------------------------------

--
-- 表的结构 `intro_teacher`
--

CREATE TABLE `intro_teacher` (
  `name` varchar(20) NOT NULL,
  `srcOfPic` varchar(100) NOT NULL,
  `content` varchar(10000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `intro_teacher`
--

INSERT INTO `intro_teacher` (`name`, `srcOfPic`, `content`) VALUES
('刘玉生', '../../static/src/刘玉生老师.jpg', '刘玉生老师，计算机科学与技术学院，CAD&CG国家重点实验室，教授。'),
('林海', '../../static/src/林海老师.jpg', '林海老师，计算机科学与技术学院，CAD&CG国家重点实验室，教授。'),
('邢卫', '../../static/src/邢卫老师.jpg', '邢卫老师，浙江大学计算机学院副教授。1992年3月毕业于浙江大学计算机系，获硕士学位。2000年12月晋升副教授。作为课题负责人、技术负责人或主要骨干承担或参与国家自然科学基金项目、国家863计划项目、国家科技支撑计划项目、浙江省重大科技攻关项目等多项。目前的主要研究领域包括计算机网络、多媒体编码、流传输技术等。'),
('金波', '../../static/src/金波老师.jpg', '金波老师主要从事软件开发技术、软件工程、计算机网络工程、建筑物智能化技术和应用、项目管理、过程改进、质量控制、项目实施规划、项目战略规划编制等的研究，曾长期从事嵌入式系统的研发。对软件产品项目管理、成本控制、质量认证、过程监理、价值评估等有长期深入的研究和丰富的实践经验，曾获得国家部级科技进步一等奖。<br><br>最近，主持研制(数据流、视频流和音频流)“三流合一”的电信级多媒体通信平台获得成功。\n');

-- --------------------------------------------------------

--
-- 表的结构 `message`
--

CREATE TABLE `message` (
  `messageID` int(11) NOT NULL,
  `sender` varchar(10) NOT NULL,
  `receiver` varchar(10) NOT NULL,
  `content` varchar(1000) NOT NULL,
  `time` varchar(40) NOT NULL,
  `readornot` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `message`
--

INSERT INTO `message` (`messageID`, `sender`, `receiver`, `content`, `time`, `readornot`) VALUES
(6, '刘玉生', '3140100001', '明天来我办公室一趟', '01/01/2017', 0),
(7, '刘玉生', '3140100002', '明天来我办公室一趟', '01/01/2017', 0),
(8, '刘玉生', '3140100003', '明天来我办公室一趟', '01/01/2017', 0),
(9, '刘玉生', '3140100004', '明天来我办公室一趟', '01/01/2017', 0),
(10, '刘玉生', '3140100005', '明天来我办公室一趟', '01/01/2017', 0),
(11, '刘玉生', '3140100006', '明天来我办公室一趟', '01/01/2017', 0),
(12, '刘玉生', '3140100007', '明天来我办公室一趟', '01/01/2017', 0),
(13, '刘玉生', '3140100008', '明天来我办公室一趟', '01/01/2017', 0),
(14, '刘玉生', '3140100001', '刚才发错了，不好意思', '01/01/2017', 0),
(15, '刘玉生', '3140100002', '刚才发错了，不好意思', '01/01/2017', 0),
(16, '刘玉生', '3140100003', '刚才发错了，不好意思', '01/01/2017', 0),
(17, '刘玉生', '3140100004', '刚才发错了，不好意思', '01/01/2017', 0),
(18, '刘玉生', '3140100005', '刚才发错了，不好意思', '01/01/2017', 0),
(19, '刘玉生', '3140100006', '刚才发错了，不好意思', '01/01/2017', 0),
(20, '刘玉生', '3140100007', '刚才发错了，不好意思', '01/01/2017', 0),
(21, '刘玉生', '3140100008', '刚才发错了，不好意思', '01/01/2017', 0),
(22, '刘玉生', '3140100001', '其实是你们的作业没交，赶快交', '01/01/2017', 0),
(23, '刘玉生', '3140100002', '其实是你们的作业没交，赶快交', '01/01/2017', 0),
(24, '刘玉生', '3140100003', '其实是你们的作业没交，赶快交', '01/01/2017', 0),
(25, '刘玉生', '3140100004', '其实是你们的作业没交，赶快交', '01/01/2017', 0),
(26, '刘玉生', '3140100005', '其实是你们的作业没交，赶快交', '01/01/2017', 0),
(27, '刘玉生', '3140100006', '其实是你们的作业没交，赶快交', '01/01/2017', 0),
(28, '刘玉生', '3140100007', '其实是你们的作业没交，赶快交', '01/01/2017', 0),
(29, '刘玉生', '3140100008', '其实是你们的作业没交，赶快交', '01/01/2017', 0),
(30, '刘玉生', '3140100001', '半夜了，大家快睡觉吧', '01/02/2017', 0),
(31, '刘玉生', '3140100002', '半夜了，大家快睡觉吧', '01/02/2017', 0),
(32, '刘玉生', '3140100003', '半夜了，大家快睡觉吧', '01/02/2017', 0),
(33, '刘玉生', '3140100004', '半夜了，大家快睡觉吧', '01/02/2017', 0),
(34, '刘玉生', '3140100005', '半夜了，大家快睡觉吧', '01/02/2017', 0),
(35, '刘玉生', '3140100006', '半夜了，大家快睡觉吧', '01/02/2017', 0),
(36, '刘玉生', '3140100007', '半夜了，大家快睡觉吧', '01/02/2017', 0),
(37, '刘玉生', '3140100008', '半夜了，大家快睡觉吧', '01/02/2017', 0),
(38, '刘玉生', '3140100001', '半夜了，大家快睡觉吧', '01/02/2017', 0),
(39, '刘玉生', '3140100002', '半夜了，大家快睡觉吧', '01/02/2017', 0),
(40, '刘玉生', '3140100003', '半夜了，大家快睡觉吧', '01/02/2017', 0),
(41, '刘玉生', '3140100004', '半夜了，大家快睡觉吧', '01/02/2017', 0),
(42, '刘玉生', '3140100005', '半夜了，大家快睡觉吧', '01/02/2017', 0),
(43, '刘玉生', '3140100006', '半夜了，大家快睡觉吧', '01/02/2017', 0),
(44, '刘玉生', '3140100007', '半夜了，大家快睡觉吧', '01/02/2017', 0),
(45, '刘玉生', '3140100008', '半夜了，大家快睡觉吧', '01/02/2017', 0);

-- --------------------------------------------------------

--
-- 表的结构 `personal_info`
--

CREATE TABLE `personal_info` (
  `userID` varchar(10) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `userType` char(1) NOT NULL,
  `question` varchar(50) NOT NULL,
  `answer` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `personal_info`
--

INSERT INTO `personal_info` (`userID`, `username`, `password`, `userType`, `question`, `answer`) VALUES
('0000', '管理员', '0000', 'A', '你是来干什么的？', '打酱油'),
('1111', '刘玉生', '1111', 'T', '你是教什么课的？', '软件需求工程'),
('201701', '游客1号', '201701', 'V', '你是来干什么的？', '观光'),
('201702', '游客2号', '201702', 'V', '你是来干什么的？', '观光'),
('2222', '林海', '2222', 'T', '你是教什么课的？', '软件需求工程'),
('3140100001', '学生1号', '0001', 'S', '你是来干什么的？', '打酱油'),
('3140100002', '学生2号', '0002', 'S', '你是来干什么的？', '打酱油'),
('3140100003', '学生3号', '0003', 'S', '你是来干什么的？', '打酱油'),
('3140100004', '学生4号', '0004', 'S', '你是来干什么的？', '打酱油'),
('3140100005', '学生5号', '0005', 'S', '你是来干什么的？', '打酱油'),
('3140100006', '学生6号', '0006', 'S', '你是来干什么的？', '打酱油'),
('3140100007', '学生7号', '0007', 'S', '你是来干什么的？', '打酱油'),
('3140100008', '学生8号', '0008', 'S', '你是来干什么的？', '打酱油'),
('3140100009', '学生9号', '0009', 'S', '你是来干什么的？', '打酱油'),
('3140100010', '学生10号', '0010', 'S', '你是来干什么的？', '打酱油'),
('3140100011', '学生11号', '0011', 'S', '你是来干什么的？', '打酱油'),
('3140100012', '学生12号', '0012', 'S', '你是来干什么的？', '打酱油'),
('3140100013', '学生13号', '0013', 'S', '你是来干什么的？', '打酱油'),
('3140100014', '学生14号', '0014', 'S', '你是来干什么的？', '打酱油'),
('3140100015', '学生15号', '0015', 'S', '你是来干什么的？', '打酱油'),
('3333', '邢卫', '3333', 'T', '你是教什么课的？', '软件需求工程'),
('4444', '金波', '4444', 'T', '你是教什么课的？', '软件工程管理');

-- --------------------------------------------------------

--
-- 表的结构 `relationship`
--

CREATE TABLE `relationship` (
  `userID` varchar(10) NOT NULL,
  `classID` int(11) NOT NULL,
  `groupID` int(11) NOT NULL,
  `score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `relationship`
--

INSERT INTO `relationship` (`userID`, `classID`, `groupID`, `score`) VALUES
('3140100001', 1, 1, 0),
('3140100002', 1, 1, 0),
('3140100003', 1, 1, 0),
('3140100004', 1, 1, 0),
('3140100005', 1, 2, 0),
('3140100006', 1, 2, 0),
('3140100007', 1, 2, 0),
('3140100008', 1, 2, 0),
('3140100009', 2, 1, 0),
('3140100010', 2, 1, 0),
('3140100011', 2, 1, 0),
('3140100012', 2, 1, 0);

-- --------------------------------------------------------

--
-- 表的结构 `resource`
--

CREATE TABLE `resource` (
  `srcID` int(11) NOT NULL,
  `classID` int(11) NOT NULL,
  `srcUrl` varchar(100) NOT NULL,
  `srcName` varchar(30) NOT NULL,
  `urlOfPic` varchar(100) NOT NULL,
  `type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `resource`
--

INSERT INTO `resource` (`srcID`, `classID`, `srcUrl`, `srcName`, `urlOfPic`, `type`) VALUES
(1, 1, '../../static/material/uml绘制.ppt', 'uml绘制', '../../static/src/SE.jpg', 'Courseware'),
(2, 1, '../../static/material/工具使用.ppt', '工具使用', '../../static/src/SE.jpg', 'Courseware'),
(3, 1, '../../static/material/c01.pdf', 'c01', '../../static/src/SE.jpg', 'RefeMaterial'),
(4, 1, '../../static/material/c05.pdf', 'c05', '../../static/src/SE.jpg', 'RefeMaterial'),
(5, 1, '../../static/material/c06.pdf', 'c06', '../../static/src/SE.jpg', 'RefeMaterial'),
(6, 1, '../../static/material/c07.pdf', 'c07', '../../static/src/SE.jpg', 'RefeMaterial'),
(7, 2, '../../static/material/课程记录1.mp3', '课程记录1', '../../static/src/SE.jpg', 'MultiMedia'),
(8, 2, '../../static/material/课程记录2.mp3', '课程记录2', '../../static/src/SE.jpg', 'MultiMedia'),
(9, 2, '../../static/material/软件需求工程.jpg', '软件需求工程', '../../static/src/SE.jpg', 'OtherMaterial'),
(10, 1, '../../static/material/新课件.pdf', '新课件', '../../static/src/SE.jpg', 'RefeMaterial');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`areaID`);

--
-- Indexes for table `class_info`
--
ALTER TABLE `class_info`
  ADD PRIMARY KEY (`classID`);

--
-- Indexes for table `floor`
--
ALTER TABLE `floor`
  ADD PRIMARY KEY (`forumID`,`floornum`);

--
-- Indexes for table `forums`
--
ALTER TABLE `forums`
  ADD PRIMARY KEY (`forumID`);

--
-- Indexes for table `homework_belong`
--
ALTER TABLE `homework_belong`
  ADD PRIMARY KEY (`studentID`,`homeworkID`,`eventTime`);

--
-- Indexes for table `homework_info`
--
ALTER TABLE `homework_info`
  ADD PRIMARY KEY (`homeworkID`);

--
-- Indexes for table `intro_course`
--
ALTER TABLE `intro_course`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `intro_teacher`
--
ALTER TABLE `intro_teacher`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`messageID`);

--
-- Indexes for table `personal_info`
--
ALTER TABLE `personal_info`
  ADD PRIMARY KEY (`userID`);

--
-- Indexes for table `relationship`
--
ALTER TABLE `relationship`
  ADD PRIMARY KEY (`classID`,`userID`,`groupID`);

--
-- Indexes for table `resource`
--
ALTER TABLE `resource`
  ADD PRIMARY KEY (`srcID`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `class_info`
--
ALTER TABLE `class_info`
  MODIFY `classID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- 使用表AUTO_INCREMENT `forums`
--
ALTER TABLE `forums`
  MODIFY `forumID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- 使用表AUTO_INCREMENT `message`
--
ALTER TABLE `message`
  MODIFY `messageID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;
--
-- 使用表AUTO_INCREMENT `resource`
--
ALTER TABLE `resource`
  MODIFY `srcID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
