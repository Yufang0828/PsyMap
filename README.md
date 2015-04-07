心理地图
========

开发环境部署需知
----------------

1.  请使用Python
    2.7.x作为python运行环境，建议安装anaconda发行版（目前为2.2.0版本）：
    `https://store.continuum.io/cshop/anaconda/ ；`

2.  使用pip安装程序需要的Python库，执行如下命令（在当前目录下）：

    -   `pip install -r requirements.txt`

3.  程序后台使用的数据库为PostgreSQL
    9.4（且不兼容MySQL），请按下列步骤安装各组件：

    1.  请先安装PostgreSQL；

    2.  安装PostGIS（用于地理位置信息处理），方法参照
        `https://docs.djangoproject.com/en/1.8/ref/contrib/gis/install/#postgis`
        ；

    3.  安装PostgreSQL之后，还需要安装psycopg2，以完成django对PostgreSQL的兼容，请前往
        `http://www.stickpeople.com/projects/python/win-psycopg/`
        选择对应版本操作系统和Python版本的程序完成exe安装程序的下载安装；

    4.  在PostgreSQL当中执行如下SQL： `CREATE EXTENSION IF NOT EXISTS hstore`
        （该步骤必须）；

4.  程序中部分旧代码仍然使用一些MySQL组件，请前往
    `http://www.codegood.com/archives/129`
    下载安装MySQLdb（对MySQL的依赖会在后续版本移除）；

5.  建议的开发环境： `PyCharm 4.0.x` ；

6.  将代码clone至本地后，本地路径名中不得还有中文字符，否则django程序无法启动；

7.  调试程序时，请将base\_generic.html代码文件当中的 `<base
    href="http://ccpl.psych.ac.cn/PsyMap/"/>`  行进行修改，将href修改为
    “http://127.0.0.1:端口号/PsyMap/” ，以便在本地进行调试；

8.  初次运行程序时候，需要使用django的migrate命令建立数据库：

    -   首先在命令行当中执行：`python manage.py makemigrations`

    -   然后执行`python manage.py migrate`

    -   创建超级管理员用户：`python manage.py createsuperuser`

9.  对原有数据库进行迁移：

    1.  修改数据库中的auth\_user表，将Password、FirstName、LastName、EMail等字段的非空约束删除；

    2.  执行util目录下的db\_migrate.py来执行数据的迁移工作。
