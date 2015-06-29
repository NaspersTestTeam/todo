__author__ = 'Berk Kibarer'
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys

class Task:

    __taskId = None

    def __init__(self,taskId):
        self.__taskId = taskId

    def Bilgilerim(self):
        __sonuc = None

        #Veri tabanina ekleme islemleri yapiliyor
        try:
            __con = lite.connect('/home/todo.db')
            cur = __con.cursor()

            cur.execute("SELECT * FROM todo WHERE taskId="+str(self.__taskId)+" LIMIT 1")
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

    def durumGuncelle(self,taskId,state):
        __sonuc = False

        taskId=int(taskId)
        state = str(state)
        #Validasyon kontrolleri yapiliyor
        if(taskId<=0 or (state!="aktif" and state!="pasif")):
            print "Problem olustu"
            sys.exit()

        #Veri tabanina ekleme islemleri yapiliyor
        try:
            __con = lite.connect('/home/todo.db')

            cur = __con.cursor()
            cur.execute("UPDATE todo SET durum='"+state+"' WHERE taskId='"+str(taskId)+"'")

            __con.commit()

            __sonuc=True

        except lite.Error, e:

            if __con:
                __con.rollback()

            print(e.args[0])
            sys.exit(1)

        finally:

            if __con:
                __con.close()
        return __sonuc
