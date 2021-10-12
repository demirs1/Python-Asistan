from requests.api import request
from Modules.basemodules import Backend
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import selenium
from selenium import webdriver
import pyowm
import http.client
import pandas
import webbrowser
from selenium.webdriver.common.keys import Keys
import urllib.parse
from pyowm import OWM
from pyowm.utils import config
import html
import requests

confirm = ["evet", "onaylıyorum", "onay", "evet onaylıyorum", "onaylıyorum evet"]
mediamodule = Backend()
global driver

class Features:


    def __init__(self, multimedia_module):
        self.mediamodule = multimedia_module

    def mapfeature(self, data):
        data = data.split()
        self.mediamodule.speak("nereyi aramamı istersin")
        location = mediamodule.recordAudio()
        self.mediamodule.speak("Bekle mustafa Sana " + location + "  nerede olduğunu göstereceğim")
        driver = webdriver.Chrome("chromedriver.exe")  # Optional argument, if not specified will search path.
        driver.get("https://www.google.com/maps/place/" + location + "/&amp;");
        time.sleep(10)
        driver.quit()
        """
    def timefunc(self, data):
        time = ctime().split(sep=" ")
        newtime = time[3]
        return newtime

    def gunfunc(self, data):
        time = ctime().split(sep=" ")
        if time[1] == "Jan":
            time[1] = "Ocak"
        if time[1] == "Feb":
            time[1] = "Şubat"
        newtime = time[2] + " " + time[1] + " " + time[-1] + " " + time[3]
        return newtime
        
        
    def animsaticiolustur(self, data):
        try:
            self.mediamodule.speak("Hangi Saat için Anımsatıcı Kurmak istiyorsun?")
            time.sleep(5)
            data2 = self.mediamodule.recordAudio()
            if "saat" in data2:
                data2 = data2.split(sep=" ")
                saat = data2[1]
            elif "buçuk" in data2.split(sep=" "):
                saat = data2[0] + ":30"
            elif "çeyrek" in data2.split(sep=" "):
                saat = data2[0] + ":15"
            else:
                data2 = data2.split(sep=".")
                if len(data2[0]) == 1:
                    saat = "0" + data2[0] + ":" + data2[1]
                else:
                    saat = data2[0] + ":" + data2[1]
            self.mediamodule.speak("Anımsatıcı Adı Nedir?")
            time.sleep(1)
            data3 = self.mediamodule.recordAudio()
            animsaticinot = data3
            saat2 = pandas.DataFrame(data=[saat])
            animsaticinot2 = pandas.DataFrame(data=[animsaticinot])
            animsaticidatay = pandas.concat([animsaticinot2, saat2], axis=1)
            animsaticidatay.columns = ["Not", "Saat"]
            animsaticix = pandas.read_excel("animsatici.xlsx")
            animsaticidata = pandas.concat([animsaticix, animsaticidatay], axis=0, ignore_index=True)
            self.mediamodule.speak("Anımsatıcını {} saatine {} notuyla kuruyorum Onaylıyor musun?".format(saat, animsaticinot))
            time.sleep(6)
            dataconfirm = self.mediamodule.recordAudio()
            if dataconfirm in confirm:
                animsaticidata.to_excel("animsatici.xlsx")
                self.mediamodule.speak("Anımsatıcın Kuruldu.")
            else:
                self.mediamodule.speak("Lütfen Komutları Baştan ver")
        except:
            self.mediamodule.speak("Bir Hata Oluştu, Lütfen Komutları Baştan Ver.")

    def animsaticioku(self, data):
        self.mediamodule.speak("Anımsatıcıların Şu Şekilde")
        animsaticidata = pandas.read_excel("animsatici.xlsx")
        for i in range(0, len(animsaticidata)):
            print(str(animsaticidata.Saat[i]) + "da" + str(animsaticidata.Not[i]))
            self.mediamodule.speak(animsaticidata.Saat[i] + "da" + animsaticidata.Not[i])
            time.sleep(3)
            """
    def playyoutube(self, data):
        global driver
        data = data.split()
        self.mediamodule.speak("ne çalmamı istersin")
        parcaismi = mediamodule.recordAudio()
        encodeurl = urllib.parse.quote(parcaismi)
        for i in data[:-1]:
            parcaismi = parcaismi + i
        self.mediamodule.speak("Bekle  Senin için " + parcaismi + " yi çalıyorum")
        #url = 'https://www.youtube.com/results?search_query='+ parcaismi
        #driver = webbrowser.get().open(url)
        driver = webdriver.Chrome("chromedriver.exe")
        
        driver.get("https://www.youtube.com/results?search_query="+ encodeurl)
        #search_field = driver.find_element_by_name("search_query")
        #search_field.send_keys(parcaismi + Keys.ENTER)
        select_element = driver.find_elements_by_xpath('//*[@id="video-title"]')
        for option in select_element:
            option.find_element_by_xpath('//*[@id="video-title"]').click()
            break
        #url = 'https://www.youtube.com/results?search_query='+ parcaismi
        #webbrowser.get().open(url)
       
        return driver

    def stopsong(self, data):
        self.mediamodule.speak("durduruluyor")
        time.sleep(1)
        driver.quit()

    #def changemusic(self, data):
     #   self.mediamodule.speak("hangi şarkıya geçmemi istersin")
      #  change = mediamodule.recordAudio()
       # time.sleep(1)
        #sel = driver.find_element_by_xpath('//*[@id="search"]')
        #sel.send_keys(change)
        #time.sleep(1)
        #ara = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
        #ara.click()
        #time.sleep(2)
        #bas = driver.find_element_by_xpath('//*[@id="img"]')
        #bas.click()
        #return driver

    def searchquestion(self, data):
        data = data.split()
        self.mediamodule.speak("ne aramamı istersin")
        soru = mediamodule.recordAudio()
        for i in data[:-1]:
            soru = soru + "+" + i

        # TODO: Driver path eklentisi arayuz ile hazırlanabilir.
        drivery = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
        drivery.get("https://tr.wikipedia.org/wiki/" + soru);

       

    def createnote(self, data):
        data = data[7:]
        file = open("notlar.txt", "w")
        file.write(str(data.encode("utf-8")))
        file.close()
        self.mediamodule.speak("Not aldım")

    def readnote(self, data):
        file = open("notlar.txt", "r")
        self.mediamodule.speak("Notların şu şekilde")
        self.mediamodule.speak(file.read()[2:-1])
        self.mediamodule.speak("notların bu kadar")
        time.sleep(3)

    def emotionplaylist(self, data):
        self.mediamodule.speak("Hangisini çalayım? Mutlu mu, Normal mi? Depresif mi?")
        time.sleep(3)
        data2 = self.mediamodule.recordAudio()
        driver = webdriver.Chrome('chromedriver.exe')
        if "mutlu" in data2:
            driver.get("https://www.youtube.com/watch?v=uwT2kmral3A&start_radio=1&list=RDMMuwT2kmral3A");
        if "normal" in data2:
            driver.get("https://www.youtube.com/watch?v=wJGcwEv7838&start_radio=1&list=RDwJGcwEv7838");
        if "depresif" in data2:
            driver.get("https://www.youtube.com/watch?v=N3oCS85HvpY&start_radio=1&list=RDN3oCS85HvpY");
        return driver


    def news(self, data):
        self.mediamodule.speak("İşte senin için birkaç haber")
        url = 'https://www.mynet.com/'
        sekme=webbrowser.get().open(url)
    
    