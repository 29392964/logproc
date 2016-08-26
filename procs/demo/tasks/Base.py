# -*- coding: utf-8 -*-
import sys,datetime,os
import pymongo,hashlib
import pymongo as MongoClient
sys.path.append("../../")
sys.path.append("../../../")
import config.mod_config as c
from calendar import monthrange

class Base:
    def __init__(self):
        self.m = pymongo.MongoClient(c.getConfig("mongo","mongouri"))
        self.demo = self.m.get_database("test").get_collection("demo")
        self.data = {}
    
    def md5(self,src):
        m2 = hashlib.md5()
        m2.update(src)
        return m2.hexdigest()

    def parse(self,line):
        tmp = line.split("\" \"")
        self.data["time"] = datetime.datetime.strptime( tmp[0].strip().strip("\""),"%Y-%m-%dT%H:%M:%S+08:00")
        self.data["ip"] = tmp[1].strip()
        self.data["md5"] = self.md5(line)

