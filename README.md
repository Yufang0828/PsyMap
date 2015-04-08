心理地图
========

开发环境部署需知
----------------

1.  请使用Python
    2.7.x作为python运行环境，建议安装anaconda发行版（目前为2.2.0版本）：
    `https://store.continuum.io/cshop/anaconda/ ；`

2.  程序后台使用的数据库为PostgreSQL
    9.4（且不兼容MySQL），请按下列步骤安装各组件：

    1.  请先安装PostgreSQL；

    2.  安装PostGIS（用于地理位置信息处理），方法参照
        `https://docs.djangoproject.com/en/1.8/ref/contrib/gis/install/#postgis`
        （打开PostgreSQL的Application Stack Builder，找到“Spatial
        Extension”\|“PostGIS 2.1 \*”并安装）；

3.  使用pip安装程序需要的Python库，执行如下命令（在当前目录下）：

    -   Windows:  `pip install -r requirements-win.txt`

    -   Linux:    `pip install -r requirements-linux.txt`

    -   Windows 平台还需要进行操作：

        -   安装psycopg2，以完成django对PostgreSQL的兼容，请前往
            `http://www.stickpeople.com/projects/python/win-psycopg/`
            选择对应版本操作系统和Python版本的程序完成exe安装程序的下载安装；

        -   程序中部分旧代码仍然使用一些MySQL组件，请前往
            `http://www.codegood.com/archives/129`
            下载安装MySQLdb（对MySQL的依赖会在后续版本移除）；

    -   Linux平台还需要进行操作（请自行选择yum install命令或apt-get
        install命令）：

        -   `yum install python-devel postgresql-devel libgeos-devel libpq-devel
            libmysqlclient-devel`

        -   `apt-get install python-dev postgresql-dev libgeos-dev libpq-dev
            libmysqlclient-dev`

4.  建议的开发环境： `PyCharm 4.0.x` ；

5.  将代码clone至本地后，本地路径名中不得还有中文字符，否则django程序无法启动；

6.  为了便在本地进行调试，选择下面的任意一种方法：

    -   将PsyMap/pages/base\_generic.html代码文件当中的 `<base href="http://ccpl.psych.ac.cn/PsyMap/"/>`  行进行修改，将href修改为
        `http://127.0.0.1:端口号/PsyMap/` ；

    -   修改本机的host文件，增加一条DNS解析规则：`ccpl.psych.ac.cn	127.0.0.1`，如果使用此方法，启动程序时需要使用80端口。

7.  初次运行程序时候，需要创建数据库，并使用django的migrate命令建立数据库：

    -   （建议在pgAdmin
        III中操作）创建名为"PsyMap"的数据库，并且需要使用`postgis_21_sample`作为模板；

    -   在PostgreSQL当中执行如下SQL： `CREATE EXTENSION IF NOT EXISTS hstore`
        （该步骤必须）；

8.  进入项目根目录，在Shell当中执行如下命令：

    -   `python manage.py makemigrations`

    -   `python manage.py migrate`

    -   `python manage.py createsuperuser`

    -   到数据库中，进入表"auth\_user"，将刚刚创建的超级管理员的UID改为0（以避免数据迁移冲突）；

9.  对原有数据库进行迁移：

    1.  修改数据库中的auth\_user表，将Password、FirstName、LastName、EMail等字段的非空约束删除；

    2.  执行util目录下的db\_migrate.py来执行数据的迁移工作。

10. 完成上述操作之后，可以启动项目，`python manage.py runserver`。
