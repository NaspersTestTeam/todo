__author__ = 'Berk Kibarer'
# !/usr/bin/python
# -*- coding: utf-8 -*-

from API import API
from task import Task
class Controller:
    __sonuc = None
    __sonucStr = "Bir problem olustu!"

    def __init__(self):
        pass

    @staticmethod
    def islemiUygula(self, taskStr,data):
        if taskStr == 'isGir':
            #__acil,__onemli,__girisTarihi,__bitisTarihi,__jiraId,__tanim,__ekNot bilgilerini bekler
            Controller.__sonuc = API.insertTask(object,data[0],data[1],data[2],data[3],data[4],data[5],data[6])
            if Controller.__sonuc == True:
                Controller.__sonucStr = "Girdi basariyla eklendi."
            return Controller.__sonucStr
        elif taskStr== 'tumIslerim':
            #durum bilgisi bekler
            Controller.__sonuc = API.allTasks(object,data,"all")

            if Controller.__sonuc != False:
                Controller.__sonucStr = Controller.__sonuc

            return Controller.__sonucStr
        elif taskStr== 'tumSurumler':
            #durum bilgisi bekler
            Controller.__sonuc = API.allReleases(object)

            if Controller.__sonuc != False:
                Controller.__sonucStr = Controller.__sonuc

            return Controller.__sonucStr
        elif taskStr == 'isiKaliciSil':
            #taskId bekler
            Controller.__sonuc = API.removePerm(object,data)
            if Controller.__sonuc == True:
                Controller.__sonucStr = "Girdi basariyla kalici olarak silindi."
            return Controller.__sonucStr
        elif taskStr == 'aktifYap':
            #taskId bekler
            taskObj = Task(int(data))

            Controller.__sonuc = taskObj.durumGuncelle(data,"aktif")
            if Controller.__sonuc == True:
                Controller.__sonucStr = "Girdi basariyla aktif olarak guncellendi."
            return Controller.__sonucStr
        elif taskStr == 'pasifYap':
            #taskId bekler
            taskObj = Task(int(data))
            Controller.__sonuc = taskObj.durumGuncelle(data,"pasif")
            if Controller.__sonuc == True:
                Controller.__sonucStr = "Girdi basariyla pasif olarak guncellendi."
            return Controller.__sonucStr
        elif taskStr == 'issueCanlidami':
            #issueNo bekler
            print data
            SystemExit(1)
            Controller.__sonuc = API.issueCanlidami(object,data)
            if Controller.__sonuc == True:
                Controller.__sonucStr = "Canli ortamda"
            else: Controller.__sonucStr = "Canlida degil"
            return Controller.__sonucStr
        elif taskStr== 'tumIslerimOzet':
            #durum bilgisi bekler
            Controller.__sonuc = API.allTasks(object,data,"summary")

            if Controller.__sonuc != False:
                Controller.__sonucStr = Controller.__sonuc

            return Controller.__sonucStr