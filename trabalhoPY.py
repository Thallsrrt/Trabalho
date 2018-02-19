 #!/usr/bin/python
  2 #-*- coding: utf8 -*-
  3
  4 import os
  5 import re
  6
  7 os.system("clear")
  8
  9 NAME = raw_input("Nome :")
 10 os.system("clear")
 11
 12 EMAIL = raw_input("E-Mail :")
 13 os.system("clear")
 14
 15 PHONE = raw_input("Telefone :")
 16 os.system("clear")
 17
 18 RG = raw_input("RG :")
 19 os.system("clear")
 20
 21 CPF = raw_input("CPF :")
 22 os.system("clear")
 23
 24 DATA = raw_input("Data de Nascimento: ")
 25 os.system("clear")
 26
 27 IP = raw_input("IP :")
 28 os.system("clear")
 29
 30 MASK = raw_input("Mascara :")
 31 os.system("clear")
 32
 33 NOME = re.findall(r'([A-Z|a-z]{1,}\ [A-Z|a-z]{1,}|[A-Z|a-z]{1,})', NAME)
 34
 35 if NOME:
 36         print(NOME)
 37         os.system("clear")
 38
 39 else:
 40         print("Nome invalido")
 41
 42 MAIL = re.findall(r'^.{1,}@(hotmail|gmail|outlook)\.(com|com.br|br)', EMAIL)
 43
 44 if MAIL:
 45         print(MAIL)
 46 else:
 47         print("E-Mail invalido")
 48
 49 HONE = re.findall(r'^\([0-9]{2}\)[0-9]{5}-[0-9]{4}$', PHONE)
 50
 51 if HONE:
 52     print(HONE)
 53 else:
 54     print("Telefone Invalido")
 55
 56 G = re.findall(r'^[0-9]{2}(\.[0-9]{3}){2}-[0-9]', RG)
 57
 58     if G:
 59         print(G)
 60     else:
