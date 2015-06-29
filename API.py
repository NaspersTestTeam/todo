__author__ = 'Berk Kibarer'
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
from task import Task
from release import Release

class API:


    def __init__(self):
        pass

    @staticmethod
    def insertTask(self,acil,onemli,girisTarihi,bitisTarihi,jiraId,tanim,ekNot):
        __sonuc = False


        #Validasyon kontrolleri yapiliyor
        if(len(acil)==0 or len(onemli)==0 or len(girisTarihi)==0 or len(bitisTarihi)==0 or len(jiraId)==0 or len(tanim)==0 or len(ekNot)==0):
            print "Problem olustu"
            sys.exit()

        #Veri tabanina ekleme islemleri yapiliyor
        try:
            __con = lite.connect('/home/todo.db')

            cur = __con.cursor()

            cur.execute("INSERT INTO todo (acil, onemli, girisTarihi, bitisTarihi, jiraId, tanim, ekNot) VALUES (?, ?, ?, ?, ?, ?, ?)", (acil, onemli, girisTarihi, bitisTarihi, jiraId,tanim,ekNot))

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

    @staticmethod
    def allTasks(self,durum,tip):
        __sonuc = False

        #Validasyon kontrolleri yapiliyor

        if(durum!='aktif' and durum!='pasif' and durum!='hepsi'):
            print "Problem olustu"
            sys.exit()
        __sqlStr = "";
        if durum=='aktif': __sqlStr = "WHERE durum='aktif'"
        elif durum=='pasif': __sqlStr = "WHERE durum='pasif'"
        #Veri tabanina ekleme islemleri yapiliyor
        try:
            __con = lite.connect('/home/todo.db')

            cur = __con.cursor()

            cur.execute("SELECT taskId FROM todo "+__sqlStr+" ORDER BY durum ASC, acil DESC, onemli DESC")

            rows = cur.fetchall()
            __sonuc = []
            for task in rows:
                __taskId = task[0]

                __taskObj = Task(int(__taskId))

                __taskInfo = __taskObj.Bilgilerim()

                if tip=="all": __sonuc.append(__taskInfo)
                elif tip=="summary": __sonuc.append(__taskInfo)

        except lite.Error, e:

            if __con:
                __con.rollback()

            print(e.args[0])
            sys.exit(1)

        finally:

            if __con:
                __con.close()
        return __sonuc
    @staticmethod
    def allReleases(self):
        __sonuc = False


        #Veri tabanina ekleme islemleri yapiliyor
        try:
            __con = lite.connect('/root/db/todo.db')

            cur = __con.cursor()

            cur.execute("SELECT releaseLogId FROM releaseLogs")

            rows = cur.fetchall()
            __sonuc = []
            for release in rows:
                __releaseId = release[0]

                __releaseObj = Release(int(__releaseId))

                __releaseInfo = __releaseObj.Bilgilerim()
                __sonuc.append(__releaseInfo)

        except lite.Error, e:

            if __con:
                __con.rollback()

            print(e.args[0])
            sys.exit(1)

        finally:

            if __con:
                __con.close()
        return __sonuc
    @staticmethod
    def issueCanlidami(self,issueNo):
        __sonuc = False
        issueNo=str(issueNo)
        #Validasyon kontrolleri yapiliyor
        if(issueNo<=0):
            print "Problem olustu"
            sys.exit()

        #Veri tabanina ekleme islemleri yapiliyor
        try:
            __con = lite.connect('/root/db/todo.db')

            cur = __con.cursor()

            cur.execute("SELECT COUNT(releaseLogId) as sayac FROM releaseLogs WHERE issues LIKE '%"+issueNo+"%' AND  host='Canli'")


            row = cur.fetchone()
            if row[0]==1: __sonuc= True



        except lite.Error, e:

            if __con:
                __con.rollback()

            print(e.args[0])
            sys.exit(1)

        finally:

            if __con:
                __con.close()
        return __sonuc