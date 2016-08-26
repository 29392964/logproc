import sys
sys.path.append("..")
sys.path.append("../../")
from core.Proc import Proc
from cnf import fname,bakpath,logpath
from tasks import Demo

if __name__ == '__main__':
    proc = Proc(fname,bakpath,logpath)
    demotask = Demo.Demo()
    proc.tasks.append(demotask)
    proc.run()

