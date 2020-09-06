#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import os 
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")
print("""
Tarama Programına Hoşgeldiniz.

Keşif Aşaması

1) Tüm sistemi ping ile tarama
2) TCP SYN ile tarama
3) TCP ACK ile  tarama
4) ICMP Echo Request ile tarama
5) UDP Ping ile tarama
6) Paketin yol analizi

 
Port Tarama Aşaması

7) Hızlı Tarama (Sistemde loglanmaz)
8) Tcp Scan (Sistemde loglanır)
9) Servis ve Versiyon Bilgisi 
10) İşletim Sistemi Bilgisi

""")

islemno = raw_input("İşlem Numarasını Giriniz: ")

if(islemno=="1"):
	hedefip = raw_input("Hedef IP Adresi Giriniz: ")
	os.system("nmap -sP " + hedefip)
	
elif(islemno=="2"):
	hedefip = raw_input("Hedef IP Adresi Giriniz: ")
	os.system("nmap -PS " + hedefip)
	
elif(islemno=="3"):
	hedefip = raw_input("Hedef IP Adresi Giriniz: ")
	os.system("nmap -PA " + hedefip)
	
elif(islemno=="4"):
	hedefip = raw_input("Hedef IP Adresi Giriniz: ")
	os.system("nmap -PE " + hedefip)
	
elif(islemno=="5"):
	hedefip = raw_input("Hedef IP Adresi Giriniz: ")
	os.system("nmap -PU " + hedefip)

elif(islemno=="6"):
	hedefip = raw_input("Hedef IP Adresi Giriniz: ")
	os.system("nmap -traceroute " + hedefip)
	
elif(islemno=="7"):
	hedefip = raw_input("Hedef IP Adresi Giriniz: ")
	os.system("nmap -sS -sV " + hedefip)
	
elif(islemno=="8"):
	hedefip = raw_input("Hedef IP Adresi Giriniz: ")
	os.system("nmap -sT " + hedefip)
	
elif(islemno=="9"):
	hedefip = raw_input("Hedef IP Adresi Giriniz: ")
	os.system("nmap -sS -sV " + hedefip)
	
elif(islemno=="10"):
	hedefip = raw_input("Hedef IP Adresi Giriniz: ")
	os.system("nmap -sS -O " + hedefip)

else:
	print("Hatalı Giriş Yaptınız, Program Kapatıldı.")
	
