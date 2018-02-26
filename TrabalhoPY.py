 1 #!/usr/bin/bash
  2 #-*- coding: utf8 -*-
  3
  4 import os
  5
  6 import re
  7
  8
  9 os.system("clear")
 10
 11 NAME = raw_input("Nome :")
 12
 13
 14 os.system("clear")
 15
 16 EMAIL = raw_input("E-Mail :")
 17
 18
 19 os.system("clear")
 20
 21 PHONE = raw_input("Telefone :")
 22
 23
 24 os.system("clear")
 25
 26 RG = raw_input("RG :")
 27
 28
 29 os.system("clear")
 30
 31 CPF = raw_input("CPF :")
 32
 33
 34 os.system("clear")
 35
 36 DATA = raw_input("Data de Nascimento: ")
 37
 38
 39 os.system("clear")
 40
 41 IP = raw_input("IP :")
 42
 43
 44 os.system("clear")
 45
 46 MASK = raw_input("Mascara :")
 47
 48
 49 os.system("clear")
 50
 51 if re.match('^([A-Z|a-z]{1,}\ [A-Z|a-z]{1,}|[A-Z|a-z]{1,})$', NAME):
 52
 53         print("Nome correto")
 54
 55 else:
 56
 57         print("Nome invalido")
 58
 59
 60 if re.match('^.{1,}@(hotmail|gmail|outlook)\.(com|com.br|br)$', EMAIL):
 61
 62         print("E-mail correto")

 64 else:
 65
 66         print("E-Mail invalido")
 67
 68
 69 if re.match('^\([0-9]{2}\)[0-9]{5}-[0-9]{4}$', PHONE):
 70
 71         print("Telefone correto")
 72
 73 else:
 74
 75         print("Telefone invalido")
 76
 77
 78 if re.match('^[0-9]{2}(\.[0-9]{3}){2}-[0-9]$', RG):
 79
 80         print("RG correto")
 81
 82 else:
 83
 84         print("RG invalido")
 85
 86
 87 if re.match('^([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}$', CPF):
 88
 89         print("CPF correto")
 90
 91 else:
 92
 93         print("CPF invalido")
 94
 95 if re.match('^(0[1-9]|[12][0-9]|3[0-1])/(0[1-9]|1[0-2])/(19[0-9]{2}|200[0-9]|201[0-7])$', DATA):
 96
 97         print("Data de Nascimento correto")
 98
 99 else:
100
101         print("Data de Nascimento invalido")
102
103
104 if re.match('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', IP):
105
106         print("IP correto")
107
108 else:
109         print("IP invalido")
110
111
112 if re.match('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', MASK):
113
114         print("Máscara correta")
115
116 else:
117         
118         print("Mascara invalido")#!/usr/bin/python
