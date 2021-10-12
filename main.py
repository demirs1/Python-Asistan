from selenium import webdriver
from Modules.basemodules import Backend
from Modules.mainfeatures import Features
from random import randint
from time import ctime
import pandas
import time
import os
from datetime import datetime
import subprocess
from pygame import mixer
import pygame

nasilsincumeleleri = ["nasılsın","naber","ne haber","napıyorsun","nasıl gidiyor","naber","napıyon","nasıl","nabıyon"]
iltifat = ["mükemmelsin","çok iyisin","mükemmel","efsane","saol","teşekkürler","çok","iyi","çok iyi"]
donus = ["iyiyim sen","çok iyiyim","biraz keyifsizim"]
donustesekkur = ["Çok teşekkürler","beni utandırıyorsun","utandım","teşekkürler","yardımcı olabildiysem ne mutlu bana"]
saat = ["saat","kaç","saat kaç","kaç saat","zaman"]
gun = ["bugün ayın kaçı","ayın","kaçı","bugün günlerden ne","günler","günlerden","bu gün ayın"]
maps = ["nerede","nerededir","nerda","nerde","neresi"]
playyoutube = ["çal","oynat","aç","youtube aç","yutup aç","yutub aç"]
search = ["nedir","kimdir","ne","nasıl"]
tempature = ["derece","hava","kaç","hava kaç","sıcaklık kaç","sıcaklık","hava durumu"]
note = ["not al","not alır mısın","not"]
noteread = ["notlarımı oku","notları oku","notlar"]
playlist = ["müzik listemi çal","müzik listem","müzik","playlist","listem","müzik listeleri"]
musik = ["alan","surrender"]
haber = ["haberler","haberleri","haber","gündem","gazete","oku","haberleri oku"]
stopsong = ["şarkıyı kapat","şarkıyı durdur","dur dur","kapat"]
kapatma = ["sistemi kapat","uyu","kendini kapat"]
kaviopen = ["hey kavi","hey","alo","kavi","açıl","açıl susam açıl","açın"]
animsatici = ["anımsatıcı oluştur","anımsatıcı kur","anımsatıcı başlat","anımsatıcı oluş"]
animsaticioku = ["anımsatıcılarım","anımsatıcımı oku","anımsatıcılar","anımsatıcılarımı oku","anımsatıcı oku","anımsatıcım"]
uygulama = ["uygulama","uygulama aç"]
changemusic = ["şarkı değiştir"]


def kavi(media, utility, data):
    if data in nasilsincumeleleri:
        media.speak(donus[randint(0, 2)])
    if data in iltifat:
        media.speak(donustesekkur[randint(0, 4)])
    if data in saat:
        media.speak(utility.timefunc(data))
    if data in gun:
        media.speak(utility.gunfunc(data))
    if data in maps:
        utility.mapfeature(data)
    if data in playyoutube:
        global driver
        driver = utility.playyoutube(data)
    if data in stopsong:
        utility.stopsong(driver)
    if data in changemusic:
        utility.stopsong(driver)
    if data.split() in search:
        utility.searchquestion(data)
    if data in tempature:
        utility.tempature(data)
    if data in note:
        utility.createnote(data)
    if data in noteread:
        utility.readnote(data)
    if data in playlist:
        utility.emotionplaylist(data)
    if data in haber:
        utility.news(data)
    if data in animsatici:
        utility.animsaticiolustur(data)
    if data in animsaticioku:
        utility.animsaticioku(data)



if __name__ == '__main__':
    mediamodule = Backend()
    utilitymodule = Features(mediamodule)
    mediamodule.speak("Merhaba Mustafa ")
    while True:
        
        data = mediamodule.recordAudio()
        if data in playyoutube:
            utilitymodule.playyoutube(data)
            time.sleep(0.5)
            data = mediamodule.recordAudio()
        elif data in kapatma:
            mediamodule.speak("Görüşürüz")
            exit()
        elif data in maps:
            utilitymodule.mapfeature(data)
            time.sleep(1)
            data = mediamodule.recordAudio()
        elif data in stopsong:
            utilitymodule.stopsong(data)
            time.sleep(1)
            data = mediamodule.recordAudio()
       # elif data in changemusic:
       #      utilitymodule.changemusic(data)
       #      time.sleep(1)
       #      data = mediamodule.recordAudio()
        elif data in saat:

            mediamodule.speak(datetime.now().strftime("%H:%M:%S"))

        elif data in playlist:
            mediamodule.speak("hangi müzik açmamı istersin")
            datal = mediamodule.recordAudio()
            if datal in musik:
                
                mixer.init()
                mixer.music.load("alan.mp3")
                mixer.music.play()
                
               # mixer.music.stop()
        elif 'müzik kapat' in data:
            mixer.music.stop()
            data = mediamodule.recordAudio()
        elif data in kaviopen:
            data = mediamodule.recordAudio()
            mediamodule.playSound("hello.mp3")
            time.sleep(0.5)
        elif data in haber:
            utilitymodule.news(data)
            time.sleep(1)
            #data = mediamodule.recordAudio()
        elif data in tempature:
            utilitymodule.tempature(data)
            time.sleep(1)
            data = mediamodule.recordAudio()
        elif data in search:
            utilitymodule.searchquestion(data)
            time.sleep(1)
            data = mediamodule.recordAudio()
        elif data in uygulama:
            mediamodule.speak("açmak istediğin uygulama ismi nedir")
            isim = mediamodule.recordAudio()
            if 'chrome' in isim:
                subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
                time.sleep(1)
                continue
            elif 'discord' in isim:
                subprocess.Popen("C:/Users\Asingx/AppData/Local/Discord/Update.exe")
                time.sleep(1)
                
            elif 'notepad' in isim:
                tol2 = "C:/AppData/Local/Discord/Update.exe"
                subprocess.Popen("C:/notepad++.exe")
                time.sleep(1)
            elif 'aslan' in isim:
                subprocess.Popen("C:/Program Files/brave.exe")
                time.sleep(5)
                subprocess.STDOUT
        else:
            kavi(mediamodule, utilitymodule, data)