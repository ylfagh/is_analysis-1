<!-- markdownlint-disable MD033-->
<!-- 禁止MD033类型的警告 https://www.npmjs.com/package/markdownlint -->

# 《信息系统分析与设计》（第4版）

![book](book.jpg)

清华大学出版社 王晓敏 邝孔武 编著

主讲：成都大学信息科学与工程学院 赵卫东

## 老师编写的课程教学平台
- 查看与修改你的GitHUB用户名：http://202.115.82.8:1522
- 源码参见: https://github.com/zwdbox/is_analysis/tree/master/项目/学生操作
-  注意，查询个人成绩界面中不要出现下图中的“错误地址”，否则会没有成绩。
  ![](p3.jpg)
  
## 搭建文档编写环境：
- 编辑器: IntelliJ IDEA
- IDEA插件: markdown 和 plantuml
- 单独安装: git 和 graphviz

## 实验

- ### [实验1：业务流程建模](./test1.md)
    - 实验1批改情况说明（大家都容易出现的问题有）：
        1. 没有按角色分组
        2. 没有文字说明
    - 部分比较优秀(95分以上)的实验1如下：    
        - [郭钊彬	软件(本)15-1](https://github.com/HaveyouBinbin/is_analysis/tree/master/test1)
        - [姚启迪	软件(本)15-1](https://github.com/Konoha-Y/is_analysis/tree/master/test1)
        - [曾玉龙	软件(本)15-2](https://github.com/Zengyulong/is_analysis/tree/master/test1)
        - [陈惠翔	软件(本)15-4](https://github.com/JasonChenhx/is_analysis/tree/master/test1)
        - [梅恩	软件(本)15-4](https://github.com/228957643/is_analysis/tree/master/test1)
        - [吴靖	软件(本)15-4](https://github.com/ikowalski/is_analysis/tree/master/test1)
        - [张启恒	软件(本)15-4](https://github.com/zhangqiheng/is_analysis/tree/master/test1)
- ### [实验2：图书管理系统用例建模](./test2.md)
    - 实验2批改情况说明（大家都容易出现的问题有）：
        1. << include >>和<< extend >>写成了include和extend，没有<<>>符号    
        2. 滥用<< extend >>。extend只是用于特殊情况，异常情况，不能用于正常情况的用例。
    比如“书目维护”用例中的“增加”，“修改”，“删除”用例，
    不应该是<< extend >>关系，应该是<< include >>关系或者是<< use >>关系。
    - 部分比较优秀(95分以上)的实验2如下：
        - [杨钉权	软件(本)15-1](https://github.com/sinmem/is_analysis/tree/master/test2)
        - [周志强	软件(本)15-1](https://github.com/aGreySky/is_analysis/tree/master/test2)
        - [杨楠	软件(本)15-2](https://github.com/abecd/is_analysis/tree/master/test2)
        - [杜芸彦	软件(本)15-3](https://github.com/d123456yy/is_analysis/tree/master/test2)
        - [邱小霞	软件(本)15-3](https://github.com/q1314520xx/is_analysis/tree/master/test2)
        - [孙守利	软件(本)15-3](https://github.com/shoulisun/is_analysis/tree/master/test2)
        - [余行	软件(本)15-3](https://github.com/yuhang456/is_analysis/tree/master/test2)
        - [张文	软件(本)15-3](https://github.com/Anntly/is_analysis/tree/master/test2)
        - [陈惠翔	软件(本)15-4](https://github.com/JasonChenhx/is_analysis/tree/master/test2)
        - [蒋春林	软件(本)15-4](https://github.com/FateBerserker/is_analysis/tree/master/test2)
        - [梅恩	软件(本)15-4](https://github.com/228957643/is_analysis/tree/master/test2)
        - [吴靖	软件(本)15-4](https://github.com/ikowalski/is_analysis/tree/master/test2)
        - [张启恒	软件(本)15-4](https://github.com/zhangqiheng/is_analysis/tree/master/test2)
- ### [实验3：图书管理系统领域对象建模](./test3.md)
- 实验3批改情况说明（大家都容易出现的问题有）：

        1. 应该是类图在前，对象图在后。整个系统最好只有一个类图，减小类的重复编写。
        
        2. 类图中不需要对象图中的实例,比如不需要具体的姓名，具体的图书名称。
        
        3. 类图中的关联线条错误太多，关联线条的三要素：类别，方向和数字对应关系都应该设计正确。
        
        4. 对象类中的数据要符合实事。比如，字符串要加单引号，数字不加引号，密码不要用明文。
          
        5. 应该说明每个类由哪个用例产生，被哪些实例引用。
              
## 抄袭说明
- 有抄袭嫌疑的实验，老师批改的成绩都比较低。原作者有可能是抄袭的受害者，如果出现这种情况，请告知老师修改成绩。
- 自己独立完成的实验，分数不会低。

## 参考资料
- 绘制方法参考[PlantUML标准](http://plantuml.com)
- Markdown格式参考：https://www.jianshu.com/p/b03a8d7b1719
- 老师的教学资源：https://github.com/zwdbox/is_analysis