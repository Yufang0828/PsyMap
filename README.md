# psymap
NOTE：
  1. 在window平台，需要需要安装win_inet_pton,并修改net.py(属于web.py)文件，添加导入win_inet_pton
    win_inet_pton下载地址：https://github.com/hickeroar/win_inet_pton
    net.py(python_path\Lib\site-packages\web\)文件: 手动添加 "import win_inet_pton" 语句  

  2. "static\css\customize-less" 目录下为自定义的less文件，因为项目中引用的是customize\psymap.css，所以要修改可以直接修改css文件     或者修改psymap.less文件，后一种方法需要手动执行命令（grunt less）或者pycharm中使用file watcher功能。
