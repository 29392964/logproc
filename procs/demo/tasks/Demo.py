import Base
import datetime
class Demo(Base.Base):
    def proc(self,row):
        self.parse(row)
        #self.demo.update({"md5":self.data["md5"]},self.data,True)
        print "Demo " + self.data["ip"]

if __name__ == '__main__':
    demo = Demo()
    demo.proc('"2016-06-28T17:20:00+08:00" "123.1.1.1" "POST /index HTTP/1.1" "200"')
