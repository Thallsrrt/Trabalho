 #!/bin/bash
  2
  3 clear
  4 read -p 'Nome: ' NAME
  5 clear
  6 read -p 'E-Mail: ' EMAIL
  7 clear
  8 read -p 'Telefone: ' PHONE
  9 clear
 10 read -p 'RG: ' RG
 11 clear
 12 read -p 'CPF: ' CPF
 13 clear
 14 read -p 'Data de Nascimento: ' DATA
 15 clear
 16 read -p 'IP: ' IP
 17 clear
 18 read -p 'MASCARA: ' MASK
 19 clear
 20         echo $NAME | grep -E --color '^([a-z|A-Z]{1,}\ [a-z|A-Z]{1,}|[a-z|A-Z]{1,}){1,}$'
 21                 if [[ $? = 1 ]]; then
 22                         clear
 23                         echo 'Nome Invalido'
 24                         sleep 2
 25                         exit
 26                 fi
 27 clear
 28         echo $EMAIL | grep -E '^.{1,}@(hotmail|gmail|outlook)\.(com|com.br|br)'
 29                 if [[ $? = 1 ]]; then
 30                         clear
 31                         echo 'E-Mail Invalido'
 32                         sleep 2
 33                         exit
 34                 fi
 35 clear
 36         echo $PHONE | grep -E '^\([0-9]{2}\)[0-9]{5}-[0-9]{4}$'
 37                 if [[ $? = 1 ]]; then
 38                         clear
 39                         echo 'Telefone Invalido'
 40                         sleep 2
 41                         exit
 42                 fi
 43 clear
 44         echo $RG | grep -E '^[0-9]{2}(\.[0-9]{3}){2}-[0-9]'
 45                 if [[ $? = 1 ]]; then
 46                         clear
 47                         echo 'RG Invalido'
 48                         sleep 2
 49                         exit
 50                 fi
 51 clear
 52         echo $CPF | grep -E '^([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}$'
 53                 if [[ $? = 1 ]]; then
 54                         clear
 55                         echo 'CPF Invalido'
 56                         sleep 2
 57                         exit
 58                 fi
 59 clear
 60     echo $DATA | grep -E '^(0[0-9]|1[0-9]|2[0-9]|3[0-1])/(0[0-9]|1[0-2])/(19[0-9][0-9]|20[0-1][0-9])$'
 61                     if [[ $? = 1 ]]; then
 62                           clear
 63                           echo 'Data de Nascimento Invalido'
 64                           sleep 2
 65                           exit
 66                  fi
 67  clear
 68
 69         echo $IP | grep -E '^([0-9]{1,3}\.){3}[0-9]{1,3}$'
 70                 if [[ $? = 1 ]]; then
 71                         clear
 72                         echo 'IP Invalido'
 73                         sleep 2
 74                         exit
 75                 fi
 76 clear
 77         echo $MASK | grep -E '^([0-9]{1,3}\.){3}[0-9]{1,3}$'
 78                 if [[ $? = 1 ]]; then
 79                         clear
 80                         echo 'MASCARA Invalida'
 81                         sleep 2
 82                         exit
 83                 else
 84                         clear
 85                         echo 'Cadastro efetuado com sucesso'
 86                         sleep 2
 87                 fi

