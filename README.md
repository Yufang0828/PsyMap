# 心理地图

##开发环境部署需知##

 1. 本应用前端使用bootstrap 3搭建，后端基于Django 1.8.x搭建，请特别注意django版本号，否则部分程序无法调试通过；
 
 2. 请使用Python 2.7.x作为python运行环境，建议安装anaconda发行版： ``https://store.continuum.io/cshop/anaconda/`` ；
 3. 程序中部分旧代码仍然使用一些MySQL组件，请前往 ``http://www.codegood.com/archives/129`` 下载安装MySQLdb（对MySQL的依赖会在后续版本移除）；
 
 4. 程序后台使用的数据库为PostgreSQL 9.4，并且不兼容MySQL，请先安装PostgreSQL；
 
 5. 安装PostgreSQL之后，还需要安装下列软件，以完成django对PostgreSQL的兼容：

    - 安装PostGIS（用于地理位置信息处理），方法参照 ``https://docs.djangoproject.com/en/1.7/ref/contrib/gis/install/#postgis`` ； 
    - 安装psycopg：请前往 ``http://www.stickpeople.com/projects/python/win-psycopg/`` 选择对应版本操作系统和Python版本的程序完成exe安装程序的下载安装；
    - 安装shapely 1.4.0库（请勿安装其他版本）：请前往 ``https://pypi.python.org/pypi/Shapely/1.4.0`` 下载对应操作系统和Python版本的shapely库；

 6. 在PostgreSQL当中执行如下SQL： ``CREATE EXTENSION IF NOT EXISTS hstore``  （该步骤必须）；
 7. 建议的开发环境： PyCharm 4.0.x；
 8. 将代码clone至本地后，本地路径名中不得还有中文字符，否则django程序无法启动；
 9. 调试程序时，请将base_generic.html代码文件当中的 ```<base href="http://ccpl.psych.ac.cn/PsyMap/"/>```
  一行进行修改，将href修改为 “http://127.0.0.1:端口号/PsyMap/” ，以便在本地进行调试；
 10. 初次运行程序时候，需要使用django的migrate命令建立数据库。