__author__ = 'Berk Kibarer'
#!/usr/bin/python
# -*- coding: utf-8 -*-
from controller import Controller
from xml.dom.minidom import parseString
import subprocess




__sonuc = "Bir problem olustu!"
__data = None
print("Secenekler: \n1)Yeni task gir\n2)Taskleri getir\n3)Isi kalici olarak sil\n4)Aktif olarak guncelle\n5)Pasif olarak guncelle\n6)Surum kayitlarini getir\n7)Issue canlida mi?\n8)Tum islerin ozeti\n")
__taskInput = int(raw_input("Secenek sayisini girin: "))

print "Sectiginiz sayi: %d" % (__taskInput)

if __taskInput==1:
    __acil = raw_input("Acil: ")
    __onemli = raw_input("Onemli: ")
    __girisTarihi = raw_input("Giris Tarihi: ")
    __bitisTarihi = raw_input("Bitis Tarihi: ")
    __jiraId = raw_input("JIRA Id: ")
    __tanim = raw_input("Tanim: ")
    __ekNot = raw_input("Ek Not: ")
    __data =(__acil,__onemli,__girisTarihi,__bitisTarihi,__jiraId,__tanim,__ekNot)
    __sonuc = Controller.islemiUygula(object,"isGir",__data)
elif __taskInput==2:
    __durum = raw_input("Durum: ")
    __allTasks = Controller.islemiUygula(object,"tumIslerim",__durum)
    if __allTasks!=False:
        __sonuc=True
        dataStr = ""
        for task in __allTasks:
            taskId = str(task[0])
            jiraId = str(task[6])
            tanim = str(task[7])
            ekNot = str(task[8])
            acil = str(task[1])
            onemli = str(task[2])
            girisTarihi = str(task[3])
            hedefTarihi = str(task[4])
            durum = str(task[5])
            dataStr += ("""<Task>
                            <TaskId>%s</TaskId>
                            <JiraId>%s</JiraId>
                            <Tanim>%s</Tanim>
                            <EkNot>%s</EkNot>
                            <Acil>%s</Acil>
                            <Onemli>%s</Onemli>
                            <GirisTarihi>%s</GirisTarihi>
                            <HedefTarihi>%s</HedefTarihi>
                            <Durum>%s</Durum>
                           </Task>""" % (taskId,jiraId,tanim,ekNot,acil,onemli,girisTarihi,hedefTarihi,durum))
        doc = parseString("""
                <TestTeamTasks>
                                %s
                 </TestTeamTasks>""" % dataStr)
        with open("/home/isListesi.xml", "w") as f:
            f.write(doc.toxml())

        subprocess.call(["cat","/home/isListesi.xml"])
elif __taskInput==3:
    __data = raw_input("Task Id: ")
    __sonuc = Controller.islemiUygula(object,"isiKaliciSil",__data)
elif __taskInput==4:
    __data = raw_input("Task Id: ")
    __sonuc = Controller.islemiUygula(object,"aktifYap",__data)
elif __taskInput==5:
    __data = raw_input("Task Id: ")
    __sonuc = Controller.islemiUygula(object,"pasifYap",__data)
elif __taskInput==6:
    __allTasks = Controller.islemiUygula(object,"tumSurumler",__data)
    if __allTasks!=False:
        __sonuc=True
        dataStr = ""
        for task in __allTasks:
            releaseLogId = str(task[0])
            tredmineId = str(task[1])
            surumNo = str(task[2])
            issues = str(task[3])
            host = str(task[4])
            tarih = str(task[5])
            durum = str(task[6])
            dataStr += ("""<Release>
                            <ReleaseLogId>%s</ReleaseLogId>
                            <TredmineId>%s</TredmineId>
                            <SurumNo>%s</SurumNo>
                            <Issues>%s</Issues>
                            <Host>%s</Host>
                            <Tarih>%s</Tarih>
                            <Durum>%s</Durum>
                           </Release>""" % (releaseLogId,tredmineId,surumNo,issues,host,tarih,durum))
        doc = parseString("""
                <TestTeamReleaseLogs>
                                %s
                 </TestTeamReleaseLogs>""" % dataStr)
        with open("/home/surumListesi.xml", "w") as f:
            f.write(doc.toxml())

        subprocess.call(["cat","/home/surumListesi.xml"])
elif __taskInput==7:
    __data = raw_input("Issue No: ")
    __sonuc = Controller.islemiUygula(object,"issueCanlidami",__data)
elif __taskInput==8:
    __durum = raw_input("Durum: ")
    __allTasks = Controller.islemiUygula(object,"tumIslerimOzet",__durum)
    __sonucStr = "\n\n"
    for task in __allTasks:
        __sonucStr = __sonucStr +" [ID: "+str(task[0])+"] - "+str(task[7])+" [ACIL: "+str(task[1])+"]"+" [ONEMLI: "+str(task[1])+"]"  +"\n"
    print __sonucStr
    __sonuc = True
print("\nSonuc: %s" % (__sonuc))


