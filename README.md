# 心理地图

NOTE：

  1. 本应用前端使用bootstrap 3搭建，后端基于Django 1.8.x搭建，请特别注意django版本号，否则部分程序无法调试通过；
  2. 程序后台使用的数据库为PostgreSQL 9.4，并且不兼容MySQL，请先安装PostgreSQL；
  3. 安装PostgreSQL之后，还需要安装下列软件，以完成django对PostgreSQL的兼容：
    1) 安装PostGIS（用于地理位置信息处理），方法参照 ``https://docs.djangoproject.com/en/1.7/ref/contrib/gis/install/#postgis`` ； 
    2) 安装shapely库：pip install shapely
  4. 在PostgreSQL当中执行如下SQL： ``CREATE EXTENSION IF NOT EXISTS hstore`` ；
  5. 建议的开发环境： PyCharm 4.0.x；
  6. 调试程序时，请将base_generic.html代码文件当中的
```html
  	<base href="http://ccpl.psych.ac.cn/PsyMap/"/>
```
  一行进行修改，将href修改为 “http://127.0.0.1:端口号/PsyMap/” ，以便在本地进行调试。
  6. 初次运行程序时候，需要使用django的migrate命令建立数据库。