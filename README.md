# sduoj_get_1st

#### 介绍
SDUOJ平台的contest“抢一血”（即第一个提交或第一个AC）自动程序，仅适合SDUCST课程【数据结构与算法】使用的SDUOJ以班级为单位的contest评测。本程序仅适用Google浏览器。

#### 平台介绍
SDUOJ（ https://oj.qd.sdu.edu.cn ）是只对校内人员开放的代码在线评测平台（这意味着外部网络无法访问），多门课程如【数据结构与算法】使用该平台进行代码评测。

#### 安装教程

1. 程序使用了requests，lxml，time，selenium，warnings库，在运行本程序前，应先确保python环境中存在相应的库。你可以使用如下命令来安装，以requests为例：

```bash
pip install requests
```

2. web自动化工具selenium用到的浏览器驱动为chromedriver，镜像地址：https://npm.taobao.org/mirrors/chromedriver 。为了方便起见，应确保chromedriver.exe程序与get_1st.py处于同一目录下。注意：**chromedriver版本应与Google浏览器相匹配！**

#### 使用说明

将该程序需要的各文件、辅助程序放到同一目录下，即可运行该程序。需要输入SDUOJ的用户名和密码以及目标页面的url。一次提交后，将输出服务器返回的信息，提交成功则返回的信息类似如下：

```json
{"code":0,"message":"成功","timestamp":"1636611425369","data":"36c3d4415004bda"}
```

#### 问题反馈

如有问题、疑惑，请联系邮箱：1916387818@qq.com 。

#### 附

项目地址：https://github.com/crjg-k/sduoj_get_1st 。

