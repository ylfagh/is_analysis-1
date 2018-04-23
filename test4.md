<!-- markdownlint-disable MD033-->
<!-- 禁止MD033类型的警告 https://www.npmjs.com/package/markdownlint -->

## 实验4 图书管理系统顺序图绘制 | [返回](./README.md)

- 本实例的目的是掌握顺序图的作用，对象交互模式，消息在对象交互中的作用，以及顺序图与活动图（通常叫流程图）的区别。
- 仔细阅读并理解第10章系统总体设计的10.4.3节：设计类的方法。
- 根据[实验2：图书管理系统用例建模](./test2.md)以及[实验3：图书管理系统领域对象建模](./test3.md)，绘制出<b>图书管理系统</b>主要用例的顺序图。
- 用PlantUML标准工具画出图书管理系统的顺序图（如教材Page215的图10.41，图10.42，Page218的图10.46和图10.47）。
- 整个文档要汇总到REMADE.md文本文件中进行说明，说明文件用Markdown格式编写。

<b>注意事项</b>
- 类划分的颗粒度要适中，不能太大，也不能太小。
- 可以将相同作用的类放在类图的包（package）中
- 类图要尽量体现类与类之间的关系：依赖关系(Dependency)，关联关系(Association)，聚合关系(Aggregation)，组合关系(Composition)，继承关系(Inheritance)。参见：
    * https://blog.csdn.net/a19881029/article/details/8957441
    * http://www.uml.org.cn/oobject/201211231.asp
- 类图要尽量体现出关系的多重性：如。
    * 1:        表示1个
    * 0..*：    表示任意多个（ ≥0）（*可以换成n）
    * *：       表示任意多个（ ≥0）
    * 1..*：    表示1个或多个（≥1）
    * 0..1：    表示0个或1个
    * 5..11：   表示5-11个
    * 1,3,8： 表示个1或3个或8个
    * 0,3..8： 表示0个或3-8个

<b>实验提交</b>

- 实验提交到自己的gitHub的is_analysis/test3目录中，主要文件名是：README.md，再附上一些图片文件。
- 你的gitHub中的is_analysis/test3目录中可能有以下文件：

``` filelist
README.md
class1.png
class2.png
object1.png
object2.png
...
```

- 本次实验需要写到纸质实验报告中。

- 你的实验内容提交成功后，可以直接访问https://github.com/<b>zhang</b>/is_analysis/tree/master/test4
查看你编写的实验文档。其中zhang是你的gitHub用户名。

- 请在2018-05-01之前提交，过时扣分。

<b>参考</b>

- 顺序图（也叫时序图）的绘制方法参考[PlantUML标准](http://plantuml.com/sequence-diagram)文件的sequence-diagram标准
- Markdown格式参考：https://www.jianshu.com/p/b03a8d7b1719
- 老师的教学资源：https://github.com/zwdbox/is_analysis
- 老师以同学身份做的<b>伪实验4</b>参考：https://github.com/zwdbox/is_analysis/tree/master/test4