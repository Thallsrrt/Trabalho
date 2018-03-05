#!/usr/bin/pyhton
#-*- coding: utf8 -*-
  
import os
  
import re
  
  
os.system("clear")
 
NAME = raw_input("Nome :")
 
 
os.system("clear")
 
EMAIL = raw_input("E-Mail :")
 
 
os.system("clear")
 
PHONE = raw_input("Telefone :")
 
 
os.system("clear")
 
RG = raw_input("RG :")
 
 
os.system("clear")
 
CPF = raw_input("CPF :")
 
 
os.system("clear")
 
DATA = raw_input("Data de Nascimento: ")
 
 
os.system("clear")
 
IP = raw_input("IP :")
 
 
os.system("clear")
 
MASK = raw_input("Mascara :")
 
 
os.system("clear")
 
if re.match('^([A-Z|a-z]{1,}\ [A-Z|a-z]{1,}|[A-Z|a-z]{1,})$', NAME):
 
          print("Nome correto")
 
else:
 
          print("Nome invalido")
 
 
if re.match('^.{1,}@(hotmail|gmail|outlook)\.(com|com.br|br)$', EMAIL):
 
          print("E-mail correto")
else:

          print("E-Mail invalido")
 
 
if re.match('^\([0-9]{2}\)[0-9]{5}-[0-9]{4}$', PHONE):
 
          print("Telefone correto")
 
else:
 
          print("Telefone invalido")
 
 
if re.match('^[0-9]{2}(\.[0-9]{3}){2}-[0-9]$', RG):
 
          print("RG correto")
 
else:
 
          print("RG invalido")
 
 
if re.match('^([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}$', CPF):
 
          print("CPF correto")
 
else:
 
          print("CPF invalido")
 
if re.match('^(0[1-9]|[12][0-9]|3[0-1])/(0[1-9]|1[0-2])/(19[0-9]{2}|200[0-9]|201[0-7])$', DATA):
 
          print("Data de Nascimento correto")
 
else:
          print("Data de Nascimento invalido")

if re.match('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', IP):

         print("IP correto")

else:
         print("IP invalido")


if re.match('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', MASK):

         print("Máscara correta")

else:
         
         print("Mascara invalido")
