# logprocs
日志实时入库（mongodb）工具

##mongodb配置

修改文件/config/app.conf中相关数据

##task使用方法

参考/procs/demo

需要在/procs/demo/cnf.py 文件配置日志文件名规则，日志路径，备份路径

    fname='access%Y%m%d.log'
    bakpath="/data1/"
    logpath="/var/log/nginx/"


在tasks增加日志解析规则和处理规则

在/procs/demo/proc.py文件增加task

    demo = Demo.Demo()
    proc.tasks.append(demo)

##启动
    cd procs/demo
    nohup python -u proc.py > nohup.out1 2>&1 &
