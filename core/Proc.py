import os,thread,time,datetime

class Proc:
    def __init__(self,fname,bakpath,logpath):
        self.fname = fname
        self.bakpath = bakpath
        self.logpath = logpath
        now = datetime.datetime.now()
        self.oldfile = now.strftime(fname)
        self.newfile = now.strftime(fname)
        print self.oldfile
        print self.newfile

        self.tasks = []
 
    def check(self):
        now = datetime.datetime.now()
        tmp = now.strftime(self.fname)
        if self.newfile != tmp and os.path.isfile(self.logpath + tmp):
            self.newfile = tmp
 
    def run(self):
        if os.path.isfile(self.logpath + self.newfile):
            with open(self.logpath + self.newfile) as file_:
                while self.oldfile == self.newfile: 
                    line = file_.readline().strip()
                    if line:
                        self.dotasks(line)
                    else:
                        time.sleep(5)
                        self.check()
            os.rename(self.logpath + self.oldfile,self.bakpath + self.oldfile)
            self.oldfile = self.newfile
        else:
            print self.newfile + " not exist"
            time.sleep(5)
        self.run()

    def dotasks(self,line):
        for t in self.tasks:
            t.proc(line)

if __name__ == '__main__':
    proc = Proc(fname,bakpath,logpath)
    proc.tasks.append(3)
    proc.tasks.append(4)
    proc.run()
