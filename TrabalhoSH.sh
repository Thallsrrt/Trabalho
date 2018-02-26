 #!/bin/bash
  
   clear
   read -p 'Nome: ' NAME
   clear
   read -p 'E-Mail: ' EMAIL
   clear
   read -p 'Telefone: ' PHONE
   clear
  read -p 'RG: ' RG
  clear
  read -p 'CPF: ' CPF
  clear
  read -p 'Data de Nascimento: ' DATA
  clear
  read -p 'IP: ' IP
  clear
  read -p 'MASCARA: ' MASK
  clear
          echo $NAME | grep -E --color '^([a-z|A-Z]{1,}\ [a-z|A-Z]{1,}|[a-z|A-Z]{1,}){1,}$'
                  if [[ $? = 1 ]]; then
                          clear
                          echo 'Nome Invalido'
                          sleep 2
                          exit
                  fi
  clear
          echo $EMAIL | grep -E '^.{1,}@(hotmail|gmail|outlook)\.(com|com.br|br)'
                  if [[ $? = 1 ]]; then
                          clear
                          echo 'E-Mail Invalido'
                          sleep 2
                          exit
                  fi
  clear
          echo $PHONE | grep -E '^\([0-9]{2}\)[0-9]{5}-[0-9]{4}$'
                  if [[ $? = 1 ]]; then
                          clear
                          echo 'Telefone Invalido'
                          sleep 2
                          exit
                  fi
  clear
          echo $RG | grep -E '^[0-9]{2}(\.[0-9]{3}){2}-[0-9]'
                  if [[ $? = 1 ]]; then
                          clear
                          echo 'RG Invalido'
                          sleep 2
                          exit
                  fi
  clear
          echo $CPF | grep -E '^([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}$'
                  if [[ $? = 1 ]]; then
                          clear
                          echo 'CPF Invalido'
                          sleep 2
                          exit
                  fi
  clear
      echo $DATA | grep -E '^(0[0-9]|1[0-9]|2[0-9]|3[0-1])/(0[0-9]|1[0-2])/(19[0-9][0-9]|20[0-1][0-9])$'
                      if [[ $? = 1 ]]; then
                            clear
                            echo 'Data de Nascimento Invalido'
                            sleep 2
                            exit
                   fi
   clear
 
          echo $IP | grep -E '^([0-9]{1,3}\.){3}[0-9]{1,3}$'
                  if [[ $? = 1 ]]; then
                          clear
                          echo 'IP Invalido'
                          sleep 2
                          exit
                  fi
  clear
          echo $MASK | grep -E '^([0-9]{1,3}\.){3}[0-9]{1,3}$'
                  if [[ $? = 1 ]]; then
                          clear
                          echo 'MASCARA Invalida'
                          sleep 2
                          exit
                  else
                          clear
                          echo 'Cadastro efetuado com sucesso'
                          sleep 2
                  fi
