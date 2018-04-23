# 实验3：图书管理系统时序图绘制（老师示范）
|学号|班级|姓名|照片|
|:-------:|:-------------: | :----------:|:---:|
|12345678|软件(本)15-4|赵卫东|![flow1](../myself.jpg)|

## 图书管理系统的时序图

## 1. 借书用例
## 1.1. PlantUML源码

``` sequence
@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response

Alice -> Bob: Another authentication Request
Alice <-- Bob: another authentication Response
@enduml
```

## 1.2. 时序图
![class](sequence1.png)

## 1.3. 时序图说明
***

## 2. 还书用例
## 2.1. PlantUML源码

``` sequence
@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response

Alice -> Bob: Another authentication Request
Alice <-- Bob: another authentication Response
@enduml
```

## 2.2. 时序图
![class](sequence2.png)

## 2.3. 时序图说明
***