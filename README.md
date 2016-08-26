# logprocs
日志实时入库（mongodb）工具

##使用方法
参考procs/demo

需要在cnf.py 文件配置日志文件名规则，日志路径，备份路径

    fname='access%Y%m%d.log'
    bakpath="/data1/"
    logpath="/var/log/nginx/"


在tasks增加日志解析规则和处理规则

在proc.py文件增加task
    demo = Demo.Demo()
    proc.tasks.append(demo)

##启动

    nohup python -u proc.py > nohup.out1 2>&1 &
