__author__ = 'Berk Kibarer'
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys

class Release:

    __releaseId = None

    def __init__(self,releaseId):
        self.__releaseId = releaseId

    def Bilgilerim(self):
        __sonuc = None

        #Veri tabanina ekleme islemleri yapiliyor
        try:
            __con = lite.connect('/root/db/todo.db')
            cur = __con.cursor()

            cur.execute("SELECT * FROM releaseLogs WHERE releaseLogId="+str(self.__releaseId)+" LIMIT 1")
            __sonuc = cur.fetchone()


        except lite.Error, e:

            if __con:
                __con.rollback()

            print(e.args[0])
            sys.exit(1)

        finally:

            if __con:
                __con.close()
        return __sonuc